from bs4 import BeautifulSoup #导入包
import re
import os
list=os.listdir("../html")
f=open("../text/投诉文本.txt","w",encoding='utf-8')#utf-8方式打开
#print(len(list))
for i in range(0,len(list)):
    path = os.path.join("../html", list[i])
    if os.path.isfile(path):
        soup = BeautifulSoup(open(path, 'rb'))  # 以rb的方式打开文件
        headlist = soup.find_all('h1')
        for head in headlist:
            alist = head.find_all('a')
            for a in alist:
                if ("[咨询投诉]" not in a.string):
                    f.write(a.string)
                    f.write("\n")
                    print(a.string)

        # 接着提取正文和回复 <TD id=postmessage。。。。>
        tdlist = soup.find_all('td', attrs={'id': re.compile("postmessage")})
        for td in tdlist:
            text = td.get_text()
            f.write(text)
            f.write("\n")
            print(text)
        print(i)


f.close()

# soup= BeautifulSoup(open('../html/321188&.htm','rb'))#以rb的方式打开文件
# #首先提取标题：<H1 class=ts>找到最里面那层<A>
# f=open("../text/投诉文本.txt","w",encoding='utf-8')#utf-8方式打开
# #print(soup.prettify())
# headlist=soup.find_all('h1')
# for head in headlist:
#     alist=head.find_all('a')
#     for a in alist:
#         if("[咨询投诉]"not in a.string):
#             f.write(a.string)
#             print(a.string)
#
#
# #接着提取正文和回复 <TD id=postmessage。。。。>
# tdlist=soup.find_all('td',attrs={'id':re.compile("postmessage")})
# for td in tdlist:
#     text=td.get_text()
#     f.write(text)
#     print(text)

# f.close()










