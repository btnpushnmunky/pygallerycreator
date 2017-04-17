import main


def test_get_user_image_list():
    main.input = lambda x: 'tests/test_imgs'
    test_dir = main.get_user_image_list()
    assert type(test_dir) is list
