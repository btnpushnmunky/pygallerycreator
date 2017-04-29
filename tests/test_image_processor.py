import src.image_processor
import tempfile
import os

def test_image_creation():
    assert False


def test_img_directory_creation():
    test_dir = tempfile.TemporaryDirectory()
    test_dir_path = os.path.join(tempfile.gettempdir(), test_dir.name)
    src.image_processor.create_img_directories(test_dir_path)
    assert os.path.isdir(os.path.join(test_dir_path, "thumbs"))
    assert os.path.isdir(os.path.join(test_dir_path, "large_imgs"))


def test_image_resize_and_save():
    assert False


def test_thumbnail_creation():
    assert False