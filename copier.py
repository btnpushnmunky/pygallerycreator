import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_desktop():
    return os.path.join(os.path.expanduser("~"), "Desktop")

desktop = get_desktop()

dist_path = os.path.join(desktop, 'py_gallery_dist')


def make_dist_dir(path):
    os.mkdir(path)


# def copy_template(path):
#     logger.debug("Copy index.html template to current directory")
#     shutil.copy("templates/index.html", f"{path}/index.html")


def copy_resources(path):
    logger.debug("Copy the montage and lightbox directories")
    shutil.copytree("lightbox", f"{path}/lightbox")
    shutil.copytree("montage", f"{path}/montage")


if __name__ == "__main__":
    make_dist_dir(dist_path)
    #copy_template(dist_path)
    copy_resources(dist_path)
