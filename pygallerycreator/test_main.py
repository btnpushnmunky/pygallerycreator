from pygallerycreator import main
from pygallerycreator.copier import default_dist_path


def test_get_user_path(monkeypatch):
    monkeypatch.setitem(__builtins__, "input", lambda x: "user dest dir")
    user_path = main.get_user_path()
    assert "user dest dir" in user_path


def test_get_user_path_no_input(monkeypatch):
    monkeypatch.setitem(__builtins__, "input", lambda x: "")
    user_path = main.get_user_path()
    assert user_path == default_dist_path


def teardown_method():
    main.input = input
