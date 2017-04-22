import src.copier import default_dist_path
import src.gallery_creator as gc
import os


def create_image_gallery(path=None):
    if path is None:
        path = default_dist_path
    else:
        pass
    image_dir = input("Please enter the path to your image directory")
    html = gc.create_html(image_dir)
    src.copier.make_dist_dir(path)
    src.copier.copy_resources(path)
    with open(os.path.join(path, "index.html"), "w+") as f:
        f.write(html)


if __name__ == "__main__":
    create_image_gallery()
