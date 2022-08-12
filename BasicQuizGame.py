from tkinter import *
from tkinter import ttk
import tkinter
y=0
a=ttk.Notebook()
def result(var):
    var.set(var.get()+100)
mks = tkinter.IntVar()
frame1=ttk.Frame(a)
frame2=ttk.Frame(a)
frame3=ttk.Frame(a)
frame4=ttk.Frame(a)
frame5=ttk.Frame(a)
frame6=ttk.Frame(a)
root=ttk.Frame(a)
answer_key=["Rome","Scotland","55","Interrobang","Mickeys"]
def quiz(y):
    a.add(frame1,text="Q1")
    a.add(frame2,text="Q2")
    a.add(frame3,text="Q3")
    a.add(frame4,text="Q4")
    a.add(frame5,text="Q5")
    a.add(frame6,text="Result")

    Label(frame1,text="Where would you be if you were standing on the Spanish Steps?", font=("Consolas",20,"bold"),bg="yellow").grid(row=2,column=2)
    Button(frame1,text="Barcelona",font=("Consolas",10,"bold"),bg="light blue",command=a1_wrong).grid(row=3,column=2)
    Button(frame1,text="Rome",font=("Consolas",10,"bold"),bg="light green",command=a1_correct).grid(row=4,column=2)
    Button(frame1,text="London",font=("Consolas",10,"bold"),bg="light pink",command=a1_wrong).grid(row=5,column=2)

    Label(frame2,text="What country has a unicorn as part of its national emblem?", font=("Consolas",20,"bold"),bg="yellow").grid(row=2,column=2)
    Button(frame2,text="Scotland",font=("Consolas",10,"bold"),bg="light blue",command=a2_correct).grid(row=3,column=2)
    Button(frame2,text="Finland",font=("Consolas",10,"bold"),bg="light green",command=a2_wrong).grid(row=4,column=2)
    Button(frame2,text="Singapore",font=("Consolas",10,"bold"),bg="light pink",command=a2_wrong).grid(row=5,column=2)

    Label(frame3,text="How many miles is New Zealand's Ninety Mile Beach?", font=("Consolas",20,"bold"),bg="yellow").grid(row=2,column=2)
    Button(frame3,text="107",font=("Consolas",10,"bold"),bg="light blue",command=a3_wrong).grid(row=3,column=2)
    Button(frame3,text="90",font=("Consolas",10,"bold"),bg="light green",command=a3_wrong).grid(row=4,column=2)
    Button(frame3,text="55",font=("Consolas",10,"bold"),bg="light pink",command=a3_correct).grid(row=5,column=2)

    Label(frame4,text="When a question mark immediately follows an exclamation mark, that is called what?", font=("Consolas",20,"bold"),bg="yellow").grid(row=2,column=2)
    Button(frame4,text="Interrogate",font=("Consolas",10,"bold"),bg="light blue",command=a4_wrong).grid(row=3,column=2)
    Button(frame4,text="Interroclaim",font=("Consolas",10,"bold"),bg="light green",command=a4_wrong).grid(row=4,column=2)
    Button(frame4,text="Interrobang",font=("Consolas",10,"bold"),bg="light pink",command=a4_correct).grid(row=5,column=2)

    Label(frame5,text="The computer mouse speed is measured in what?", font=("Consolas",20,"bold"),bg="yellow").grid(row=2,column=2)
    Button(frame5,text="Clicks",font=("Consolas",10,"bold"),bg="light blue",command=a5_wrong).grid(row=3,column=2)
    Button(frame5,text="Mickeys",font=("Consolas",10,"bold"),bg="light green",command=a5_correct).grid(row=4,column=2)
    Button(frame5,text="Minnies",font=("Consolas",10,"bold"),bg="light pink",command=a5_wrong).grid(row=5,column=2)

    Label(frame6, text="The total marks obtained is:-", font=("Consolas",20,"bold"),bg="light green",fg="green").grid(row=2,column=2)
    Label(frame6, textvariable=mks,font=("Consolas",20,"bold"),bg="blue",fg="light blue").grid(row=5,column=2)
    
