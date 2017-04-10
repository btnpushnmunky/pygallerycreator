import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

dist_path = os.path.join(os.path.expanduser("~"), "Desktop", "dist")

def make_dist_dir():
    os.mkdir(dist_path)

def copy_template():
    logger.debug("Copy index.html template to current directory")
    shutil.copy("templates/index.html", f"{dist_path}/index.html")

def copy_resources():
    logger.debug("Copy the montage and lightbox directories")
    shutil.copytree("lightbox", f"{dist_path}/lightbox")
    shutil.copytree("montage", f"{dist_path}/montage")


if __name__ == "__main__":
    make_dist_dir()
    copy_template()
    copy_resources()
