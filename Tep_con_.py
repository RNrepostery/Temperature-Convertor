from tkinter import *
mw=Tk()
def tem():
    f=cel.get()
    f=float(f)
    c=(f-32)*5/9
    l2["text"]=f"{f}fahrenhei={c:.2f}celsius"

def temp():
    c=cel.get()
    c=float(c)
    f=c*9/5+32
    l2["text"]=f"{c}celsius={f:.2f}fahrenhei"


def r1():
    f.pack_forget() 
    f2.pack(fill=BOTH,expand=1) 

def r2():
    f2.pack_forget() 
    f.pack(fill=BOTH,expand=1)    

mw.geometry("350x150+600+200")
mw.title("Temperature converter")

sf=Frame(mw)
sf.pack(fill=BOTH,expand=1)

f=Frame(sf)
f.pack(fill=BOTH,expand=1)
l1=Label(f,text="fahrenheit",width=8)
l1.pack(side=LEFT,padx=10)
cel=IntVar()
e1=Entry(f,font=("Centaur"),textvariable=cel)
e1.pack(side=LEFT,padx=10)
b1=Button(f,text="Convert",height=1,width=6,command=tem)
b1.pack(side=LEFT,pady=2)

f2=Frame(sf)
f2.pack(fill=BOTH,expand=1)
l1=Label(f2,text="Celsius",width=8)
l1.pack(side=LEFT,padx=10)
cel=IntVar()
e1=Entry(f2,font=("Centaur"),textvariable=cel)
e1.pack(side=LEFT,padx=10)
b1=Button(f2,text="Convert",height=1,width=6,command=temp)
b1.pack(side=LEFT,pady=2)

l2=Label(mw,text="WELCOME")
l2.pack()
lb=LabelFrame(mw,text="Option")
lb.pack(fill=BOTH,expand=1)
val=IntVar()
val.set(1)
r1=Radiobutton(lb,text="F to C",value=0,variable=val,command=r1)
r1.pack(side=RIGHT,padx=2,pady=2)
r2=Radiobutton(lb,text="C to F",value=1,variable=val,command=r2)
r2.pack(side=LEFT,padx=2,pady=2)


mainloop()