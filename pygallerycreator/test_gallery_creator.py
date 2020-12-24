import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
import gallery_creator
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

test_file_dir = os.path.dirname(__file__)
TEST_IMG_DIR = os.path.join(test_file_dir, "test_imgs")


def test_create_image_list():
    """Test creating the image list."""
    image_list = gallery_creator.get_image_list(TEST_IMG_DIR)
    logger.debug("Test list is {0}".format(image_list))
    assert len(image_list) == 6


def test_create_html():
    """Test creating the gallery."""
    html = gallery_creator.create_html(TEST_IMG_DIR)
    html_length = len(html)
    logger.debug("HTML length {0}".format(html_length))
    assert "<!DOCTYPE html>" in html
