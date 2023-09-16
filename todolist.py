from tkinter import *
import tkinter as tk

root=Tk()
root.title("To Do List")
root.geometry('350x420')
root.config(background="lavender")
def add_task():
    task =task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
def del_task():
    task_selected=task_list.curselection()
    if task_selected:
        task_list.delete(task_selected)
        
task_label=Label(text="Enter a task", font=("Times New Roman",20,"bold"),background="lavender")
task_label.place(x=30,y=20,height=50,width=280)
task_entry = Entry(root, font=('calibre',10,'normal'),)
task_entry.place(x=60,y=70,height=30,width=210)
add_button = tk.Button(root, text="Add Task" , background="brown", foreground="white",command=add_task)
add_button.place(x=100,y=110,height=30,width=140)
del_button = tk.Button(root, text="Delete Task" , background="brown", foreground="white", command=del_task)
del_button.place(x=100,y=150,height=30,width=140)

task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
task_list.place(x=60,y=200,height=180,width=210)


root.mainloop()