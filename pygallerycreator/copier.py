import os
import logging
import shutil

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
base_dir = os.path.dirname((os.path.realpath(__file__)))


def get_user_home():
    """
    Find the user's desktop folder.

    :return: Path to user's desktop as a string
    """
    return os.path.expanduser("~")

home = get_user_home()

default_dist_path = os.path.join(home, 'py_gallery_dist')


def make_dist_dir(path):
    """
    Create the distribution directory and it's subdirectories.

    :param path: Path to the distribution directory
    :return: None
    """
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print("The specified destination already exists.")


def copy_resources(path):
    """
    Copy the javascript directories and their contents to the dist directory.

    :param path: Path to the distribution directory
    :return: None
    """
    shutil.copytree("vendor/lightbox", "{0}/lightbox".format(path))
    shutil.copytree("vendor/montage", "{0}/montage".format(path))
