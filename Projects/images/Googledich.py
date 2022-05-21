from googletrans import Translator
from tkinter import *
from PIL import Image,ImageTk #chen anh

# tao tk window
root = Tk()
root.title('Google Translate')
root.geometry("500x630")  #kich thuoc
root.iconbitmap('images/logo.ico')  #chen logo

load = Image.open('images/background.png') #chen background
render = ImageTk.PhotoImage(load)   #xuat hinh ra
img = Label(root,image= render)  #label trong tkinter giup hien thi hinh anh vs van ban
img.place(x=0,y=0)   #dat len toa do man hinh

name = Label(root,text="Translator",fg="#FFFFFF",bd=0,bg="#03152D")
name.config(font=("Transformers Movie",30))  #config giup cap nhat widgit
name.pack(pady=10) #sap xep layout, pady: cach truc tung 10 don vi, padx: cach truc x 10 don vi


box = Text(root,width=28,heigh=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

def translate1():
    Input = box.get(1.0, END)
    print(Input)
    t = Translator()
    a = t.translate(Input, src='vi', dest='en')
    b = a.text
    box1.insert(END, b)

def translate2():
    Input1 = box.get(1.0, END)
    print(Input1)
    t = Translator()
    c = t.translate(Input1, src='en', dest='vi')
    d = c.text
    box1.insert(END, d)

def translate():
    pass

clear_button = Button(button_frame,text="Clear text",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=clear)
clear_button.place(x=80,y=310)

# trans_button = Button(button_frame,text="Translate",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate)
# trans_button.place(x=290,y=350)

vi_en = Button(button_frame,text="Vi -> En",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate1)
vi_en.place(x=220,y=310)

en_vi = Button(button_frame,text="En -> Vi",font=(("Arial"),10,'bold'),bg='#303030',fg="#FFFFFF",command=translate2)
en_vi.place(x=360,y=310)

box1 = Text(root,width=28,heigh=8,font=("ROBOTO",16))
box1.pack(pady=60)

root.mainloop() #tao chuoi vong lap de hien thi cua so