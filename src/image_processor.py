from PIL import Image
import os


def create_thumb_dir(base_path):
   os.mkdir(os.path.join(base_path,"thumbs"))


def create_resized_images_dir(base_path):
   os.mkdir(os.path.join(base_path, "large_imgs"))
