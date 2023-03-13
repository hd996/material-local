import boto3
import re, os, sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from config import *


def upload_to_s3(file_name):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region,
    )
    s3.upload_file(
        file_name,
        bucket_name,
        bucket_path + file_name,
        ExtraArgs={"ContentType": "video/mp4"},
    )
    return host + bucket_path + file_name


if __name__ == "__main__":
    upload_to_s3("demo.mp4")
