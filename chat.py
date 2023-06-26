import openai

def send_msg(msg:str, 
             API_KEY = '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')-> str:

    openai.api_key = API_KEY

# 发送 API 请求
    response = openai.ChatCompletion.create(
        messages=[
            {'role': 'system', 'content': 'you are a chat expert'},
            {'role': 'user', 'content': msg}
        ],
        model='gpt-3.5-turbo-0301',
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        max_tokens=1000,
    )
    reply = response['choices'][0]['message']['content']
    return reply

if __name__=='__main__':
    send_msg('hello')

print(send_msg('hello'))