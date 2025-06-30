from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import os
import numpy as np
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recongnition System")

        title=Label(self.root,text="Photo Sample Training",relief=SUNKEN,bg="white",fg="red",font=("times new roman",28,"bold"))
        title.place(x=0,y=0,width=1530,height=80)

        #top image--
        img=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\facialrecognition.png")
        img=img.resize((1530,300),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        img_lbl=Label(self.root,image=self.photoimg)
        img_lbl.place(x=0,y=81,width=1530,height=300)

    

        #button
        btn_1=Button(self.root,text="TRAIN DATA",bd=2,relief=RIDGE,bg="BLUE",fg="white" ,cursor="hand2",font=("times new roman",20,"bold"),command=self.train_classifier)
        btn_1.place(x=0,y=380,width=1530,height=60)

        img_bottom=Image.open("C:\\Users\\Giriraj\\OneDrive\\Desktop\\face recongnition system.py\\college_images\\new.jpg")
        img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            #print("hello")
        ids=np.array(ids)
        #print("ssssssssssssssssssssssss")

        #********************Train the classifier and save*****************    
        clf=cv2.face.LBPHFaceRecognizer_create()
        #print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!",parent=self.root)

    


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
