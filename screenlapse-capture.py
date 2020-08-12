import argparse
import os
import subprocess
import time

import boto3
import pyautogui

import actions
import constants


def push_img():
    s3 = boto3.client("s3")
    s3.upload_file(
        constants.IMG_NAME,
        actions.get_bucket_name(),
        actions.get_session_key() + "/" + str(int(time.time())) + ".png",
    )


def handle_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--time",
        help="number of seconds between screenshots. default is 5",
        type=int,
        metavar="secs",
    )
    parser.add_argument(
        "-o",
        "--offline",
        help="Use filesystem for image storage instead of S3",
        action="store_true",
    )
    args = parser.parse_args()
    if args.time is None:
        args.time = 3
    if args.time <= 0:
        raise argparse.ArgumentTypeError("Time must be positive")
    return args


def main():
    args = handle_args()
    sleep_time = args.time
    offline = args.offline
    actions.set_session_key()
    if offline:
        try:
            os.mkdir("img")
        except FileExistsError:
            print("img directory already exists. Exiting...")
            exit()
    i = 1
    try:
        while True:
            if not offline:
                pyautogui.screenshot(constants.IMG_NAME)
                push_img()
                subprocess.run(["cls"], shell=True)
                print("Image " + str(i) + " captured and pushed. [ctrl+c to quit]")
            else:
                pyautogui.screenshot("img/img" + str(i) + ".png")
                subprocess.run(["cls"], shell=True)
                print(
                    "Image "
                    + str(i)
                    + " captured. Running in offline mode. [ctrl+c to quit]"
                )
            i += 1
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Closing down...")
        exit()


if __name__ == "__main__":
    main()
