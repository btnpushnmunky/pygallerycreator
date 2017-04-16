import os
from jinja2 import Environment, FileSystemLoader


JINJA_ENV = Environment(loader=FileSystemLoader("templates"))

def get_image_list(dir_path):
    image_list = [image for image in os.listdir(dir_path)]
    return image_list

def create_html(image_dir):
    template = JINJA_ENV.get_template("index.html")
    images = get_image_list("tests/test_imgs")
    return template.render(images=images)
