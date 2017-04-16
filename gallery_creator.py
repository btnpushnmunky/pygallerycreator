import bs4
import os
import logging
from jinja2 import Environment, FileSystemLoader


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_image_list(dir_path):
    image_list = [image for image in os.listdir(dir_path)]
    logger.debug(image_list)
    return image_list

def create_html_file():
    soup = "<!DOCTYPE html>"
    return soup
