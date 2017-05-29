import os
import tempfile
from . import copier


def test_index_template_exists():
    assert os.path.isfile("templates/index.html")


def test_montage_dir_exists():
    assert os.path.isdir("vendor/montage")


def test_lightbox_dir_exists():
    assert os.path.isdir("vendor/lightbox")


def test_dist_creation():
    d = copier.get_desktop()
    temp_dir = tempfile.TemporaryDirectory(dir=d)
    temp_dir_path = os.path.join(d, temp_dir.name)
    copier.copy_resources(temp_dir_path)
    assert os.path.isdir(temp_dir_path)
