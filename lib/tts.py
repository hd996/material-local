import os, sys
from TTS.api import TTS

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from config import audio_name

languages = {
    "zh": {
        "model_name": "tts_models/zh-CN/baker/tacotron2-DDC-GST",
        "speakers": {"male": "", "female": ""},
    },
    "en": {
        "model_name": "tts_models/en/ek1/tacotron2",
        "speakers": {"male": "", "female": ""},
    },
    "fr": {
        "model_name": "tts_models/fr/css10/vits",
        "speakers": {"male": "", "female": ""},
    },
    "pt": {
        "model_name": "tts_models/pt/cv/vits",
        "speakers": {"male": "", "female": ""},
    },
}


def gen(country_code, text):
    tts = TTS(languages[country_code]["model_name"])
    tts.tts_to_file(
        text=text,
        file_path=audio_name,
    )


if __name__ == "__main__":
    tts_pt = TTS(languages["pt"]["model_name"])
    print("tts.speakers:", tts_pt.speakers)
    print("tts.languages:", tts_pt.languages)
    tts_pt.tts_to_file(
        text="Olá, mundo",
        file_path="output-pt.wav",
    )
