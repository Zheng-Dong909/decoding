from pocketsphinx import AudioFile

# # 读取音频文件并进行语音识别
# audio_file = "./test.wav"

# for phrase in AudioFile(audio_file):
#     print(phrase)

import speech_recognition as sr

# 创建语音识别器对象
r = sr.Recognizer()

# 读取语音文件
audio_file = "./test.wav"
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)  # 从语音文件中读取音频数据

try:
    # 进行语音识别
    text = r.recognize_google(audio, language="en-US")  # 使用 Google 语音识别 API，指定语言为英文
    print("转换结果：", text)
except sr.UnknownValueError:
    print("无法识别语音")
except sr.RequestError as e:
    print(f"请求错误：{e}")