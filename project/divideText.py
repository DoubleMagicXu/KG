import jieba
import os
from collections import Counter
f=open("../text/投诉文本.txt",'r', encoding='UTF-8')#只读，注意编码方式
line=f.read() #读取文件一行代码，有可能读的是空行
if line:
    #print(line)
    seg_list = jieba.cut(line, cut_all=False)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n':
            c[x] += 1
    #print("Full Mode: " + "/ ".join(seg_list))
    for i in c.most_common(1000):
        print(i)
    #print(c.most_common(50))


f.close()
