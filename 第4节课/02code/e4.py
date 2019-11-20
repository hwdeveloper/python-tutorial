import turtle
#把海龟改为熊猫
turtle.register_shape('panda.gif')
turtle.shape('panda.gif')
#设置速度
turtle.speed(1)
def move(x,y):
    turtle.goto(x,0)
    turtle.goto(x,y)
    turtle.goto(0,y)
    turtle.goto(0,0)

move(200,100)
