from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import cv2
from PIL import Image,ImageTk
import os
import mysql.connector
from student import Student
from time import strftime
from datetime import datetime

 

class Face_recognizer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        title=Label(self.root,text="Photo Sample Training",relief=SUNKEN,bg="white",fg="green",font=("times new roman",28,"bold"))
        title.place(x=0,y=0,width=1530,height=80)

        #left image--
        img=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\face_detector1.jpg")
        img=img.resize((780,650),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        img_lbl=Label(self.root,image=self.photoimg)
        img_lbl.place(x=0,y=81,width=780,height=650)

        #right image--
        img1=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img1=img1.resize((800,650),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        img_lbl1=Label(self.root,image=self.photoimg1)
        img_lbl1.place(x=781,y=81,width=800,height=650)

        #button
        btn_1=Button(img_lbl1,text="FACE RECOGNIZER",bd=2,relief=RIDGE,bg="green",fg="white" ,cursor="hand2",font=("times new roman",15,"bold"),padx=10,pady=5,command=self.face_recog)
        btn_1.place(x=300,y=550,width=200,height=40)

    
    #****************************attendance***********************************
    def mark_attendance(self,i,r,n,d):
        with open("sweta.csv","r+",newline="\n") as f:
            mydataList=f.readlines()
            name_list=[]
            for line in mydataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




        #**************face recognition************************************
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minneighbour,color,text,clf):
            grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(grey_img,scalefactor,minneighbour)

            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(grey_img[y:y+h,x:x+w])
                print(id)
                
                confidence=int((100*(1-predict/300)))

                  
                conn=mysql.connector.connect(host="localhost",user="root",password="@0108madhav",database="face_recognition")
                my_cursor=conn.cursor()
                
                
                my_cursor.execute("SELECT stud_name FROM student_table WHERE stud_id=%s",(id,))
                
                name=my_cursor.fetchone()
                
                #name="+".join(name)
                if name:
                    name=name[0]
                else:
                    name="unknown"

                my_cursor.execute("SELECT roll FROM student_table WHERE stud_id=%s", (id,))

                rollno=my_cursor.fetchone()
                #rollno="+".join(rollno)
                if rollno:
                    rollno=rollno[0]
                else:
                    rollno="unknown" 

                my_cursor.execute("SELECT dep FROM student_table WHERE stud_id=%s",(id,))
                dep=my_cursor.fetchone()
                #dep="+".join(dep)
                if dep:
                    dep=dep[0]
                else:
                    dep="unknown" 

                my_cursor.execute("SELECT  stud_id FROM student_table WHERE stud_id=%s",(id,))
                i=my_cursor.fetchone()
                #dep="+".join(dep)
                if i:
                    i=i[0]
                else:
                    i="unknown" 


                 
                if confidence>77:
                    cv2.putText(img,f"ID : {i}",(x,y-78),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    #print name on head
                    cv2.putText(img,f"Roll : {rollno}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Name : {name}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    cv2.putText(img,f"Department : {dep}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,rollno,name,dep)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
            return coord
            
        def recognize(img,clf,facecascade):
            coord=draw_boundary(img,facecascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,face_cascade)
            cv2.imshow("Welcome to face recognization",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                


if __name__ == "__main__":
    root=Tk()
    obj=Face_recognizer(root)
    root.mainloop()
 
