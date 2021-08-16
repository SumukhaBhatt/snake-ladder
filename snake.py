def again():
    global s
    a[s[0]-1].config(bg="white")
    a[s[1]-1].config(bg="white")
    s=[0,0]
    sc[0]["value"]=0
    sb[0]["text"]=0
    sc[1]["value"]=0
    sb[1]["text"]=0
def sum1(opt=0,ctr=0,clr="blue"):
    global s
    rn=randrange(1,7)
    def slow(rn,i=1):
        global s
        if i<rn:
            if not((s[opt] in lad) or( s[opt] in snake) or (s[not opt]==s[opt])):
                a[s[opt]-1].config(bg="white")
            s[opt]=s[opt]+1
            if not((s[opt] in lad) or( s[opt] in snake) or (s[not opt]==s[opt])):
                a[s[opt]-1].config(bg=clr)
            sn.after(1000,slow,rn,i+1)
        else:
            if not(s[opt] in lad or s[opt] in snake or s[not opt]==s[opt]):
                a[s[opt]-1].config(bg="white")
            s[opt]=s[opt]+1
            if s[opt] in lad:
                a[lad[s[opt]]-1].config(bg=clr)
                s[opt]=lad[s[opt]]
                sc[opt]["value"]=s[opt]
                sb[opt]["text"]=s[opt]
                sn.after(1000,sum1,opt,ctr,clr)
                return
            elif s[opt] in snake:
                a[snake[s[opt]]-1].config(bg=clr)
                s[opt]=snake[s[opt]]
                sc[opt]["value"]=s[opt]
                sb[opt]["text"]=s[opt]
            else:
                a[s[opt]-1].config(bg=clr)
                sc[opt]["value"]=s[opt]
                sb[opt]["text"]=s[opt]
            if rn==6:
                sn.after(1000,sum1,opt,ctr,clr)
                return
            elif ctr==0:
                sn.after(2000,sum1,1,1,"brown")
                return
            return
    lb["text"]=rn
    if (s[opt]+rn)<=100:
        if s[opt]+rn==100:
            if opt==0:
                messagebox.showinfo("Congrats","You won the match")
                again()
                return
            else:
                messagebox.showinfo("Bad luck","you loss the match")
                again()
                return
        slow(rn)
    elif ctr==0:
        sn.after(2000,sum1,1,1,"brown")
from tkinter import Frame,Label,Button,Tk,HORIZONTAL
from random import randrange
from tkinter import messagebox
from tkinter.ttk import Progressbar
r=Tk()
r.geometry("500x600")
r.minsize(width=500,height=550)
r.maxsize(width=500,height=600)
r.title("Snake game")
sn=Frame(r,bg="white")
sn.grid()
sn1=Frame(r,background="white")
sn1.grid(sticky="w")
a=[None for x in range(100)]
g=1
m=100
n=90
rw=-1
s=[0,0]
while g<=5:
    cl=0
    rw=rw+1
    for i in range(m,n,-1):
        a[i-1]=Label(sn,text=i,bg="white",)
        a[i-1].grid(row=rw,column=cl,padx=15,pady=15)
        cl=cl+1
    rw=rw+1
    cl=0
    for i in range(m-19,n+1):
        a[i-1]=Label(sn,text=i,bg="white",)
        a[i-1].grid(row=rw,column=cl,pady=15,padx=15)
        cl=cl+1
    m=m-20
    n=n-20
    g=g+1
lad={4:14,9:31,20:38,28:84,40:59,63:81,71:91}
snake={17:7,54:34,62:18,64:60,87:24,93:73,95:75,99:46}
for i in lad:
    a[i-1].config(bg="green")
for i in snake:
    a[i-1].config(bg="red")
b1=Button(sn,text="Play",bg="violet",command=sum1).grid(column=4,row=101)
b2=Button(sn,text="Play again",bg="violet",command=again).grid(column=6,row=101)
lb=Label(sn,text=0)
lb.grid(column=5,row=101)
sc=[None,None]
sb=[None,None]
Label(sn1,text="Blue:").grid(column=0,row=0)
sc[0]=Progressbar(sn1,orient=HORIZONTAL,length=190,mode="determinate")
sc[0].grid(column=1,row=0,sticky="w")
sb[0]=Label(sn1,text=0)
sb[0].grid(column=2,row=0)
Label(sn1,text="Brown:").grid(column=0,row=1)
sc[1]=Progressbar(sn1,orient=HORIZONTAL,length=190)
sc[1].grid(column=1,row=1,sticky="w")
sb[1]=Label(sn1,text=0)
sb[1].grid(column=2,row=1)
r.mainloop()
