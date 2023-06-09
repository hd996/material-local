import re, os, sys
from .s3 import upload_to_s3
from util import randomStr

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from config import *

combine_video_name = "combine-video-" + randomStr(5) + ".mp4"


# 生成无声视频
def video_slience(video_path):
    video_slience_name = re.sub(r"(.*).mp4", r"\1-silence.mp4", video_path)
    cmd = "%s -i %s -vcodec copy -an %s -y" % (
        ffmpeg_path,
        video_path,
        video_slience_name,
    )
    os.system(cmd)
    return video_slience_name


# 生成新视频
def combine(video_path):
    video_slience_name = video_slience(video_path)
    cmd = "%s -i %s -i output.wav -c:v copy -c:a aac -strict experimental %s -y" % (
        ffmpeg_path,
        video_slience_name,
        combine_video_name,
    )
    os.system(cmd)
    # video_url = upload_to_s3(combine_video_name)
    # os.remove(combine_video_name)
    return ""


if __name__ == "__main__":
    print(combine("demo.mp4"))
