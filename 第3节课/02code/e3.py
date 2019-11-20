i = 0
while i < 10:
    # 当 i == 7 时，不希望执行需要重复执行的代码
    if i == 7:
        # i为什么要增加1
        i = i+1
        continue
    # 重复执行的代码
    print(i)
    i = i+1