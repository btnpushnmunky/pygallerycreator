import src.copier
import src.gallery_creator as gc
import os
import src.image_processor


def get_user_path():
    """
    Get the user's destination directory for the gallery folder
    """
    user_path = input("Please enter a destination directory for the gallery. [Desktop] ")
    if user_path is "":
        user_path = src.copier.default_dist_path
    else:
        pass
    return user_path


def create_image_gallery():
    """
    Create the gallery directory and it's contents
    """
    user_path = get_user_path()
    image_dir = input("Please enter the path to your image directory")
    html = gc.create_html(image_dir)
    src.copier.make_dist_dir(user_path)
    src.copier.copy_resources(user_path)
    src.image_processor.create_images(image_dir, user_path)
    with open(os.path.join(user_path, "index.html"), "w+") as f:
        f.write(html)


if __name__ == "__main__":
    create_image_gallery()
