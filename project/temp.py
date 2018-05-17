a={("投诉","半个月"):0,("小区","厉害"):0}
f=open("../text/htm/0.txt",'r',encoding='UTF-8')
text=f.read()
for i in a:
    if i[0] in text and i[1] in text:
        a[i]+=1
t=sorted(a.items(),key = lambda x:x[1],reverse = True)

for i in t:
    print(i[0][0],i[0][1],i[1])
f.close()