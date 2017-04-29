from PIL import Image
import os


def create_img_directories(base_path):
    os.mkdir(os.path.join(base_path, "large_imgs"))
    os.mkdir(os.path.join(base_path,"thumbs"))
