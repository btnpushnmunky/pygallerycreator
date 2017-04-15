import bs4
import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
cwd = os.path.dirname(__file__)

def get_image_list(dir_path):
    image_list = [image for image in os.listdir(dir_path)]
    logger.debug(image_list)
    return image_list

def create_html_file():
    template_path = os.path.join("templates", "index.html")
    f = open(template_path)
    soup = bs4.BeautifulSoup(f, 'html.parser')
    return soup
