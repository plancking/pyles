import jieba,wordcloud

txt=open("threekingdoms.txt","r",encoding="utf-8").read()
ls1=jieba.lcut(txt)
counts={}
for word in ls1:
    if len(word)==1:
        continue
    counts[word]=counts.get(word,0)+1
ls2=list(counts.items())
ls2.sort(key=lambda x:x[1],reverse=True)
wlist=[]
for i in range(16):
    wlist.append(ls2[i][0])
w=wordcloud.WordCloud(width=600,font_path="msyh.ttc",height=400)
w.generate(" ".join(wlist))
w.to_file("a.png")
