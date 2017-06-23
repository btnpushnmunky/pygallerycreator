import os
# from jinja2 import Environment, FileSystemLoader
import jinja2
from my_html import my_html
# JINJA_ENV = Environment(loader=FileSystemLoader("templates"))


def get_image_list(dir_path):
    """
    Get the image list.

    :param dir_path: Path to the directory of images
    :return:  A list of image filenames
    """
    image_list = [image for image in os.listdir(dir_path)]
    return image_list


def create_html(image_dir):
    """
    Create the html for the template.

    :param image_dir: Path to the directory of images
    :return: HTML for the index.html file
    """
    template = jinja2.Template(my_html)
    # template = template_env.get_template(TEMPLATE_FILE)
    images = get_image_list(image_dir)
    return template.render(images=images)
