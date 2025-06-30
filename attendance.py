from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import csv
import cv2
import os
from tkinter import filedialog
 
global Idr
mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")
    
    #***************text  variables************************
        self.var_atten_id=StringVar()
        self.var_roll=StringVar()
        self.var_atten_status=StringVar()
        self.var_date=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_name=StringVar()


    # first image on top-- 
        img=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\smart-attendance.jpg")
        img=img.resize((770,180),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=770,height=180)

    #second image on top--
        img1=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\AdobeStock_303989091.jpeg")
        img1=img1.resize((780,180),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=771,y=0,width=780,height=180)

        title=Label(self.root,text=" ATTENDANCE MANAGMENT SYSTEM",relief=SUNKEN,bg="black",fg="yellow",font=("times new roman",28,"bold"))
        title.place(x=0,y=181,width=1530,height=45)

    #main frame--
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=20,y=227,width=1480,height=550)   
    
    #left label frame--
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=    ("times new roman",15,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=530)

    #Img in left frame--
        img_left_frame=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\hqdefault.jpg")
        img_left_frame=img_left_frame.resize((680,180),Image.LANCZOS)
        self.photoimg_left_frame=ImageTk.PhotoImage(img_left_frame)

        f_lbl=Label(Left_frame,image=self.photoimg_left_frame)
        f_lbl.place(x=5,y=0,width=680,height=180)

        left_inside_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        left_inside_frame.place(x=10,y=195,width=680,height=310)

    #left inside frame labels and entry---
    
        #attendance id label-
        attendance_id_label=Label(left_inside_frame,bg="white",text="Attendance ID",font=("times new roman",12,"bold"))
        attendance_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendance_id_entry=ttk.Entry(left_inside_frame ,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        attendance_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # department label-
        dep_label=Label(left_inside_frame,bg="white",text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame ,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #attendance status label-
        attendance_status_label=Label(left_inside_frame,bg="white",text="Attendance Status",font=("times new roman",12,"bold"))
        attendance_status_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        
        div_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_status,font=("times new roman",12,"bold"),width=20,state="readonly")
        div_combo['values']=("Select Status","Present","Absent")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Name label-
        Name_label=Label(left_inside_frame,bg="white",text="Name",font=("times new roman",12,"bold"))
        Name_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame ,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        Name_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Date label-
        date_label=Label(left_inside_frame,bg="white",text="Date",font=("times new roman",12,"bold"))
        date_label.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame ,textvariable=self.var_date,width=20,font=("times new roman",13,"bold"))
        date_entry.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        #Roll label-
        roll_label=Label(left_inside_frame,bg="white",text="Roll",font=("times new roman",12,"bold"))
        roll_label.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame ,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=4,padx=10,pady=5,sticky=W)

        #Time label-
        time_label=Label(left_inside_frame,bg="white",text="Time",font=("times new roman",12,"bold"))
        time_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame ,textvariable=self.var_time,width=20,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=4,padx=10,pady=5,sticky=W)

        def get_input():
            Id=attendance_id_entry.get()
            return Id


        #Buttons frame--
      
        btn_frame=Frame( left_inside_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=0,y=240,width=680,height=35)

        Import_btn=Button(btn_frame,text="Import csv",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white",command=self.import_csv )
        Import_btn.grid(row=0,column=0)

        Export_btn=Button(btn_frame,text="Export csv",command=self.export_csv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white" )
        Export_btn.grid(row=0,column=1)

        Update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white" )
        Update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=21,font=("times new roman",13,"bold"),bg="blue",fg="white" ,command=self.reset)
        reset_btn.grid(row=0,column=3)




    #Right label frame--
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",15,"bold"))
        Right_frame.place(x=750,y=10,width=710,height=530)

        table_frame=Frame( Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=5,width=695,height=490)

        #***************scroll bar in table******************

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("Id","rollno","name","dep","time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("Id",text="Attendance ID")
        self.AttendanceReportTable.heading("rollno",text="ROll NO")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance Status ")

        self.AttendanceReportTable["show"]="headings"
    
        self.AttendanceReportTable.column("Id",width=100)
        self.AttendanceReportTable.column("rollno",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)
     

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>", lambda event: self.get_cursor())
        idr=get_input()


    #********************************fetch data*********************************
    def fetch_Data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


    #import csv  data-
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_Data(mydata) 


    #export csv data-

    def export_csv(self):
        try:
            if(len(mydata))<1:
                messagebox.showerror("No data","no data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV", filetypes=(("csv file","*.csv"),("All files","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Export data","your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as e:
            messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)

    #****************************reset button**********************************
    def reset(self):
        self.var_atten_id.set("")
        self.var_dep.set("")
        self.var_atten_status.set("")
        self.var_name.set("")
        self.var_date.set("")
        self.var_roll.set("")
        self.var_time.set("")



 
        


            
    def get_cursor(self):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]

        if rows:
            self.var_atten_id.set(rows[0])
            self.var_dep.set(rows[1])
            self.var_atten_status.set(rows[2])
            self.var_name.set(rows[3])
            self.var_date.set(rows[4])
            self.var_roll.set(rows[5])
            self.var_time.set(rows[6])
        else:
            messagebox.showerror("Error","No record selected",parent=self.root)
          


 




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
