#收银员输入苹果的价格
p1=input("苹果价格:")
#p1是个字符串，需要把字符串转为浮点数
p2=float(p1)
#购买苹果重量
w1=input("苹果重量:")
#把w1转为浮点数
w2=float(w1)
#计算总的金额
total = p2*w2
print("总金额是:",total)