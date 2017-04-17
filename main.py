import src.copier
import src.gallery_creator as gc


def get_user_image_list():
    image_folder = input("What's the path to your image folder?")
    user_image_list = gc.get_image_list(image_folder)
    return user_image_list


def main():
    pass
