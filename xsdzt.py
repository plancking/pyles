import jieba,wordcloud

txt=open("xsdzt.txt","r",encoding="utf-8").read()
txt=jieba.lcut(txt)
w=wordcloud.WordCloud(width=800,height=600,font_path="msyh.ttc",max_words=20)
w.generate(" ".join(txt))
w.to_file("b.jpg")
