import os
import time

import constants


def get_bucket_name() -> str:
    with open("data/" + constants.BUCKET_NAME_FILE_NAME) as f:
        return f.read()


def create_data_dir() -> bool:
    try:
        os.mkdir("data")
        return True
    except FileExistsError:
        return False


def set_session_key():
    """ Used to organise folders in S3.
    Should make life easier when it comes to pulling the images and creating the video.
    Folder names take the form of a unix timestamp representing the time the screen capture session
    started.
    Make sure you've called create_data_dir before you call this pls"""

    with open("data/" + constants.SESSION_ID_FILE_NAME, "w") as f:
        f.write(str(int(time.time())))


def get_session_key() -> str:
    """Make sure you've called `create_data_dir()` before you call this pls"""
    with open("data/" + constants.SESSION_ID_FILE_NAME, "r") as f:
        return f.read()


if __name__ == "__main__":
    set_session_key()
    # print(get_session_key())
    push_img()
    # print(get_session_key() + "/" + str(int(time.time())) + ".png")
    # print(time.time())
