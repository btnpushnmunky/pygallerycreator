from pygallerycreator import main
from pygallerycreator.copier import default_dist_path


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
    monkeypatch.setitem(__builtins__, "input", lambda x: "test_imgs_output")
    main.create_image_gallery("test_imgs")


def teardown_method():
    """Reset input."""
    main.input = input
