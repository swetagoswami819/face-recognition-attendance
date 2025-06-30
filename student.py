from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox
import mysql.connector
import cv2
import os
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        #*******************variables*************************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



    # first image on top-- 
        img=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\face-Recognition.png")
        img=img.resize((510,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        """f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)"""
        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2",command=self.open_img)
        self.btn_1.place(x=0,y=0,width=510,height=130)
        
    
    #second image on top--
        img1=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\smart-attendance.jpg")
        img1=img1.resize((510,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        """f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=511,y=0,width=510,height=130)"""
        self.btn_2=Button(self.root,image=self.photoimg1,cursor="hand2",command=self.open_img1)
        self.btn_2.place(x=511,y=0,width=510,height=130)


    #third image on top--
        img2=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\student3.jpg")
        img2=img2.resize((510,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        """f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1017,y=0,width=510,height=130)"""

        self.btn_3=Button(self.root,image=self.photoimg2,cursor="hand2",command=self.open_img2)
        self.btn_3.place(x=1017,y=0,width=510,height=130)

    #bg image--
        img3=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\wp2551980.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
    
    #title lable--
        title_lbl=Label(bg_img,text="STUDENT MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="hot pink")
        title_lbl.place(x=0,y=0,width=1530,height=45)   
    
    #main frame--
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)   
    
    #left label frame--
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=    ("times new roman",15,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=580)

    #Img in left frame--
        img_left_frame=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\AdobeStock_303989091.jpeg")
        img_left_frame=img_left_frame.resize((690,130),Image.LANCZOS)
        self.photoimg_left_frame=ImageTk.PhotoImage(img_left_frame)

        f_lbl=Label(Left_frame,image=self.photoimg_left_frame)
        f_lbl.place(x=5,y=0,width=690,height=130)

    #current course frame--
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
        Current_course_frame.place(x=5,y=135,width=690,height=115)
        
        #department label-
        dep_label=Label(Current_course_frame,bg="white",text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        #department combobox-
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo['values']=("Select Department","CSE","IT","Civil","Mechanical","EL=lectrical","AIML","ishara karate")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course label-
        course_label=Label(Current_course_frame,bg="white",text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        #Course combobox-
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo['values']=("Select Course" ,"B-Tech","M-tech","BCA","MCA","BBA","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year label-
        year_label=Label(Current_course_frame,bg="white",text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10)

        #Year combobox-
        year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo['values']=("Select Year" ,"2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        #Semester label-
        sem_label=Label(Current_course_frame,bg="white",text="Semester",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        #Semester combobox-
        sem_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        sem_combo['values']=("Select Semester" ,"I","II","III","IV","V","VI","VII","VIII")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=1,sticky=W)

    #class student frame--
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",15,"bold"))
        Class_Student_frame.place(x=5,y=250,width=690,height=300)
    
    #class student frame labels--
        
        #student id label-
        stud_id_label=Label(Class_Student_frame,bg="white",text="Student ID",font=("times new roman",12,"bold"))
        stud_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        stud_id_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        stud_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
         
    #student name label-
        stud_name_label=Label(Class_Student_frame,bg="white",text="Student Name",font=("times new roman",12,"bold"))
        stud_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        stud_name_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        stud_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class divison label-
        class_div_label=Label(Class_Student_frame,bg="white",text="Class Divison",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=20,state="readonly")
        div_combo['values']=("Select Divison","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        

        #Roll no label-
        Roll_no_label=Label(Class_Student_frame,bg="white",text="Roll No",font=("times new roman",12,"bold"))
        Roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Roll_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender label-
        Gender_label=Label(Class_Student_frame,bg="white",text="Gender",font=("times new roman",12,"bold"))
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="readonly")
        gender_combo['values']=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DOB label-
        DOB_label=Label(Class_Student_frame,bg="white",text="DOB",font=("times new roman",12,"bold"))
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email label-
        Email_label=Label(Class_Student_frame,bg="white",text="Email",font=("times new roman",12,"bold"))
        Email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no label-
        phone_no_label=Label(Class_Student_frame,bg="white",text="Phone No",font=("times new roman",12,"bold"))
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address label-
        Address_label=Label(Class_Student_frame,bg="white",text="Address",font=("times new roman",12,"bold"))
        Address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        Address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name label-
        Teacher_name_label=Label(Class_Student_frame,bg="white",text="Teacher Name",font=("times new roman",12,"bold"))
        Teacher_name_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        Teacher_name_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        Teacher_name_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons--
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radiobtn1.grid(row=5,column=0)
        
         
        radiobtn2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        radiobtn2.grid(row=5,column=1)

        #Buttons frame--
      
        btn_frame=Frame(Class_Student_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=200,width=680,height=70)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.add_data)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.update)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.delete)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=21,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.reset)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        Takephoto_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        Takephoto_btn.grid(row=1,column=0)

        updatephoto_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        updatephoto_btn.grid(row=1,column=1)

     
    #Right label frame--
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=750,y=10,width=710,height=580)

        #Img in right frame--
        img_right_frame=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\AdobeStock_303989091.jpeg")
        img_right_frame=img_right_frame.resize((690,130),Image.LANCZOS)
        self.photoimg_right_frame=ImageTk.PhotoImage(img_right_frame)

        f_lbl=Label(Right_frame,image=self.photoimg_right_frame)
        f_lbl.place(x=5,y=0,width=690,height=130)

        # **********Search System**********************
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Student information",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=700,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select Option","roll","phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        self.var_search=StringVar()
        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,command=self.search_data,text="Search",width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        show_all_btn=Button(search_frame,text="Show All",command=self.fetch_data,width=11,font=("times new roman",13,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)

        #********************table frame***************
        table_frame=Frame(Right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=700,height=340)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("div",text="Divison")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
      

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #****************Function Declaration****************************
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="@0108madhav",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("INSERT INTO student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.   var_semester.get(),self.var_std_id.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get()))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("save","Data added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self.root)

    #*********fetch_Data****************************************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="@0108madhav",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_table")
        data=my_cursor.fetchall()

        if(len(data)!=0):
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    #************************get cursor*******************************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
            
    
    #**************update*******************************
    def update(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                upadate=messagebox.askyesno("update","Do you want to update this dataset?",parent=self.root)
                if upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root",    password="@0108madhav",database="face_recognition")
                    my_cursor=conn.cursor()

                    
                    query = """UPDATE student_table SET dep=%s,course=%s,year=%s,semester=%s, stud_name=%s,stud_id=%s,divison=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s, address=%s,teacher=%s,photosample=%s WHERE stud_id=%s"""

               

                    values=(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_name.get(),self.var_std_id.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get())
                    
                    my_cursor.execute(query,values)
                
                else:
                    if not upadate:
                        return
                messagebox.showinfo("Success","Students details update successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error",f"Not update Due to : {str(e)}",parent=self.root)
    
    #**********************Delete function************************
    def delete(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","student Id must  be required",parent=self.root)
        else:
            try:
                deleted=messagebox.askyesno("delete","Do you want to delete this dataset?",parent=self.root)
                if deleted>0:
                    conn=mysql.connector.connect(host="localhost",user="root",    password="@0108madhav",database="face_recognition")
                    my_cursor=conn.cursor()
                    query="delete from student_table where stud_id=%s"
                    values=(self.var_std_id.get(),)
                    my_cursor.execute(query,values)
                else:
                    if not deleted:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delete data",parent=self.root)
            except Exception as e:
                messagebox.showerror("Delete",f"Due to : {str(e)}",parent=self.root)
    
    #**********************reset function**************************
    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Divison")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#***************************search data *********************************
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please select Option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",         password="@0108madhav",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_table where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+""
                "%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as e:
                print("Due to:"+f"Error:{e}")

                    
#***********************Generate dataset or take photo samples******************
    def generate_dataset(self):
       
        
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.  var_std_id.get()=="":
            messagebox.showerror("Error","ALl fields are required",parent=self.root)
        else:
            try:
                #print("connectiing to mysql")
                conn=mysql.connector.connect(host="localhost",user="root",     password="@0108madhav",database="face_recognition")
                my_cursor=conn.cursor()
                #print("connect mysql")
                my_cursor.execute("Select  * from student_table")
                myresult=my_cursor.fetchall()
                #print("records found")
                id=0
                for x in myresult:
                    id+=1
                    #print("generate id")
                    query = """UPDATE student_table SET dep=%s,course=%s,year=%s,semester=%s, stud_name=%s,divison=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s, address=%s,teacher=%s,photosample=%s WHERE stud_id=%s"""

                    values=(self.var_dep.get(),self.var_course.get(),self.var_year.get(),self. var_semester.get(),self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),self.var_dob.get(),self.var_email.get(),self. var_phone.get(),self.var_address.get(),self.var_teacher.get(),self.var_radio1.get(),self.var_std_id.get())
                    
                my_cursor.execute(query,values)
                conn.commit()
                #print("query execute successfully")
                self.fetch_data()
                self.reset()
                conn.close()
                #print("conn close successfully")
                    
                #*******load predefined data on face frontal from open cv**********
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                #if face_classifier.empty():
                    #print("Error: ofile no t ofsdksfjgdlapsfddvv loaded properp;y html xml")

                def face_cropped(img):
                    #print("1one")
                    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(grey,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                 
                 
                cap=cv2.VideoCapture(0)
                #print("2two")
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_cropped(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        #print("3three")
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!",parent=self.root)


            except Exception as e:
                messagebox.showerror("Delete",f"Due to : {str(e)}",parent=self.root)

    #*****************************change top photos***********************************
    def open_img(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img=Image.open(fln)
        img_browse=img.resize((510,130),Image.LANCZOS)
        self.photoimg_browse=ImageTk.PhotoImage(img_browse)
        self.btn_1.config(image=self.photoimg_browse)

    def open_img1(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img1=Image.open(fln)
        img_browse1=img1.resize((510,130),Image.LANCZOS)
        self.photoimg_browse1=ImageTk.PhotoImage(img_browse1)
        self.btn_2.config(image=self.photoimg_browse1)

    def open_img2(self):
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open Images",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
        img2=Image.open(fln)
        img_browse2=img2.resize((510,130),Image.LANCZOS)
        self.photoimg_browse2=ImageTk.PhotoImage(img_browse2)
        self.btn_3.config(image=self.photoimg_browse2)


    """def get_id():
        global idr
    
        idr=stud_id_entry.get()"""

   

                

                
                



        
        

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()