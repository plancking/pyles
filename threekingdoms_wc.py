import jieba,wordcloud

txt=open("threekingdoms.txt","r",encoding="utf-8").read()
txt=jieba.lcut(txt)
w=wordcloud.WordCloud(width=600,font_path="msyh.ttc",height=400,max_words=15)
w.generate(" ".join(txt))
w.to_file("a_.png")
