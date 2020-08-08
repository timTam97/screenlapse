import random
import string

import boto3

# noinspection PyUnresolvedReferences
s3 = boto3.client("s3")


def random_key(length: int) -> str:
    key = []
    for i in range(length):
        key.append(random.choice(string.ascii_lowercase + string.digits))
    return "".join(key)


def main():
    bucket_name = "screenshot-storage-" + random_key(25)
    with open("bucket", "w") as f:
        f.write(bucket_name)
    s3.create_bucket(
        ACL="private",
        Bucket=bucket_name,
        CreateBucketConfiguration={"LocationConstraint": "ap-southeast-2"},
    )


if __name__ == "__main__":
    main()
