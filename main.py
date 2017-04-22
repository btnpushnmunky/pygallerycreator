import src.copier
import src.gallery_creator as gc
import os


def get_user_path():
    user_path = input("Please enter a destination directory for the gallery. Default is Desktop")
    if user_path is None:
        user_path = src.copier.default_dist_path
    else:
        pass
    return user_path


def create_image_gallery():
    path = get_user_path()
    image_dir = input("Please enter the path to your image directory")
    html = gc.create_html(image_dir)
    src.copier.make_dist_dir(path)
    src.copier.copy_resources(path)
    with open(os.path.join(path, "index.html"), "w+") as f:
        f.write(html)


if __name__ == "__main__":
    create_image_gallery()
