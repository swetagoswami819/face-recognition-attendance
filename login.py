from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_recongnition_System
from register import Register

import mysql.connector

def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

    #===============================image=========================    
        img=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\frontal.jpg")
        img=img.resize((1530,800),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=800)


        #img1=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\logo.png")
        #img1=img1.resize((150,100),Image.LANCZOS)
        #self.photoimg1=ImageTk.PhotoImage(img1)

        #f_lbl=Label(self.root,image=self.photoimg1)
        #f_lbl.place(x=0,y=0,width=150,height=100)

        log_frame=Frame(self.root,bd=2,bg="white")
        log_frame.place(x=600,y=200,width=400,height=400)

        img_logo=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\LoginIconAppl.png")
        img_logo=img_logo.resize((80,80),Image.LANCZOS)
        self.photoimg_logo=ImageTk.PhotoImage(img_logo)

        f_lbl=Label(log_frame,image=self.photoimg_logo)
        f_lbl.place(x=150,y=5,width=80,height=80)

        logo_label=Label(log_frame,text="Get Started",font=("times new roman",20,"bold"),fg="black",bg="white").place(x=122,y=90)

        user_logo=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\LoginIconAppl.png")
        user_logo=user_logo.resize((20,20),Image.LANCZOS)
        self.photouser_logo=ImageTk.PhotoImage(user_logo)

        f_lbl=Label(log_frame,image=self.photouser_logo)
        f_lbl.place(x=40,y=140,width=20,height=20)

        user_label=Label(log_frame,text="Username",font=("times new roman",12,"bold"),fg="black",bg="white").place(x=75,y=140)

        self.user_entry=ttk.Entry(log_frame,width=50)
        self.user_entry.place(x=40, y=170)
 

        pass_logo=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\lock-512.png")
        pass_logo=pass_logo.resize((20,20),Image.LANCZOS)
        self.photopass_logo=ImageTk.PhotoImage(pass_logo)

        f_lbl=Label(log_frame,image=self.photopass_logo)
        f_lbl.place(x=40,y=200,width=20,height=20)

        pass_label=Label(log_frame,text="Password",font=("times new roman",12,"bold"),fg="black",bg="white").place(x=75,y=200)

        self.pass_entry = ttk.Entry(log_frame, width=50,show="*")
        self.pass_entry.place(x=40, y=230)


    #login button
        login_btn=Button(log_frame,text="Login",relief=RAISED,command=self.login,cursor="hand2",font=("times new roman",10),bg="red",fg="black").place(x=150,y=280,width=120,height=35)

    #registerbutton
        registerbtn=Button(log_frame,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",command=self.register_win)
        registerbtn.place(x=15,y=320,width=160)

    #forgetbutton
        forgetbtn=Button(log_frame,text="Forget password",font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",command=self.forget_password_window)
        forgetbtn.place(x=10,y=340,width=160)

    def login(self):
        if self.user_entry.get()==""or self.pass_entry.get()=="":
            messagebox.showerror("Error","All field required")
        elif self.user_entry.get()=="kapu" and self.pass_entry.get()=="ashu":
            messagebox.showinfo("Success","welcome")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@0108madhav",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(self.user_entry.get(),self.pass_entry.get()))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username or password")
            else:
                open_main=messagebox.askyesno("Ask","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_recongnition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def reset_pass(self):
        if self.security_que_combo.get()=="Select":
            messagebox.showerror("Error","Please Select Security Question",parent=self.root2)
        elif self.security_ans_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer of security question",parent=self.root2)
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@0108madhav",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityque=%s and securityans=%s")
            value=(self.user_entry.get(),self.security_que_combo.get(),self.security_ans_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_pass_entry.get(),self.user_entry.get())
                my_cursor.execute(query,value)
            conn.commit()
            conn.close()
            messagebox.showinfo("Info","Your password has been reset",parent=self.root2)
            self.root2.destroy()



    def forget_password_window(self):
        if self.user_entry.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="@0108madhav",database="face_recognition")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.user_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.config(bg="white")

                l=Label(self.root2,text="Forget password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_que_label=Label(self.root2,text="Select Security Question.",bg="white",font=("times new roman",15,"bold"))
                security_que_label.place(x=50,y=80)

                self.security_que_combo=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),width=30,state="readonly")
                self.security_que_combo['values']=("Select" ," What is your birth date?","What is your favouraite month?","What is your favouraite place?","What is your favouraite food?")
                self.security_que_combo.current(0)
                self.security_que_combo. place(x=50,y=120,width=250)

                #Security answer label-
                security_ans_label=Label(self.root2,text="Security Answer",bg="white",font=("times new roman",15,"bold"))
                security_ans_label.place(x=50,y=160)

                self.security_ans_entry=ttk.Entry(self.root2,width=30,font=("times new roman",13,"bold"))
                self.security_ans_entry.place(x=50,y=210,width=250)

                new_pass_label=Label(self.root2,text="New Password",bg="white",font=("times new roman",15,"bold"))
                new_pass_label.place(x=50,y=240)

                self.new_pass_entry=ttk.Entry(self.root2,width=30,font=("times new roman",13,"bold"))
                self.new_pass_entry.place(x=50,y=280,width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green",cursor="hand2",command=self.reset_pass)
                btn.place(x=130,y=330,width=90)


    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()