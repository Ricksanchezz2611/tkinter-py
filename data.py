import tkinter as tk
from tkinter import ttk
import openpyxl

def load_data():
    path = "C:/Users/Karthikeya/OneDrive/Desktop/datazerror/summer.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active 

    list_values = list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, values=value_tuple)

def insert_row():
    name = name_entry.get()
    age = int(age_spinbox.get())
    stats = status_combobox.get()
    p_stats = "Graduate" if a.get() else "Non-Graduate"

    print(name, age, stats, p_stats)


    path = "C:/Users/Karthikeya/OneDrive/Desktop/datazerror/summer.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    row_values = [name,age,stats,p_stats]
    sheet.append(row_values)
    workbook.save(path)


    treeview.insert('', tk.END, values=row_values)

    name_entry.delete(0, "end")
    name_entry.insert(0, "Name")
    age_spinbox.delete(0, "end")
    age_spinbox.insert(0, "Age")
    status_combobox.set(combo_list[0])
    checkbutton.state(["!selected"])        

def toggle_mode():
    if(mode_switch.instate(["selected"])):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

root = tk.Tk()
style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

combo_list = ["Student","Non-student","Teacher","Other"]

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
widgets_frame.grid(row=0,column=0,padx=20,pady=20)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
name_entry.grid(row=0,column=0,padx=5,pady=(0,5),sticky="ew")

age_spinbox = ttk.Spinbox(widgets_frame,from_=18,to=100)
age_spinbox.insert(0, "Age")
age_spinbox.bind("<FocusIn>", lambda e: age_spinbox.delete('0', 'end'))
age_spinbox.grid(row=1,column=0,padx=5,pady=(0,5),sticky="ew")

status_combobox = ttk.Combobox(widgets_frame,values=combo_list)
status_combobox.current(0)
status_combobox.grid(row=2,column=0,padx=5,pady=(0,5),sticky="ew")

a = tk.BooleanVar()
checkbutton = ttk.Checkbutton(widgets_frame,text="graduate",variable = a)
checkbutton.grid(row=3,column=0,padx=5,pady=(0,5),sticky="nsew")

button = ttk.Button(widgets_frame,text="Insert",command=insert_row)
button.grid(row=4,column=0,padx=5,pady=(0,5),sticky="nsew")

separator = ttk.Separator(widgets_frame)
separator.grid(row=5,column=0,padx=(20,10),pady=10,sticky="ew")

mode_switch = ttk.Checkbutton(widgets_frame,text="Mode",style="Switch",command=toggle_mode)
mode_switch.grid(row=6,column=0,padx=5,pady=10,sticky="nsew")

treeframe = ttk.Frame(frame)
treeframe.grid(row=0,column=1,pady=10)
treeScroll = ttk.Scrollbar(treeframe)
treeScroll.pack(side="right",fill="y")

cols = ("name","age","status","p status")
treeview = ttk.Treeview(treeframe,show="headings",yscrollcommand=treeScroll.set,columns=cols,height=13)
treeview.column("name",width=100)
treeview.column("age",width=50)
treeview.column("status",width=100)
treeview.column("p status",width=100)
treeview.pack()
treeScroll.config(command=treeview.yview)
load_data()

root.mainloop()