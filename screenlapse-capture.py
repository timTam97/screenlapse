import argparse
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
    actions.set_session_key()
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
