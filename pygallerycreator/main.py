import copier
import gallery_creator
import image_processor
import os


def get_user_path():
    """
    Get the user's destination directory for the gallery folder.
    :return: User image directory path as a string.
    """
    gallery_dist_name = input("Please enter a name for your gallery directory: [py_gallery_dist] ")
    if gallery_dist_name is "":
        gallery_dist_name = copier.default_dist_path
    else:
        gallery_dist_name = os.path.join(copier.get_desktop(), gallery_dist_name)
    return gallery_dist_name


def create_image_gallery():
    """
    Create all the elements of the gallery
    """
    user_directory_path = get_user_path()
    image_dir = input("Please enter the path to your image directory: ")
    html = gallery_creator.create_html(image_dir)
    copier.make_dist_dir(user_directory_path)
    copier.copy_resources(user_directory_path)
    image_processor.create_images(image_dir, user_directory_path)

    with open(os.path.join(user_directory_path, "index.html"), "w+") as f:
        f.write(html)


if __name__ == "__main__":
    create_image_gallery()
