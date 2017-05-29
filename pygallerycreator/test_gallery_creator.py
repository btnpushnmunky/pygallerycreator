from pygallerycreator import gallery_creator
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

test_file_dir = os.path.dirname(__file__)
TEST_IMG_DIR = os.path.join(test_file_dir, "test_imgs")


def test_create_image_list():
    image_list = gallery_creator.get_image_list(TEST_IMG_DIR)
    logger.debug(f"Test list is {image_list}")
    assert len(image_list) == 3


def test_create_html():
    html = gallery_creator.create_html(TEST_IMG_DIR)
    html_length = len(html)
    logger.debug(f"HTML length {html_length}")
    assert "<!DOCTYPE html>" in html
