import pygame
from aip import AipSpeech
import speech_recognition as sr
import urllib3


# 忽略百度api连接时的报错信息。
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Baidu Speech API
APP_ID = '17750758'
API_KEY = 'f9v3TLtb6KIIZR8IyqsRY1zp'
SECRET_KEY = 'rM4IqhyUCkilmFKWGBYio1iOreFCIlpj'
    
client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)


# 录音
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("请下达指令吧！！")
        audio = r.listen(source)

    with open("recording.wav", "wb") as f:
        f.write(audio.get_wav_data())

# 百度语音转文字
def listen():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1536,
    })

    text_input=''

    try:
      text_input = result["result"][0]
    except Exception :
      text_input='错误'
      print(text_input)
    return text_input
   



