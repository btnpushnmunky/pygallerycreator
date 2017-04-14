import bs4
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_image_list(dir_path):
    image_list = [image for image in os.listdir(dir_path)]
    logger.debug(image_list)
    return image_list