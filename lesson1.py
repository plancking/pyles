tempstr = input("请输入带符号的温度值：")
if tempstr[-1] in ['F','f']:
    c = (eval(tempstr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}c".format(c))
elif tempstr[-1] in ['C','c']:
    f=1.8*eval(tempstr[0:-1])+32
    print("转换后的温度是{:.2f}f".format(f))
else:
    print("输入格式错误")

