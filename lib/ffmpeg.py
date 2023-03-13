import re, os, sys
from .s3 import upload_to_s3

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from config import audio_name
from util import randomStr

combine_video_name = "combine-video-" + randomStr(5) + ".mp4"


def video_slience(video_path):
    video_slience_name = re.sub(r"(.*).mp4", r"\1-silence.mp4", video_path)
    cmd = "ffmpeg -i %s -vcodec copy -an %s -y" % (
        video_path,
        video_slience_name,
    )
    os.system(cmd)
    return video_slience_name


def combine(video_path):
    video_slience_name = video_slience(video_path)
    cmd = "ffmpeg -i %s -i %s -c:v copy -c:a aac -strict experimental %s -y" % (
        video_slience_name,
        audio_name,
        combine_video_name,
    )
    os.system(cmd)
    # video_url = upload_to_s3(combine_video_name)
    # os.remove(combine_video_name)
    return ""


if __name__ == "__main__":
    print(combine("demo.mp4"))
