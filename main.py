import argparse
from lib import tts, ffmpeg

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--country-code", "-cc", help="国家代码(支持列表: zh | en | pt | fr)", required=True
    )
    parser.add_argument("--text", "-t", help="文案", required=True)
    parser.add_argument("--video-path", "-vp", help="视频地址", required=True)
    args = parser.parse_args()

    tts.gen(getattr(args, "country_code"), args.text)
    video_url = ffmpeg.combine(
        getattr(args, "video_path"),
    )
    print(video_url)
