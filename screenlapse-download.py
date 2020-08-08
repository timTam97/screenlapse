import argparse
import subprocess

import boto3

s3 = boto3.client("s3")


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "session_key", help="The session key to download images from", type=str
    )
    return parser.parse_args()


def main():
    args = handle_args()
    # TODO figure out how to implement pagination (>1000 images)
    res = s3.list_objects_v2(Bucket=actions.get_bucket_name(), Prefix=args.session_key,)
    subprocess.run(["mkdir img"], shell=True)
    file_list = res.get("Contents")
    i = 1
    print("Downloading images...")
    for obj in file_list:
        print(str(i) + "/" + str(len(file_list)))
        s3.download_file(
            actions.get_bucket_name(), obj.get("Key"), "img\\img" + str(i) + ".png"
        )
        i += 1


if __name__ == "__main__":
    main()
