import wxpy

rb=wxpy.Bot(cache_path=True)
'''
myfriend=rb.friends(update=False)
for i in myfriend:
    try:
        print(i.remark_name,"  ",i.signature,"\n")
    except:
        pass

'''
myf=rb.friends(update=False)
for i in myf:
    try:
        if i.remark_name=='何旭':
            i.send_msg(msg='hello world!!!')
        #print(i)
    except:
        pass

