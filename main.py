import re
import base64

with open('audio_sample.txt', 'rb') as f:
    file_contents = f.read()

# 使用分隔符提取音频数据
start_str = b"------WebKitFormBoundaryrEoIr8CLEX9elrhJ\r\nContent-Disposition: form-data; name=\"source\"; filename=\"blob\"\r\nContent-Type: audio/ogg; codecs=opus\r\n\r\n"
end_str = b"\r\n------WebKitFormBoundaryrEoIr8CLEX9elrhJ--\r\n"
start_idx = file_contents.find(start_str) + len(start_str)
end_idx = file_contents.find(end_str)

audio_data = file_contents[start_idx:end_idx]

# 解码 Base64 数据为字节类型
audio_data_bytes = base64.b64decode(audio_data)

# 将解码后的音频数据保存为 Ogg 文件
with open('decoded_audio.ogg', 'wb') as f:
    f.write(audio_data_bytes)

print("音频解码成功并保存为 Ogg 文件。")
