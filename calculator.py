from tkinter import *
import tkinter as tk

root=Tk()
root.title("Calculator")
root.geometry('350x650')
    
def  data_ad():
    sum=float(name_entry.get())+float(name_entry2.get())
    answer_label2.config(text=sum)
def  data_sub():
    dif=float(name_entry.get())-float(name_entry2.get())
    answer_label2.config(text=dif)
def  data_mul():
    prd=float(name_entry.get())*float(name_entry2.get())
    answer_label2.config(text=prd)
def  data_div():
    div=round(float(name_entry.get())/float(name_entry2.get()),2)
    answer_label2.config(text=div)




name_label=Label(text="Enter 1st Number", font=("Times New Roman",20,"bold"))
name_label.place(x=30,y=20,height=50,width=280)
name_entry = Entry(root, font=('calibre',10,'normal'),)
name_entry.place(x=60,y=70,height=30,width=210)

name_label2=Label(text="Enter 2nd Number", font=("Times New Roman",20,"bold"))
name_label2.place(x=30,y=120,height=50,width=280)
name_entry2 = Entry(root, font=('calibre',10,'normal'),)
name_entry2.place(x=60,y=180,height=30,width=210)

answer_label=Label(text=" Result ", font=("Times New Roman",20,"bold"))
answer_label.place(x=30,y=320,height=40,width=280)
answer_label2=Label(text=" ", font=("Times New Roman",20,"bold"),background="white")
answer_label2.place(x=60,y=390,height=40,width=220)



add_button=Button(root,text="+",background="red",foreground="white",command=data_ad,
                font=("Aurella",20,"bold",))
add_button.place(x=60,y=270,height=30,width=30) 
done_button=Button(root,text="-",background="red",foreground="white",command=data_sub,
                font=("Aurella",20,"bold",))
done_button.place(x=120,y=270,height=30,width=30) 
done_button=Button(root,text="*",background="red",foreground="white",command=data_mul,
                font=("Aurella",20,"bold",))
done_button.place(x=180,y=270,height=30,width=30) 
done_button=Button(root,text="/",background="red",foreground="white",command=data_div,
                font=("Aurella",20,"bold",))
done_button.place(x=240,y=270,height=30,width=30) 

root.mainloop()