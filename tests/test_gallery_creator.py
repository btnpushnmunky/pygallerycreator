import gallery_creator
import os

def test_create_image_list():
    dir = os.path.dirname(__file__)
    test_img_path = os.path.join(dir, "test_imgs")
    image_list = gallery_creator.get_image_list(test_img_path)
    assert len(image_list) == 3


def test_found_template():
    template = None
    assert template


def test_got_image_dir():
    dir = None
    assert dir
