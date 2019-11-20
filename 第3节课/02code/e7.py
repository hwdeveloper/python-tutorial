
def age18(age):
    if(age>18):
        return True
    else:
        return False
        
#通过键盘输入你的年龄
a1 = input("输入年龄:")
#把年龄转为整数
a2 = int(a1)
#把年龄传给函数
if(age18(a2)):
    print("上大学")
else:
    print("好好学习")
