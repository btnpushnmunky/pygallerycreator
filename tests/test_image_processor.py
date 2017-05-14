import src.image_processor
import tempfile
import os

CWD = os.path.dirname(__file__)
TEST_IMG_DIR = os.path.join(CWD, 'test_imgs')
TEST_DIR = tempfile.TemporaryDirectory()
TEST_DIR_PATH = os.path.join(tempfile.gettempdir(), TEST_DIR.name)


# def test_image_creation():
    # src.image_processor.create_images(TEST_IMG_DIR, TEST_DIR_PATH)


def test_img_directory_creation():
    src.image_processor.create_images(TEST_IMG_DIR, TEST_DIR_PATH)
    assert os.path.isdir(os.path.join(TEST_DIR_PATH, "thumbs"))
    print(os.listdir(os.path.join(TEST_DIR_PATH, "thumbs")))
    assert os.path.isdir(os.path.join(TEST_DIR_PATH, "large_imgs"))


def test_image_resize_and_save():
    assert False


def test_thumbnail_creation():
    assert False
