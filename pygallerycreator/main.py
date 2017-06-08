import copier
import gallery_creator
import image_processor
import os


def get_user_path():
    """
    Get the user's destination directory for the gallery folder.

    :return: User image directory path as a string.
    """
    dir_name_input = """
    Please enter a name for your gallery directory: [py_gallery_dist]
    """
    gallery_dir_name = input(dir_name_input)
    if gallery_dir_name is "":
        gallery_dir_name = copier.default_dist_path
    else:
        user_def_path = os.path.join(copier.get_user_home(), gallery_dir_name)
        gallery_dir_name = os.path.join(user_def_path)
    return gallery_dir_name


def get_raw_image_dir():
    """Get the user's image director."""
    d = input("Please enter the path to your image directory: ")
    return d


def create_image_gallery(raw_images):
    """Create all the elements of the gallery."""
    user_directory_path = get_user_path()
    html = gallery_creator.create_html(raw_images)
    copier.make_dist_dir(user_directory_path)
    copier.copy_resources(user_directory_path)
    image_processor.create_images(raw_images, user_directory_path)

    with open(os.path.join(user_directory_path, "index.html"), "w+") as f:
        f.write(html)


if __name__ == "__main__":
    user_dir = get_raw_image_dir()
    create_image_gallery()
