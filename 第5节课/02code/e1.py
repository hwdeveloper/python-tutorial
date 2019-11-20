import VoiceAi
while True:
    VoiceAi.rec()
    text=VoiceAi.listen()
    print(text)