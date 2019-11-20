import VoiceAi
while True:
    VoiceAi.rec()
    text=VoiceAi.listen()
    if(text.find('小刚')!=-1){
        print("主人，你的名字太棒了！")
    }else{
        print("主人，我没有听到你的名字！")
    }