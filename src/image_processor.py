from PIL import Image
import os

def create_thumb_dir(base_path):
   os.mkdir(os.path.join(base_path,"thumbs"))
