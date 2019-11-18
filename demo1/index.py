import VoiceAi

import turtle
#把海龟改为熊猫
turtle.register_shape('panda.gif')
turtle.shape('panda.gif')
turtle.speed(1)

turtleX=0
turtleY=0

def drawPlane(text):
  global turtleX
  global turtleY

  if(text.find('左')!=-1):
       print("向左走")
       turtleX=turtleX-100
       turtle.goto(turtleX,turtleY)
  elif (text.find('右')!=-1):
       print("向右走")
       turtleX=turtleX+100
       turtle.goto(turtleX,turtleY)
  elif (text.find('上')!=-1):
       print("向上走")
       turtleY=turtleY+100
       turtle.goto(turtleX,turtleY)
  elif (text.find('下')!=-1):
       print("向下走")
       turtleY=turtleY-100
       turtle.goto(turtleX,turtleY)
       


while True:
    VoiceAi.rec()
    text=VoiceAi.listen()
    drawPlane(text)
