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


def copy_resources_gui(temp_path, dest_path):
    """
    Copy the javascript directories and their contents to the dist directory.
    This function must be used for the GUI version.

    :param temp_path: Path to the distribution directory
    :param dest_path: Path to the destination directory
    :return: None
    """
    shutil.copytree("{0}/lightbox".format(temp_path), "{0}/lightbox".format(dest_path))
    shutil.copytree("{0}/montage".format(temp_path), "{0}/montage".format(dest_path))
    shutil.copytree("{0}/bootstrap-gallery".format(temp_path), "{0}/bootstrap-gallery".format(dest_path))

