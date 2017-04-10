import os
import tempfile

def test_index_template_exists():
    assert os.path.isfile("./templates/index.html")

def test_montage_dir_exists():
    assert os.path.isdir("./montage")

def test_lightbox_dir_exists():
    assert os.path.isdir("./lightbox")

def test_dist_creation():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    dist_dir = os.mkdir(os.path.expanduser("~") + "/Desktop/dist")
    assert os.path.isdir(os.path.expanduser("~") + "/Desktop/dist")
