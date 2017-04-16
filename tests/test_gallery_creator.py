from src import gallery_creator
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
dir = os.path.dirname(__file__)
test_img_path = os.path.join(dir, "test_imgs")

def test_create_image_list():
    image_list = gallery_creator.get_image_list(test_img_path)
    logger.debug(image_list)
    assert len(image_list) == 3

def test_got_image_dir():
    dir = None
    assert dir

def test_create_template():
    template = gallery_creator.create_html(test_img_path)
    logger.debug(template)
    assert "<!DOCTYPE html>" in template