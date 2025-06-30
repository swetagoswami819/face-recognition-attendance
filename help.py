from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
 

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        title_lbl=Label(self.root,text="FULL STACK JAVA DEVELOPER",font=("times new roman",15,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img=Image.open(r"college_images\laptop.jpg")
        img=img.resize((1500,720),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1500,height=720)

        dev_label=Label(f_lbl,text="Email : sg8528224@gmail.com",font=("times new roman",15,"bold"),bg="black",fg="blue")
        dev_label.place(x=580,y=180)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()

