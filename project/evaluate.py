import random
file=open("../text/实体关联排序.txt",'r',encoding='UTF-8')
dic={}#存放数据的字典
line=file.readline()
i=0
while(line):
    text=line.strip('\n')
    dic[(text.split()[0],text.split()[1])]=text.split()[2]
    line=file.readline()
    i+=1
    if i>=10000:
        break
html = ""
for w, c in dic.items():
    color = 'rgb(%s, %s, %s)' % (str(random.randint(0, 255)), str(random.randint(0, 255)), str(random.randint(0, 255)))
    fontsize = int(float(c) * 10 + 10)
    html += '<span style=\"font-size:' + str(fontsize) + 'px;color:' + color + ';float:left;\">' +'&#160'+ w[0]+'-'+w[1]+'&#160' + '</span>'

# dump it to a file
f=open('../text/result.html','w',encoding='UTF-8')
f.write(html)
print(html)
f.close()