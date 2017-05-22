import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_desktop():
    return os.path.join(os.path.expanduser("~"), "Desktop")

desktop = get_desktop()

default_dist_path = os.path.join(desktop, 'py_gallery_dist')


def make_dist_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print("The specified destination already exists.")

def copy_resources(path):
    shutil.copytree("vendor/lightbox", f"{path}/lightbox")
    shutil.copytree("vendor/montage", f"{path}/montage")
