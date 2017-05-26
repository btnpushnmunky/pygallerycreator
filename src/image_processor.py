from PIL import Image
import os

THUMB_SIZE = (256, 256)
LARGE_SIZE = (2048, 2048)


def create_images(user_images_dir, base_save_path):
    """
    Open the original image files and save a thumb and gallery version
    """
    thumb_dir = os.path.join(base_save_path, "thumbs")
    large_image_dir = os.path.join(base_save_path, "large_imgs")
    os.mkdir(thumb_dir)
    os.mkdir(large_image_dir)

    def open_image(img_filename):
        """
        Open an image file and return it and its name
        :param img_filename: Filename of image as a string
        :return: Image with name excluding extension
        """
        final_img_name = img_filename.split('.')[0]
        outfile = ".".join((final_img_name, "jpg"))
        img = Image.open(os.path.join(user_images_dir, img_filename))
        return img, outfile

    def create_image_versions(original_image):
        """
        Create the thumbnail and large image for an image file
        :param original_image: Filename as string
        :return: None
        """
        img, img_name = open_image(original_image)
        img.thumbnail(THUMB_SIZE)
        thumb_file = os.path.join(thumb_dir, img_name)
        img.save(thumb_file)
        large_img, large_img_name = open_image(original_image)
        large_img.thumbnail(LARGE_SIZE)
        large_file = os.path.join(large_image_dir, large_img_name)
        large_img.save(large_file)

    for file_name in os.listdir(user_images_dir):
        create_image_versions(file_name)
