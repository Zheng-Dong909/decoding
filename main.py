from flask import Flask, request

app = Flask(__name__)

@app.route('/your-server-endpoint', methods=['POST'])
def handle_audio_data():
    audio_file = request.files['audio']
    if audio_file:
        # 保存音频文件
        audio_file.save('recorded_audio.ogg')
        return '音频数据已成功接收。'
    else:
        return '未收到音频数据。'

if __name__ == '__main__':
    app.run()
