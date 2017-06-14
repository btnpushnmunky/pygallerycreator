import copier
import gallery_creator
import image_processor
import os
import gui
from PyQt5 import QtWidgets
import sys


def get_user_path():
    """
    Get the user's destination directory for the gallery folder.

    :return: User image directory path as a string.
    """
    dir_name_input = "Gallery path. Created in home directory. (ex: Desktop/mygallery): [py_gallery_dist]"
    gallery_dir_name = input(dir_name_input)
    if gallery_dir_name is "":
        gallery_dir_name = copier.default_dist_path
    else:
        user_def_path = os.path.join(copier.get_user_home(), gallery_dir_name)
        gallery_dir_name = os.path.join(user_def_path)
    return gallery_dir_name


def get_raw_image_dir():
    """Get the user's image director."""
    d = input("Please enter the path to your image directory: ")
    return d


def get_directories():
    """Get directories."""
    raw_directory = get_raw_image_dir()
    new_gallery_dir = get_user_path()
    return raw_directory, new_gallery_dir


def create_image_gallery(raw_images, new_gallery_path):
    """Create all the elements of the gallery."""
    html = gallery_creator.create_html(raw_images)
    copier.make_dist_dir(new_gallery_path)
    copier.copy_resources(new_gallery_path)
    image_processor.create_images(raw_images, new_gallery_path)

    with open(os.path.join(new_gallery_path, "index.html"), "w+") as f:
        f.write(html)


class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    """Class for our app."""

    def __init__(self, parent=None):
        """Init the class."""
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.source_button.clicked.connect(self.get_source)
        self.destination_button.clicked.connect(self.set_destination)

    def get_source(self):
        """Get the source directory."""
        print("Get source")

    def set_destination(self):
        """Get the destination directory."""
        print("Set destination")


def main():
    """Main function to launch the app."""
    app = QtWidgets.QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
