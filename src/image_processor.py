from PIL import Image
import os


def create_img_directories(base_path):
    """
    Create a directory for the thumbs and resized 'large' images
    """
    os.mkdir(os.path.join(base_path, "large_imgs"))
    os.mkdir(os.path.join(base_path, "thumbs"))


def create_images(user_images_dir):
    """
    Open the original image files and save a thumb and gallery version
    """
    pass
