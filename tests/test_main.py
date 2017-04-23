import main
from src.copier import default_dist_path


def test_get_user_path(monkeypatch):
    monkeypatch.setitem(__builtins__, "input", lambda x: "user dest dir")
    user_path = main.get_user_path()
    assert user_path == "user dest dir"


def test_get_user_path_no_input(monkeypatch):
    monkeypatch.setitem(__builtins__, "input", lambda x: None)
    user_path = main.get_user_path()
    assert user_path == default_dist_path


def teardown_method():
    main.input = input
