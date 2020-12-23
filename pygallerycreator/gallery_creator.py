import os
import jinja2
from montage_html import html as m_html
from bootstrap_html import html as b_html

def get_image_list(dir_path):
    """
    Get the image list.

    :param dir_path: Path to the directory of images
    :return:  A list of image filenames
    """
    image_list = [image for image in os.listdir(dir_path) if os.path.splitext(image)[1].lower() == ".jpg"]
    return image_list


def create_html(image_dir, kind="montage"):
    """
    Create the html for the template.

    :param image_dir: Path to the directory of images
    :return: HTML for the index.html file
    """
    if kind == "montage":
        template = jinja2.Template(m_html)
    elif kind == "bootstrap":
        template = jinja2.Template(b_html)
    else:
        print("Please specify either montage or bootstrap for kind of gallery.")
        template = None
    # template = template_env.get_template(TEMPLATE_FILE)
    images = get_image_list(image_dir)
    return template.render(images=images)
