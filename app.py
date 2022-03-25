from tkinter import*
from PIL import Image,ImageTk
from googletrans import Translator

#tạo tk window
root=Tk()
root.title('Google Galaxy')
root.geometry("500x630")
root.iconbitmap('logo.ico')

load=Image.open("background.png")
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name=Label(root,text="Translator",fg="#A333FF",bd=0,bg="#03152d")
name.config(font=("Transformers Movie",30))
box=Text(root,width=35,height=8,font=("ROBOTO",16))
name.pack(pady=10)
box.pack(pady=20)

Button_frame=Frame(root).pack(side=BOTTOM)
def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    input=box.get(1.0,END)
    print(input)
    t=Translator()
    a=t.translate(input,src="vi",dest="en")
    b=a.text
    box1.insert(END,b)
clear_button=Button(Button_frame,text="clear_text",font=(("Arial"),10,'bold'),bg="#303030",fg="#A333FF",command=clear)
clear_button.place(x=150,y=310)
trans_button=Button(Button_frame,text="Translate",font=(("Arial"),10,'bold'),bg="#303030",fg="#A333FF",command=translate)
trans_button.place(x=290,y=310)
box1=Text(root,width=35,height=8,font=("ROBOTO",16))
box1.pack(pady=50)






root.mainloop()
