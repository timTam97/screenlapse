import time

import boto3

import constants


def get_bucket_name() -> str:
    with open(constants.BUCKET_NAME_FILE_NAME) as f:
        return f.read()


def set_session_key():
    """ Used to organise folders in S3.
    Should make life easier when it comes to pulling the images and creating the video.
    Folder names take the form of a unix timestamp representing the time the screen capture session
    started."""
    with open(constants.SESSION_ID_FILE_NAME, "w") as f:
        f.write(str(int(time.time())))


def get_session_key() -> str:
    with open(constants.SESSION_ID_FILE_NAME, "r") as f:
        return f.read()


if __name__ == "__main__":
    set_session_key()
    # print(get_session_key())
    push_img()
    # print(get_session_key() + "/" + str(int(time.time())) + ".png")
    # print(time.time())
