import jieba
from collections import Counter
f=open("../text/投诉文本.txt",'r', encoding='UTF-8')#只读，注意编码方式
of=open("../text/高频词.txt",'w', encoding='UTF-8')
#加载停用词表
stopWord = [line.strip()for line in open('../text/停用词.txt').readlines() ]
line=f.read() #读取文件一行代码，有可能读的是空行
if line:
    seg_list = jieba.cut(line, cut_all=False)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n'and x not in stopWord:
            c[x] += 1
    for i in c.most_common(1500):
        of.write(str(i[0])+' '+str(i[1])+'\n')
        print(i)
f.close()
of.close()
