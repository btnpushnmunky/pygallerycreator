import os
from . import copier


def test_index_template_exists():
    assert os.path.isfile("templates/index.html")


def test_montage_dir_exists():
    assert os.path.isdir("vendor/montage")


def test_lightbox_dir_exists():
    assert os.path.isdir("vendor/lightbox")


def test_get_desktop():
    d = copier.get_desktop()
    assert "Desktop" in d


def test_dist_creation(tmpdir):
    temp_dir_path = tmpdir.mkdir("testing")
    print(temp_dir_path)
    copier.copy_resources(temp_dir_path)
    assert os.path.isdir(temp_dir_path)
