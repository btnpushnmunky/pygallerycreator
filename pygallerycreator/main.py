import os
import sys
import copier
import image_processor
import gallery_creator


def get_user_path():
    """
    Get the user's destination directory for the gallery folder.

    :return: New gallery directory path as a string.
    """

    dir_name_input = "Gallery path. Created in home directory. (ex: Desktop/mygallery): [py_gallery_dist]"
    gallery_dir_name = input(dir_name_input)
    if gallery_dir_name is "":
        gallery_dir_name = copier.default_dist_path
    else:
        user_def_path = os.path.join(copier.get_user_home(), gallery_dir_name)
        gallery_dir_name = os.path.join(user_def_path)
    return gallery_dir_name

def get_raw_image_dir():
    """
    Get the user's image directory.

    :return: User's raw image directory as a string.
    """

    d = input("Please enter the path to your image directory: ")
    return d

def get_directories():
    """Get directories."""

    raw_directory = get_raw_image_dir()
    new_gallery_dir = get_user_path()
    return raw_directory, new_gallery_dir

def create_image_gallery(raw_images, new_gallery_path, type=""):

    """Create all the elements of the gallery."""

    copier.make_dist_dir(new_gallery_path)
    print(type)
    if type == "gui":
        copier.copy_resources_gui(sys._MEIPASS, new_gallery_path)
    else:
        copier.copy_resources_gui("vendor", new_gallery_path)
    image_processor.create_images(raw_images, new_gallery_path)
    filename_directory = os.path.join(new_gallery_path, "large_imgs")
    html = gallery_creator.create_html(filename_directory)
    with open(os.path.join(new_gallery_path, "index.html"), "w+") as f:
        f.write(html)


if __name__ == "__main__":
    user_dir, new_gallery = get_directories()
    create_image_gallery(user_dir, new_gallery)
