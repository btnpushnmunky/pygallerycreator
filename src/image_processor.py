from PIL import Image
import os

THUMB_SIZE = (512, 512)

def create_images(user_images_dir, base_save_path):
    """
    Open the original image files and save a thumb and gallery version
    """
    os.mkdir(os.path.join(base_save_path, "large_imgs"))
    os.mkdir(os.path.join(base_save_path, "thumbs"))
    thumb_dir = os.path.join(base_save_path, "thumbs")
    large_image_dir = os.path.join(base_save_path, "large_imgs")

    for img_file in os.listdir(user_images_dir):

        # TODO: Create 'large' file and write to correct directory

        thumb_name = img_file.split('.')[0]
        outfile = ".".join((thumb_name, "jpg"))
        img = Image.open(os.path.join(user_images_dir, img_file))
        img.thumbnail(THUMB_SIZE)
        thumb_file = os.path.join(thumb_dir, outfile)
        img.save(thumb_file)
