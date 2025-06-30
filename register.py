from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
 

class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        #********************variables************************************
        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_que=StringVar()
        self.var_security_ans=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()

    #=========================set color============================
        self.root.config(bg="pink")
    
    #======================title==================================
        title_lbl=Label(self.root,text="NEW REGISTERATION ",font=("times new roman",25,"bold"),fg="white",bg="black")
        title_lbl.place(x=0,y=0,width=1530,height=55)

    #===============================image=========================    
        img=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\nik-z1d-LP8sjuI-unsplash (1).jpg")
        img=img.resize((500,600),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=100,y=100,width=500,height=600)

    #====================Frame======================================
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=600,y=100,width=750,height=600)

        title_lbl=Label(main_frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="navy blue",bg="white")
        title_lbl.grid(row=0,column=1,padx=50,pady=20,sticky=W)


        #First name label-
        first_label=Label(main_frame,text="First Name",bg="white",font=("times new roman",15,"bold"))
        first_label.grid(row=1,column=1,padx=50,pady=10,sticky=W)

        first_entry=ttk.Entry(main_frame,textvariable=self.var_first_name,width=30,font=("times new roman",13,"bold"))
        first_entry.grid(row=2,column=1,padx=50,sticky=W)

        #First name label-
        last_label=Label(main_frame,text="Last Name",bg="white",font=("times new roman",15,"bold"))
        last_label.grid(row=1,column=3,padx=50,pady=10,sticky=W)

        last_entry=ttk.Entry(main_frame,textvariable=self.var_last_name,width=30,font=("times new roman",13,"bold"))
        last_entry.grid(row=2,column=3,padx=50,sticky=W)

        #contact no. label-
        contact_label=Label(main_frame,text="Contact No.",bg="white",font=("times new roman",15,"bold"))
        contact_label.grid(row=3,column=1,padx=50,pady=10,sticky=W)

        contact_entry=ttk.Entry(main_frame,textvariable=self.var_contact,width=30,font=("times new roman",13,"bold"))
        contact_entry.grid(row=4,column=1,padx=50,sticky=W)

        #Email label-
        email_label=Label(main_frame,text="Email",bg="white",font=("times new roman",15,"bold"))
        email_label.grid(row=3,column=3,padx=50,pady=10,sticky=W)

        email_entry=ttk.Entry(main_frame,textvariable=self.var_email,width=30,font=("times new roman",13,"bold"))
        email_entry.grid(row=4,column=3,padx=50,sticky=W)

        #security question label-
        security_que_label=Label(main_frame,text="Select Security Question.",bg="white",font=("times new roman",15,"bold"))
        security_que_label.grid(row=5,column=1,padx=50,pady=10,sticky=W)

        security_que_combo=ttk.Combobox(main_frame,textvariable=self.var_security_que,font=("times new roman",12,"bold"),width=30,state="readonly")
        security_que_combo['values']=("Select" ,"What is your birth date?","What is your favouraite month?","What is your favouraite place?","What is your favouraite food?")
        security_que_combo.current(0)
        security_que_combo.grid(row=6,column=1,padx=50,sticky=W)

        #Security answer label-
        security_ans_label=Label(main_frame,text="Security Answer",bg="white",font=("times new roman",15,"bold"))
        security_ans_label.grid(row=5,column=3,padx=50,pady=10,sticky=W)

        security_ans_entry=ttk.Entry(main_frame,textvariable=self.var_security_ans,width=30,font=("times new roman",13,"bold"))
        security_ans_entry.grid(row=6,column=3,padx=50,sticky=W)

        #password label-
        password_label=Label(main_frame,text="Password",bg="white",font=("times new roman",15,"bold"))
        password_label.grid(row=7,column=1,padx=50,pady=10,sticky=W)

        password_entry=ttk.Entry(main_frame,textvariable=self.var_password,width=30,font=("times new roman",13,"bold"))
        password_entry.grid(row=8,column=1,padx=50,sticky=W)

        #confirm password label-
        confirm_pass_label=Label(main_frame,text="Confirm Password",bg="white",font=("times new roman",15,"bold"))
        confirm_pass_label.grid(row=7,column=3,padx=50,pady=10,sticky=W)

        confirm_pass_entry=ttk.Entry(main_frame,textvariable=self.var_confirm_password,width=30,font=("times new roman",13,"bold"))
        confirm_pass_entry.grid(row=8,column=3,padx=50,sticky=W)

        #checkbox of terms and conditions--
        self.var_check=IntVar()
        Checkbutton(main_frame,text="Agree to the terms and conditions",variable=self.var_check,bg="white",font=("times new roman",15,"bold")).grid(row=9,column=1,padx=10)

        reg_btn=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\register-now-button1.jpg")
        reg_btn=reg_btn.resize((200,50),Image.LANCZOS)
        self.photo_reg_btn=ImageTk.PhotoImage(reg_btn)

        f_btn=Button(main_frame,image=self.photo_reg_btn,borderwidth=0,cursor="hand2",command=self.register_data)
        f_btn.place(x=60,y=430,width=200,height=50)

        log_btn=Image.open(r"C:\\Users\\Giriraj\\OneDrive\Desktop\\face recongnition system.py\\college_images\\loginpng.png")
        log_btn=log_btn.resize((200,40),Image.LANCZOS)
        self.photo_log_btn=ImageTk.PhotoImage(log_btn)

        f_btn=Button(main_frame,image=self.photo_log_btn,borderwidth=0,cursor="hand2",command=self.login_now)
        f_btn.place(x=300,y=435,width=200,height=40)


    #====================Function declaration=============================

    def login_now(self):
        self.root.destroy()

    def register_data(self):
        if self.var_first_name.get()=="" or self.var_password.get()==""or self.var_security_que.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","please agree terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",     password="@0108madhav",database="face_recognition")
            my_cursor=conn.cursor()

            query=("select * from register where email=%s")
            values=(self.var_email.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist")
            else:
                my_cursor.execute("""
    INSERT INTO register 
    (fname, lname, contact, email, securityque, securityans, password) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (
    self.var_first_name.get(),
    self.var_last_name.get(),
    self.var_contact.get(),
    self.var_email.get(),
    self.var_security_que.get(),
    self.var_security_ans.get(),
    self.var_password.get()
))

            conn.commit()
            conn.close()

            messagebox.showinfo("Success","Register successfully",parent=self.root)
    
 
 
if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
