import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
import main
from copier import default_dist_path
import tempfile
import os


def test_get_user_path(monkeypatch):
    """Make sure getting the user's path works."""
    monkeypatch.setitem(__builtins__, "input", lambda x: "user dest dir")
    user_path = main.get_user_path()
    assert "user dest dir" in user_path


def test_get_user_path_no_input(monkeypatch):
    """Make sure the default path is used if no input for destination dir."""
    monkeypatch.setitem(__builtins__, "input", lambda x: "")
    user_path = main.get_user_path()
    assert user_path == default_dist_path


def test_get_raw_images(monkeypatch):
    """Make sure we have a path to raw images."""
    monkeypatch.setitem(__builtins__, "input", lambda x: "test_imgs")
    raw_images = main.get_raw_image_dir()
    assert "test_imgs" in raw_images


def test_create_gallery(monkeypatch):
    """Test creation of the gallery."""
    tdir = tempfile.TemporaryDirectory()
    my_temp_dir = os.path.join(tdir.name, 'test_imgs_output')
    monkeypatch.setitem(__builtins__, "input", lambda x: my_temp_dir)
    main.create_image_gallery("test_imgs", my_temp_dir, "bootstrap")


def teardown_method():
    """Reset input."""
    main.input = input
