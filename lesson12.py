fp=open("try.txt","w+")
fp.writelines(["hello","python"])
fp.seek(0)
for line in fp:
    print(line)
fp.close()
