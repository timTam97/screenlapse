import argparse
import os
import subprocess
import time

import PIL.ImageGrab
import boto3

import actions
import constants


def push_img():
    s3 = boto3.client("s3")
    s3.upload_file(
        constants.TEMP_IMG_NAME,
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
    parser.add_argument(
        "-m", "--multi", help="Take multi-monitor screenshots", action="store_true"
    )
    args = parser.parse_args()
    if args.time is None:
        args.time = 3
    if args.time <= 0:
        raise argparse.ArgumentTypeError("Time must be positive")
    return args


def update_strings(offline: bool, counter: int) -> tuple:
    if offline:
        save_string = "img/img{}.png".format(str(counter))
        print_string = "Image {} captured. Running in offline mode. [ctrl+c to quit]".format(
            str(counter)
        )
    else:
        save_string = constants.TEMP_IMG_NAME
        print_string = "Image {} captured and pushed. [ctrl+c to quit]".format(
            str(counter)
        )
    return save_string, print_string


def main():
    args = handle_args()
    sleep_time = args.time
    offline = args.offline
    actions.set_session_key()
    i = 1
    if offline:
        try:
            os.mkdir("img")
        except FileExistsError:
            print("img directory already exists. Exiting...")
            exit()
    try:
        while True:
            save_string, print_string = update_strings(offline, i)
            PIL.ImageGrab.grab(all_screens=args.multi).save(save_string)
            if not offline:
                push_img()
            subprocess.run(["cls"], shell=True)
            print(print_string)
            time.sleep(sleep_time)
            i += 1
    except KeyboardInterrupt:
        print("Closing down...")
        exit()


if __name__ == "__main__":
    main()
