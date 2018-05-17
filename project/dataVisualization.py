import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['simHei']
plt.rcParams['axes.unicode_minus']=False#解决中文乱码问题
file=open("../text/高频词.txt",'r',encoding='UTF-8')
eef=open("../text/实体关联.txt",'r',encoding='UTF-8')
ees=open("../text/实体关联排序.txt",'r',encoding='UTF-8')
# eline=file.readline()
# edic={}
# while eline:
#     text = eline.strip('\n')
#     edic[text.split()[0]] = text.split()[1]
#     eline = file.readline()
# freq=[]
# for i in edic.values():
#     freq.append(int(i))
# plt.bar(range(len(edic)),freq,color='gray')
# plt.show()
eesdic={}
eesline=ees.readline()
while eesline:
    text=eesline.strip('\n')
    eesdic[(text.split()[0],text.split()[1])]=text.split()[2]
    eesline=ees.readline()

freq=[]
k=0
for i in eesdic.values():
    freq.append(float(i))
    k+=1
    if k>=15000:
        break

plt.bar(range(len(freq)),freq,color='gray')
plt.show()


file.close()
eef.close()
ees.close()