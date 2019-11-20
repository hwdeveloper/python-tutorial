import VoiceAi

import turtle
t=turtle.Turtle()
t.shape("turtle")
t.speed(1)

turtleX=0
turtleY=0

def drawPlane(text):
  global turtleX
  global turtleY

  if(text.find('左')!=-1 or text.find("佐")!=-1):
       turtleX=turtleX-100
       t.goto(turtleX,turtleY)
  elif (text.find('右')!=-1):
       turtleX=turtleX+100
       t.goto(turtleX,turtleY)
  elif (text.find('上')!=-1):
       turtleY=turtleY+100
       t.goto(turtleX,turtleY)
  elif (text.find('下')!=-1):
       turtleY=turtleY-100
       t.goto(turtleX,turtleY)
       


while True:
    VoiceAi.rec()
    text=VoiceAi.listen()
    drawPlane(text)