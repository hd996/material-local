import re, os, sys


# 视频裁剪
def cut_video(video_path, start_second, end_second):
    cmd = "ffmpeg -ss %s -t %s -i %s -vcodec copy -acodec copy demo-cut.mp4 -y" % (
        start_second,
        end_second,
        video_path,
    )
    os.system(cmd)


if __name__ == "__main__":
    cut_video("demo.mp4", "00:00:00", "00:00:05")
