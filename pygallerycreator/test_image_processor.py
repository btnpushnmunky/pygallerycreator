from pygallerycreator import image_processor
import tempfile
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

CWD = os.path.dirname(__file__)
TEST_IMG_DIR = os.path.join(CWD, 'test_imgs')
TEST_DIR = tempfile.TemporaryDirectory()
TEST_DIR_PATH = os.path.join(tempfile.gettempdir(), TEST_DIR.name)


def test_img_directory_creation():
    image_processor.create_images(TEST_IMG_DIR, TEST_DIR_PATH)
    assert os.path.isdir(os.path.join(TEST_DIR_PATH, "thumbs"))
    assert os.path.isdir(os.path.join(TEST_DIR_PATH, "large_imgs"))


def test_large_file_creation():
    assert len(os.listdir(os.path.join(TEST_DIR_PATH, "large_imgs"))) == 3


def test_thumbnail_creation():
    assert len(os.listdir(os.path.join(TEST_DIR_PATH, "thumbs"))) == 3
