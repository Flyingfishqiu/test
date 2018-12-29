import os
from driver.driver import mydriver


def save_image(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__)).split('test_case')[0]+'report/image/'
    driver.get_screenshot_as_file(base_dir+file_name)


if __name__ == '__main__':
    save_image('hh.png')