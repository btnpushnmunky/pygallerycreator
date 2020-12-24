import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)))
import copier

def test_montage_dir_exists():
    assert os.path.isdir("vendor/montage")


def test_lightbox_dir_exists():
    assert os.path.isdir("vendor/lightbox")


def test_bootstrap_dir_exists():
    assert os.path.isdir("vendor/bootstrap-gallery")


def test_get_user_desktop():
    path = copier.get_user_desktop()
    assert path == os.path.join(os.path.expanduser("~"), "Desktop")


def test_dist_creation(tmpdir):
    temp_dir_path = tmpdir.mkdir("testing")
    print(temp_dir_path)
    copier.copy_resources_gui("vendor", temp_dir_path)
    assert os.path.isdir(temp_dir_path)
