# material-local
🎬 素材本地化

## 📖 前言
在视频素材制作的时候，一般只会做一个语言版本，但在很多场景下（例如广告投放多国家/多语种时），我们需要做不同语言版本的视频，我们只需要以下几个步骤就可以轻松地去完成这件事
1. 将原视频生成无声视频
2. 根据文案生成语音
3. 将语音和无声视频合成新视频

有几个需要注意的点：
1. 🔊 语音效果
  - 语速（需模型支持）
  - 男女声（需模型支持）
  - 感情（需模型支持）
2. 🎬 视频效果
  - 语音和视频时长匹配（手动调整，或技术裁剪）
  - 语音和视频内容对应（手动调整，难度极高）

❗️郑重声明: 本人从事前端开发，对NLP了解并不多，这个项目更多的是探索解决方案，有任何问题请提[ISSUE](https://github.com/hd996/material-local/issues)，大家共同学习😄


## 🚀 启动
在启动之前需要安装必须的环境
- [ffmpeg](https://ffmpeg.org/download.html)
- [python3](https://www.python.org/downloads)

目前支持多语言的tts模型比较少，大部分模型都只针对单一语言训练，我使用的是`coqui-ai/TTS`，好处是切换语言模型比较方便，之前也尝试过[Huggingface](https://huggingface.co/)上的模型，效果也是一样的

```zsh
pip install TTS # 安装coqui-ai/TTS
python main.py -h # 获取帮助
python main.py -cc {contry_code} -t {text} -vp {video_path} # 原视频 + 文案 => 合成视频

# 举个🌰
python main.py -cc zh -t "这个是一个很棒的游戏，我非常喜欢玩" -vp demo.mp4 # 中文
python main.py -cc en -t "This is a great game, I like playing very much" -vp demo.mp4 # 英文
python main.py -cc fr -t "C’est un grand jeu, j’aime jouer beaucoup" -vp demo.mp4 # 法语

# 生成视频上传s3
# copy config.py.example => config.py，代码在lib/s3.py
```

## 👩‍💻 Q & A
- Q: 当前存在问题？
- A: 「前言」提到的「语速/男女声/情感/匹配度」等问题，需要自己去尝试合适的模型，另外对于长文本，支持地都很差

- Q: 为什么不用云？
- A: 在云上没找到现成的方案，没有用云的tts是因为没💰，云基本都是支持「语速/男女声/长文本」等问题

## 🔗 链接
- [coqui-ai/TTS](https://github.com/coqui-ai/TTS)
- [FFmpeg](https://ffmpeg.org)
- [tts-tacotron2-ljspeech](https://huggingface.co/speechbrain/tts-tacotron2-ljspeech)