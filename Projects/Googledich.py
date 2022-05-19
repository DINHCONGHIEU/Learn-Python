from googletrans import Translator
from tkinter import *
from PIL import Image,ImageTk #chen anh

t = Translator()
a = t.translate("em dep qua",src="vi",dest="en")
b = a.text

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
    pass

def translate():
    pass



root.mainloop() #tao chuoi vong lap de hien thi cua so