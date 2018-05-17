import os
f=open("../text/实体.txt",'r',encoding='UTF-8')
entity=[]
line=f.readline()
while line:#读取文件到LIST
    entity.append(line.strip('\n'))#去除'\n'
    line=f.readline()
dic={}#词典数组
for x in range(0,len(entity)-1):
    for y in range(x+1,len(entity)):
        dic[(entity[x],entity[y])]=0

# for x in entity:
#     for y in entity:
#         if(x!=y):
#             dic[(x,y)]=0
list=os.listdir("../text/htm")
for i in range(0,len(list)):#35000次循环
    path = os.path.join("../text/htm", list[i])
    if os.path.isfile(path):
        tf=open(path,"r",encoding='UTF-8')
        context=tf.read()
        for j in dic:  #750*1499
            if j[0] in context and j[1] in context:
                dic[j]+=1
        tf.close()
    print(i)


#词典按照Value降序
sort=sorted(dic.items(),key = lambda x:x[1],reverse = True)
ef=open("../text/实体关联.txt",'w',encoding='UTF-8')
for i in sort:
    ef.write(str(i[0][0])+' '+str(i[0][1])+' '+str(i[1])+'\n')
    print(i)
f.close()
ef.close()