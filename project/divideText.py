import jieba
import re
from collections import Counter
f=open("../text/投诉文本.txt",'r', encoding='UTF-8')#只读，注意编码方式
of=open("../text/高频词.txt",'w', encoding='UTF-8')
ef=open("../text/实体.txt",'w',encoding='UTF-8')
jieba.load_userdict('../text/自定义词.txt')#导入自定义词
#加载停用词表
stopWord = [line.strip()for line in open('../text/停用词.txt').readlines() ]
line=f.read()
if line:
    seg_list = jieba.cut(line, cut_all=False)
    c = Counter()
    for x in seg_list:
        if len(x) > 1 and x != '\r\n'and (x not in stopWord )and not x.isdigit():
            if(not re.match(r'[a-zA-Z]+',x)):#正则表达式过滤英文
                c[x] += 1
    for i in c.most_common(1500):
        of.write(str(i[0])+' '+str(i[1])+'\n')
        ef.write(str(i[0]) + '\n')
        print(i)
f.close()
of.close()
ef.close()
