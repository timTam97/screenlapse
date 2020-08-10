import argparse
import os

import boto3

import actions

s3 = boto3.client("s3")


def handle_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "session_key", help="The session key to download images from", type=str
    )
    return parser.parse_args()


def main():
    args = handle_args()
    try:
        os.mkdir("img")
    except FileExistsError:
        print("'img' folder already exists. Exiting...")
        exit()
    print("Gathering images to download...")
    res = s3.list_objects_v2(Bucket=actions.get_bucket_name(), Prefix=args.session_key,)
    file_list = res.get("Contents")
    while res.get("IsTruncated"):
        res = s3.list_objects_v2(
            Bucket=actions.get_bucket_name(),
            Prefix=args.session_key,
            ContinuationToken=res.get("NextContinuationToken"),
        )
        file_list.extend(res.get("Contents"))
    print("Downloading images...")
    for i in range(len(file_list)):
        print(str(i + 1) + "/" + str(len(file_list)))
        s3.download_file(
            actions.get_bucket_name(),
            file_list[i].get("Key"),
            "img\\img" + str(i) + ".png",
        )


if __name__ == "__main__":
    main()
