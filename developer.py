from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",15,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img=Image.open(r"college_images\\dev.jpg")
        img=img.resize((1530,720),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        #Frame--
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)

        #img_Dev=Image.open(r"college_images\\dev.jpg")
        #img_Dev=img_Dev.resize((200,200),Image.LANCZOS)
        #self.photoimg_Dev=ImageTk.PhotoImage(img_Dev)

        #f_lbl_dev=Label(main_frame,image=self.photoimg_Dev)
        #f_lbl_dev.place(x=300,y=0,width=200,height=200)

       #developer info--
        dev_label=Label(main_frame,text="Hello, My name is Sweta Goswami",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am a B-tech CSE student in R.D enginerring college.",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=40)

        img_lbl=Image.open(r"college_images\\photo.jpg")
        img_lbl=img_lbl.resize((500,500),Image.LANCZOS)
        self.photoimg_lbl=ImageTk.PhotoImage(img_lbl)

        f_lbl_lbl=Label(main_frame,image=self.photoimg_lbl)
        f_lbl_lbl.place(x=0,y=210,width=500,height=500)







if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
