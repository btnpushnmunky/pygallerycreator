import src.copier
import src.gallery_creator as gc
import os


def create_image_gallery():
    image_dir = input("Please enter the path to your image directory")
    html = gc.create_html(image_dir)
    src.copier.make_dist_dir(src.copier.dist_path)
    src.copier.copy_resources(src.copier.dist_path)
    with open(os.path.join(src.copier.dist_path, "index.html"), "w+") as index_file:
        index_file.write(html)

if __name__ == "__main__":
    create_image_gallery()
