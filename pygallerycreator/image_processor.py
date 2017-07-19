from PIL import Image
import os

THUMB_SIZE = (256, 256)
LARGE_SIZE = (1024, 1024)


def create_images(user_images_dir, base_save_path):
    """
    Open the original image files and save a thumb and gallery version.

    :param user_images_dir: User's image directory path as a string
    :param base_save_path: The parent directory that will hold image dirs
    :return: None
    """
    thumb_dir = os.path.join(base_save_path, "thumbs")
    overlay_image_dir = os.path.join(base_save_path, "large_imgs")
    os.mkdir(thumb_dir)
    os.mkdir(overlay_image_dir)

    def base_filename(filename):
        """
        Process the filename so it preserves periods.

        :param filename: Filename as a string
        :return: Base image name without extension
        """
        split_filename = filename.rsplit(".")
        fn_length = len(split_filename)
        if fn_length > 2:
            basename = ".".join(split_filename[:-1])
        else:
            basename = split_filename[0]
        return basename

    def open_image(img_filename):
        """
        Open an image file and return it and its name.

        :param img_filename: Filename of image as a string
        :return: Image with name including extension
        """
        final_img_name = base_filename(img_filename)
        # final_img_name = img_filename.rsplit('.')[0]
        outfile = ".".join((final_img_name, "jpg"))
        img = Image.open(os.path.join(user_images_dir, img_filename))
        return img, outfile

    def create_image_versions(original_image):
        """
        Create the thumbnail and large image for an image file.

        :param original_image: Filename as string
        :return: None
        """
        if os.path.splitext(original_image)[1].lower() == '.jpg':
            img, img_name = open_image(original_image)
            img.thumbnail(THUMB_SIZE)
            thumb_file = os.path.join(thumb_dir, img_name)
            img.save(thumb_file)
            large_img, large_img_name = open_image(original_image)
            large_img.thumbnail(LARGE_SIZE)
            large_file = os.path.join(overlay_image_dir, large_img_name)
            large_img.save(large_file)
        else:
            pass

    for file_name in os.listdir(user_images_dir):
        create_image_versions(file_name)
