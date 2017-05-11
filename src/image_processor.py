from PIL import Image
import os

THUMB_SIZE = (128, 128)


def create_img_directories(base_path):
    """
    Create a directory for the thumbs and resized 'large' images
    """
    

def create_images(user_images_dir, base_path):
    """
    Open the original image files and save a thumb and gallery version
    """
    os.mkdir(os.path.join(base_path, "large_imgs"))
    os.mkdir(os.path.join(base_path, "thumbs"))

    for img_file in os.listdir(user_images_dir):
        img_path = os.path.join(user_images_dir, img_file)
        img = Image.open(img_path)

        # TODO: Create 'large' file and write to correct directory
        # TODO: Create thumb and write to correct directory
