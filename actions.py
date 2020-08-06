import time

import boto3

import constants


def push_img():
    s3 = boto3.client("s3")
    with open(constants.BUCKET_NAME_FILE_NAME, "r") as f:
        s3.upload_file(
            constants.IMG_NAME,
            f.read(),
            get_session_key() + "/" + str(int(time.time())) + ".png",
        )


def set_session_key():
    """ Used to organise folders in S3.
    Should make life easier when it comes to pulling the images and creating the video. """
    with open(constants.SESSION_ID_FILE_NAME, "w") as f:
        f.write(str(int(time.time())))


def get_session_key():
    with open(constants.SESSION_ID_FILE_NAME, "r") as f:
        return f.read()


if __name__ == "__main__":
    set_session_key()
    # print(get_session_key())
    push_img()
    # print(get_session_key() + "/" + str(int(time.time())) + ".png")
    # print(time.time())
