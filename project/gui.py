import tkinter as tk
from tkinter import *
file=open("../text/实体关联排序.txt",'r',encoding='UTF-8')
dic={}#存放数据的字典
line=file.readline()
while(line):
    text=line.strip('\n')
    dic[(text.split()[0],text.split()[1])]=text.split()[2]
    line=file.readline()
print(len(dic))
delete=['客户']
def searchEntity(text):
    for i in dic:
        if text==str(i[0]) and str(i[1]) not in delete:
            print(str(i[1]))
            strvar.set(str(i[1]))
            return
        elif text==str(i[1]) and str(i[0]) not in delete:
            print(str(i[0]))
            strvar.set(str(i[0]))
            return;
    print("NONE")
    strvar.set("NONE")
def button():
    t=search.get()
    searchEntity(t)
def labelClear():
    t=search.get()

gui=tk.Tk()
gui.title('基于投诉文本的知识图谱')
gui.geometry('500x300+700+300')
search=tk.Entry(gui)
go=tk.Button(gui,text='GO',command=button)
clear=tk.Button(gui,text='CLEAR',command=labelClear)
strvar=StringVar()
strvar.set("")
label=tk.Label(gui,textvariable=strvar)
search.pack()
go.pack()
label.pack(padx=5, pady=80)
gui.mainloop()
file.close()


#物业 ：没人  机动车：机动车道  交警：交管
