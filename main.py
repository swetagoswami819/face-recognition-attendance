from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognization import Face_recognizer
from attendance import Attendance
from developer import Developer
from help import Help
 

class Face_recongnition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

    # first image on top-- 
        img=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\BestFacialRecognition.jpg")
        img=img.resize((510,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)

    #second image on top--
        img1=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\facialrecognition.png")
        img1=img1.resize((510,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=511,y=0,width=510,height=130)

    #third image on top--
        img2=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\2-AI-invades-automobile-industry-in-2019.jpeg")
        img2=img2.resize((510,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1017,y=0,width=510,height=130)

    #bg image--
        img3=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
    
    #title lable--
        title_lbl=Label(bg_img,text="FACE RECOGINITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="navy blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    #****************************time************************************
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
    
        lbl=Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

    #student button--
        img4=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\student.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details_btn,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_lbl=Button(bg_img,text="Student Details",command=self.student_details_btn,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_lbl.place(x=200,y=300,width=220,height=40)

    #Face detector button--
        img5=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\face_detector1.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognizer_btn)
        b2.place(x=500,y=100,width=220,height=220)

        b2_lbl=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black",command=self.face_recognizer_btn)
        b2_lbl.place(x=500,y=300,width=220,height=40)

    #Attendance button--
        img6=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\report.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_btn)
        b3.place(x=800,y=100,width=220,height=220)

        b3_lbl=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black",command=self.attendance_btn)
        b3_lbl.place(x=800,y=300,width=220,height=40)

    #Help Desk button--
        img7=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\helpdesk.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_btn)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_lbl=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black",command=self.help_btn)
        b4_lbl.place(x=1100,y=300,width=220,height=40)

    #Train Data button--
        img8=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\train.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_Data_btn)
        b5.place(x=200,y=380,width=220,height=220)

        b5_lbl=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black",command=self.train_Data_btn)
        b5_lbl.place(x=200,y=580,width=220,height=40)

    #photos button--
        img9=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\new.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)

        b6_lbl=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b6_lbl.place(x=500,y=580,width=220,height=40)

    #Developer button--
        img10=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\Team-Management-Software-Development.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_btn)
        b7.place(x=800,y=380,width=220,height=220)

        b7_lbl=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black",command=self.developer_btn)
        b7_lbl.place(x=800,y=580,width=220,height=40)

    #Exit button--
        img11=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\exit.jpg")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_lbl=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black",command=self.iexit)
        b8_lbl.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
    
    def iexit(self):
        self.iexit=messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return 


    #************************functions button*******************************
    def student_details_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_Data_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognizer_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognizer(self.new_window)


    def attendance_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_btn(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    



if __name__ == "__main__":
    root=Tk()
    obj=Face_recongnition_System(root)
    root.mainloop()
