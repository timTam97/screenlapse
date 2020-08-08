import argparse
import subprocess
import time

import boto3
import pyautogui

import constants


def push_img():
    s3 = boto3.client("s3")
    s3.upload_file(
        constants.IMG_NAME,
        get_bucket_name(),
        get_session_key() + "/" + str(int(time.time())) + ".png",
    )


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--time",
        help="number of seconds between screenshots. default is 5",
        type=int,
        metavar="secs",
    )
    args = parser.parse_args()
    if args.time is None:
        args.time = 5
    if args.time <= 0:
        raise argparse.ArgumentTypeError("Time must be positive")
    set_session_key()
    i = 1
    while True:
        # grab screenshot
        # push to aws
        # wait 5 secs
        pyautogui.screenshot(constants.IMG_NAME)
        push_img()
        subprocess.run(["cls"], shell=True)
        print("Image " + str(i) + " captured and pushed. [ctrl+c to quit]")
        i += 1
        time.sleep(args.time)


if __name__ == "__main__":
    main()