def a1_correct():
    Label(frame1,text="Correct!",font=("Consolas",30,"bold"),background="green",fg="yellow").grid(row=7,column=2)
    Label(frame1,text="Marks obtained:100",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    result(mks)

def a1_wrong():
    Label(frame1,text="Inorrect!",font=("Consolas",30,"bold"),background="red",fg="yellow").grid(row=7,column=2)
    Label(frame1,text="Marks obtained:0",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    Label(frame1,text="Correct answer is:",font=("Consolas",30,"bold"),background="orange",fg="brown").grid(row=13,column=2)
    Label(frame1,text="Rome",font=("Consolas",30,"bold"),background="light blue",fg="green").grid(row=15,column=2)

def a2_correct():
    Label(frame2,text="Correct!",font=("Consolas",30,"bold"),background="green",fg="yellow").grid(row=7,column=2)
    Label(frame2,text="Marks obtained:100",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    result(mks)

def a2_wrong():
    Label(frame2,text="Inorrect!",font=("Consolas",30,"bold"),background="red",fg="yellow").grid(row=7,column=2)
    Label(frame2,text="Marks obtained:0",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    Label(frame2,text="Correct answer is:",font=("Consolas",30,"bold"),background="orange",fg="brown").grid(row=13,column=2)
    Label(frame2,text="Scotland",font=("Consolas",30,"bold"),background="light blue",fg="green").grid(row=15,column=2)

def a3_correct():
    Label(frame3,text="Correct!",font=("Consolas",30,"bold"),background="green",fg="yellow").grid(row=7,column=2)
    Label(frame3,text="Marks obtained:100",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    result(mks)

def a3_wrong():
    Label(frame3,text="Inorrect!",font=("Consolas",30,"bold"),background="red",fg="yellow").grid(row=7,column=2)
    Label(frame3,text="Marks obtained:0",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    Label(frame1,text="Correct answer is:",font=("Consolas",30,"bold"),background="orange",fg="brown").grid(row=13,column=2)
    Label(frame1,text="55",font=("Consolas",30,"bold"),background="light blue",fg="green").grid(row=15,column=2)

def a4_correct():
    Label(frame4,text="Correct!",font=("Consolas",30,"bold"),background="green",fg="yellow").grid(row=7,column=2)
    Label(frame4,text="Marks obtained:100",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    result(mks)

def a4_wrong():
    Label(frame4,text="Inorrect!",font=("Consolas",30,"bold"),background="red",fg="yellow").grid(row=7,column=2)
    Label(frame4,text="Marks obtained:0",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    Label(frame1,text="Correct answer is:",font=("Consolas",30,"bold"),background="orange",fg="brown").grid(row=13,column=2)
    Label(frame1,text="Interrobang",font=("Consolas",30,"bold"),background="light blue",fg="green").grid(row=15,column=2)

def a5_correct():
    Label(frame5,text="Correct!",font=("Consolas",30,"bold"),background="green",fg="yellow").grid(row=7,column=2)
    Label(frame5,text="Marks obtained:100",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    result(mks)

def a5_wrong():
    Label(frame5,text="Inorrect!",font=("Consolas",30,"bold"),background="red",fg="yellow").grid(row=7,column=2)
    Label(frame5,text="Marks obtained:0",font=("Consolas",30,"bold"),background="black",fg="white").grid(row=10,column=2)
    Label(frame1,text="Correct answer is:",font=("Consolas",30,"bold"),background="orange",fg="brown").grid(row=13,column=2)
    Label(frame1,text="Mickeys",font=("Consolas",30,"bold"),background="light blue",fg="green").grid(row=15,column=2)

#print(mks)
quiz(y)
a.pack()
a.mainloop()