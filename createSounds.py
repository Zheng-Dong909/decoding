import pyttsx3

# 创建 Text-to-Speech 引擎
engine = pyttsx3.init()

# 设置语音参数（可选）
engine.setProperty('voice', 'en-us')  # 设置语音为美式英语
engine.setProperty('rate', 100)  # 设置语速为 150 字/分钟

# 要转换的文本
text = "Hi. How are you?"
# text = "你好"
# 将文本转换为音频
output_file = "./output.wav"
engine.save_to_file(text, output_file)
engine.runAndWait()