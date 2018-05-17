eef=open("../text/实体关联.txt",'r',encoding='UTF-8')
ef=open("../text/高频词.txt",'r',encoding='UTF-8')
kf=open("../text/实体关联排序.txt",'w',encoding='utf-8')#utf-8方式打开
eedic={}
edic={}
eesdic={}
line=eef.readline()
while(line):
    text=line.strip('\n')
    eedic[(text.split()[0],text.split()[1])]=text.split()[2]
    #print(eedic)
    line=eef.readline()

line=ef.readline()
while line:
    text = line.strip('\n')
    edic[text.split()[0]] = text.split()[1]
    line=ef.readline()
for i in eedic:
    eesdic[(i[0],i[1])]=int(eedic[i])/int(edic[i[0]])/int(edic[i[1]])

sort=sorted(eesdic.items(),key = lambda x:x[1],reverse = True)
for i in sort:
    kf.write(str(i[0][0])+' '+str(i[0][1])+' '+str(i[1])+'\n')
    print(i)
eef.close()
ef.close()
kf.close()