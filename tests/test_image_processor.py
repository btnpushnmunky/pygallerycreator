import src.image_processor
import tempfile
import os

def test_image_creation():
    assert False


def test_thumb_dir_creation():
    test_dir = tempfile.TemporaryDirectory()
    test_dir_path = os.path.join(tempfile.gettempdir(), test_dir.name)
    src.image_processor.create_thumb_dir(test_dir_path)
    assert os.path.isdir(os.path.join(test_dir_path, "thumbs"))


def test_resized_img_dir_creation():
    assert False


def test_image_resize_and_save():
    assert False


def test_thumbnail_creation():
    assert False