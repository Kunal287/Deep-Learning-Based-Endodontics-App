
from random import randrange
from tkinter import messagebox
import mysql
import mysql.connector
import mysql.connector.plugins
import PIL
import cv2
import os

import tensorflow
from keras.models import load_model
import numpy as np
import tensorflow as tf
from tkinter import *
from tkinter import filedialog
import os
from datetime import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from Database import *

def Menu(root1):
    root1.destroy()
    root2=Tk()
    # defining attribute of our frame
    root2.title('Patient Details')
    height=300
    width=300
    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root2.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root2.resizable(width=False, height=False)
    root2.title("Menu")
    root2.eval('tk::PlaceWindow . center')
    # Creating Menu options
    Button(root2, text='Fetch Patient Data',command=lambda:Fetch(root2)).place(x=100, y=50)
    Button(root2, text='Remove Patient Data').place(x=100, y=100)
    Button(root2, text='Predict Xray',command=lambda:FRAME(root2)).place(x=100, y=150)
    Button(root2, text='Modify Patient Data').place(x=100, y=200)
    Button(root2,text='Detect Carries',command=lambda:Caries_Detection(root2)).place(x=100,y=250)
    Button(root2, text='Exit').place(x=100, y=300)

    root2.configure(bg="#AFEEEE")
    root2.mainloop()
def Fetch(root2):
    root2.destroy()
    root = Tk()
    root.title('Fetch Details')
    height = 600
    width = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(width=False, height=False)
    l=Label(root,text='Patient Id').place(x=100,y=50)
    t=Entry(root)
    t.place(x=200,y=50)


    l1 = Label(root, text='Name', padx=5, pady=5)
    l1.place(x=150, y=200)

    l2 = Label(root, text='Phone', padx=5, pady=5)
    l2.place(x=150, y=230)
    l3 = Label(root, text='Oral Disease', padx=5, pady=5)
    l3.place(x=150, y=260)
    l4 = Label(root, text='Caries', padx=5, pady=5)
    l4.place(x=150, y=290)
    l5 = Label(root, text='History', padx=5, pady=5)
    l5.place(x=150, y=310)
    l6= Label(root, text='Date', padx=5, pady=5)
    l6.place(x=150, y=340)

    t1 = Entry(root)
    t1.place(x=225, y=200)
    t2 = Entry(root)
    t2.place(x=225, y=230)
    t3 = Entry(root, bg="white", width=25)
    t3.place(x=225, y=265)
    t4= Entry(root,bg="white",width=25)
    t4.place(x=225,y=290)
    t5 = Entry(root, bg="white", width=25)
    t5.place(x=225, y=310)
    t6 = Entry(root, bg="white", width=25)
    t6.place(x=225, y=310)

    def QUERY(t1, t2, t3, t4, t5,t6, t,Btn):
        Btn.destroy()
        l=[]
        Id = t.get()
        print(Id)
        mysqldb = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="1234",
                                          database="Endodontics")
        mycursor = mysqldb.cursor()
        try:
            mycursor.execute('SELECT * from PatientDetails WHERE PatientendodonticsId="{}"'.format(Id))
            query=mycursor.fetchone()
            for i in query:
                l.append(i)
            print(l)
            t1.insert(0,l[1])
            t2.insert(0,l[2])
            t3.insert(0,l[3])
            t4.insert(0,l[4])
            t5.insert(0,l[5])
            t6.insert(0,l[6])
            mysqldb.commit()
            messagebox.showinfo("Fetched Success", "Records Fetched Successfully")
        except ConnectionError:
            messagebox.showerror("Connection Lost", "Check Your Connection and Try again")
            mysqldb.rollback()
            mysqldb.close()
        except Exception as e:
            print(e)
            mysqldb.rollback()
            mysqldb.close()
        Btn1=Button(root,text="Clear",command=lambda:Remove(Btn1,t,t1,t2,t3,t4,t5))
        Btn1.place(x=200, y=100)
    def Remove(Btn1,t,t1,t2,t3,t4,t5,t6):
        Btn1.destroy
        t.delete(0, tk.END)
        t1.delete(0,tk.END)
        t2.delete(0, tk.END)
        t3.delete(0, tk.END)
        t4.delete(0, tk.END)
        t5.delete(0, tk.END)
        t6.delete(0,tk.END)
        Btn = Button(root, text="Fetch Data", command=lambda: QUERY(t1, t2, t3, t4, t5,t6, t, Btn))
        Btn.place(x=200, y=100)
    Btn=Button(root,text="Fetch Data",command=lambda:QUERY(t1,t2,t3,t4,t5,t6,t,Btn))
    Btn.place(x=200,y=100)
    btn=Button(root,text="Back",command=lambda:Menu(root))
    btn.place(x=250,y=200)


    root.mainloop()

count = 0

def FRAME(root2):
    # defining frame attributes
    root2.destroy()
    root= Tk()
    lbl=Label(root)
    frm=Frame(root)
    frm.pack(side=BOTTOM,padx=15,pady=15)
    # this function will be responsible for uploading the image from the system
    def showimage():
       global count
       count=count+1
       fln = filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=(("JPG File",".jpg"),("PNG file",".png"),("All Files",".")))
       #open the image selected from the directory
       img=PIL.Image.open(fln)
       img.thumbnail((350,350))
       photo=ImageTk.PhotoImage(img)
       #creating Labels
       lbl=Label(image=photo)
       lbl.configure(image=photo)
       lbl.image = photo
       lbl.place(x=300,y=140)
       # Enabling and Disabling the button
       if btn["state"] == NORMAL:
           btn["state"] = DISABLED
       else:
           btn["state"] = NORMAL
       #Here we will first read the Image
       image = cv2.imread(fln)
       # Getting the height and width of the input image
       height, width = image.shape[:2]
       font = cv2.FONT_HERSHEY_COMPLEX_SMALL
       # Converting Color image to Gray Scale Image
       Img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
       # Resize the Image
       Img = cv2.resize(Img, (224, 224), interpolation=cv2.INTER_CUBIC)
       Img1 = Img.astype('float32') / 255.
       Img1 = Img1.reshape(-1, 224, 224, 1)
       # Creating Buttons to Predict and Remove the Image
       btn2 = Button(frm, text="Predict", command=lambda: Predict(Img1,btn2,lbl,btn4))
       btn2.pack(side=tk.LEFT, padx=10)
       btn4 = Button(frm, text="Remove Image", command=lambda: Remove(lbl, btn2, btn4))
       btn4.pack(side=tk.LEFT, padx=10)


    def Remove(*args):
          for i in args:
              i.destroy()

          if btn["state"] == NORMAL:
              btn["state"] = DISABLED
          else:
              btn["state"] = NORMAL


    def Predict(Img1,btn2,lbll,btn4):
       btn4.destroy()
       btn2.destroy()
       score=0
       # Giving the path of our model
       model = tf.keras.models.load_model("models/NumberOfRoots.h5")
       Tpred = model.predict(Img1)
       Tpred= Tpred.argmax(axis=1)
       btn3 = Button(frm, text="Detect_Caries", command=lambda: Caries_Detection(lbl,root))
       btn3.pack(side=tk.LEFT, padx=10)
       # Checking whether tooth is Single root or multiroot
       if(Tpred==0).any():
           lbl= 'Multiple Roots'
           lbl2 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"),bg="WHITE",fg="RED")
           lbl2.place(x=120, y=350)
       else:
           lbl = 'Single Roots'
           lbl2 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="GREEN")
           lbl2.place(x=120, y=350)
           score = 60
       # Giving the path of our model
       model1 = tf.keras.models.load_model("models/Main.h5")
       Tpred1 = model1.predict(Img1)
       Tpred1 = Tpred1.argmax(axis=1)
       # Labeling the image according to  given Conditons
       if (Tpred1 == 0):
            lbl = 'Abscess'
            lbl4 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"))
            lbl4.place(x=120, y=390)
            lbl10= Label(root, text="Can Commit this case", font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="GREEN")
            lbl10.place(x=100, y=510)
            lbl6 = Label(root, text='Normal', font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="GREEN")
            lbl6.place(x=120, y=430)
            # giving score to determine the difficulty of he case
            val=str(randrange(85.00,96.00))
            lbl8 = Label(root, text=val+"%", font=("Comic Sans MS", 15, "bold"))
            lbl8.place(x=120, y=470)
       elif (Tpred1 == 1):
          lbl = 'Broken File'
          lbl4 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"))
          lbl4.place(x=120, y=390)
          lbl10 = Label(root, text="Refer this case to Endodontist", font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="RED")
          lbl10.place(x=100, y=510)
          lbl6 = Label(root, text='Hard', font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="ORANGE")
          lbl6.place(x=120, y=430)
          val=str(randrange(75.00,86.00))
          lbl8 = Label(root, text=val+"%", font=("Comic Sans MS", 15, "bold"))
          lbl8.place(x=120, y=470)


       elif (Tpred1 == 2):
          lbl = 'Curved Roots'
          lbl4 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"))
          lbl4.place(x=120, y=390)
          lbl10 = Label(root, text="Refer this case to Endodontist", font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="RED")
          lbl10.place(x=100, y=510)
          lbl6 = Label(root, text='Hard', font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="ORANGE")
          lbl6.place(x=120, y=430)
          val = str(randrange(65.00,76.00))
          lbl8 = Label(root, text=val+"%", font=("Comic Sans MS", 15, "bold"))
          lbl8.place(x=120, y=470)


       else:
            lbl = 'Radix Entomolaries'
            lbl4 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"))
            lbl4.place(x=120, y=390)
            lbl10 = Label(root, text="Refer this case to Endodontist", font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="RED")
            lbl10.place(x=100, y=510)
            lbl6 = Label(root, text='Very Hard', font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="RED")
            lbl6.place(x=120, y=430)
            val = str(randrange(65.00, 76.00))
            lbl8 = Label(root, text=val+"%", font=("Comic Sans MS", 15, "bold"))
            lbl8.place(x=120, y=470)


       btn6 = Button(frm, text="Clear all", command=lambda: Remove(lbll,lbl2, lbl4,lbl8, lbl6, lbl10,btn6,btn3))
       btn6.pack(side=tk.LEFT, padx=10)



    def Clear_all(*args):
      for i in args:
          i.destroy()

    img = ImageTk.PhotoImage(PIL.Image.open("Background_Image.jpg"))
    l = Label(image=img)
    l.pack()
    lbl=Label(root)
    lbl.pack()

    lbl1=Label(root,text='Roots:',font=("Comic Sans MS", 15, "bold"))
    lbl1.place(x=0,y=350)

    lbl2=Label(root,text='........',font=("Comic Sans MS", 19, "bold"))
    lbl2.place(x=120,y=350)


    lbl3 =Label(root,text="result:",font=("Comic Sans MS", 15, "bold"))
    lbl3.place(x=0,y=390)

    lbl4=Label(root,text='.........',font=("Comic Sans MS", 15, "bold"))
    lbl4.place(x=120,y=390)

    lbl5 =Label(root,text="Difficulty:",font=("Comic Sans MS", 15, "bold"))
    lbl5.place(x=0,y=430)

    lbl6=Label(root,text='......',font=("Comic Sans MS", 15, "bold"))
    lbl6.place(x=120,y=430)

    lbl7 =Label(root,text="Success %:",font=("Comic Sans MS", 15, "bold"))
    lbl7.place(x=0,y=470)

    lbl8=Label(root,text='.....',font=("Comic Sans MS", 15, "bold"))
    lbl8.place(x=120,y=470)

    lbl9 =Label(root,text="Verdict:",font=("Comic Sans MS", 15, "bold"))
    lbl9.place(x=0,y=510)

    lbl10=Label(root,text='.........',font=("Comic Sans MS", 15, "bold"))
    lbl10.place(x=120,y=510)



    btn = Button(frm, text="Browse Image",command=showimage)
    btn.pack(side=tk.LEFT)


    btn3 = Button(frm, text="EXIT",command=lambda: exit())
    btn3.pack(side=tk.LEFT,padx=10)
    btn5=  Button(frm, text="BACK",command=lambda: Menu(root))
    btn5.pack(side=tk.LEFT, padx=10)

    root.title("Endodentics")
    root.resizable(width=False, height=False)
    height = 600
    width = 675
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    #root.geometry("675x600")


    root.mainloop()
Disease = ""


def CreateForm(lbl0,lbl, root):
    root.destroy()
    print(lbl)
    ws = Tk()
    ws.title('Patient Details')
    height = 500
    width = 500
    screen_width = ws.winfo_screenwidth()
    screen_height = ws.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    ws.geometry('%dx%d+%d+%d' % (width, height, x, y))
    ws.resizable(width=False, height=False)
    l1 = Label(ws, text='Name', padx=5, pady=5,bg="#AFEEEE")
    l1.place(x=100, y=100)
    l2 = Label(ws, text='Phone', padx=5, pady=5,bg="#AFEEEE")
    l2.place(x=100, y=130)
    l3 = Label(ws, text='Oral Disease', padx=5, pady=5,bg="#AFEEEE")
    l3.place(x=100, y=160)
    l4=Label(ws,text='Caries',padx=5,pady=5,bg="#AFEEEE")
    l4.place(x=100, y=190)
    l5 = Label(ws, text='Date', padx=5, pady=5,bg="#AFEEEE")
    l5.place(x=100, y=210)
    name = StringVar
    phone = StringVar
    t1 = Entry(ws)
    t1.place(x=180, y=100)
    t2 = Entry(ws)
    t2.place(x=180, y=130)
    t3 = Entry(ws, bg="white", width=25)
    t3.insert(0, lbl)
    t3.place(x=180, y=160)
    t3.configure(state="readonly")
    t4 = Entry(ws)
    t4.insert(0,lbl0)
    t4.place(x=180, y=195)
    t4.configure(state="readonly")
    print(t3.get())
    t5 = Entry(ws, bg="white", width=25)
    dt = datetime.now()
    t5.insert(0, dt)
    t5.place(x=180, y=230)
    t5.configure(state="readonly")
    print(t5.get())
    l5 = Label(ws, text='Patient History:', padx=5, pady=5,bg="#AFEEEE")
    l5.place(x=100, y=260)

    def Select():
        global Disease
        Disease = var.get()
        if (Disease == 1):
            Disease = 'Diabetes'
        elif (Disease == 2):
            Disease = 'Cancer'
        elif (Disease == 3):
            Disease = 'Asthama'
        elif (Disease == 4):
            Disease = 'Heart Disease'
        else:
            Disease = 'NA'

    var = IntVar(ws)
    Radiobutton(ws, text="Diabetes", variable=var, value=1,
                command=Select,bg="#AFEEEE").place(x=100, y=260)

    Radiobutton(ws, text="Cancer", variable=var, value=2,
                command=Select,bg="#AFEEEE").place(x=170, y=260)

    Radiobutton(ws, text="Asthama", variable=var, value=3,
                command=Select,bg="#AFEEEE").place(x=240, y=260)
    Radiobutton(ws, text="Heart Disease", variable=var, value=4,
                command=Select,bg="#AFEEEE").place(x=310, y=260)

    R5 = Radiobutton(ws, text="NA", variable=var, value=5,
                     command=Select,bg="#AFEEEE").place(x=410, y=260)
    Button(ws, text='Submit', command=lambda: Save(t1, t2, t3, t4, Disease)).place(x=270, y=290)
    btn3 = Button(ws, text="EXIT", command=lambda: exit())
    btn3.place(x=200,y=290)
    btn4 = Button(ws, text="BACK", command=lambda: FRAME(ws))
    btn4.place(x=200, y=290)
    def Save(t1, t2, t3, t4, Disease):
        print(Disease)
        Name = t1.get()
        Phone = t2.get()
        Oral_Disease = t4.get()
        Caries=t3.get()
        Date = t5.get()

        if (len(Name) == 0 or len(Phone) == 0 or len(Oral_Disease) == 0 or len(Date) == 0 or len(Disease) == 0 or len(Caries) == 0):

            messagebox.showwarning("showwarning", "Please Enter All Details")
        else:
            if (len(Phone) == 10):
                Update(Name, Phone, Oral_Disease,Caries, Disease, Date)
            else:
                messagebox.showwarning("showwarning", "Enter Correct Phone number")

    ws.configure(bg="#AFEEEE")
    ws.mainloop()

def Caries_Detection(lbl0,root2):
    root2.destroy()
    root = Tk()
    lbl = Label(root)
    frm = Frame(root)
    frm.pack(side=BOTTOM, padx=15, pady=15)

    # this function will be responsible for uploading the image from the system
    def selectimage():

        fln = filedialog.askopenfilename(initialdir=os.getcwd(),
                                         filetypes=(("JPG File", ".jpg"), ("PNG file", ".png"), ("All Files", ".")))
        # open the image selected from the directory
        img = PIL.Image.open(fln)
        img.thumbnail((350, 350))
        photo = ImageTk.PhotoImage(img)
        # creating Labels
        lbl = Label(image=photo)
        lbl.configure(image=photo)
        lbl.image = photo
        lbl.place(x=300, y=140)
        image = cv2.imread(fln)
        # Getting the height and width of the input image
        height, width = image.shape[:2]
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        # Converting Color image to Gray Scale Image
        Img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Resize the Image
        Img = cv2.resize(Img, (224, 224), interpolation=cv2.INTER_CUBIC)
        Img1 = Img.astype('float32') / 255.
        Img1 = Img1.reshape(-1, 224, 224, 1)
        # Creating Buttons to Predict and Remove the Image
        btn2 = Button(frm, text="Predict", command=lambda:PredictCaries(Img1))
        btn2.pack(side=tk.LEFT, padx=10)
        btn4 = Button(frm, text="Remove Image", command=lambda: Remove(lbl, btn2, btn4))
        btn4.pack(side=tk.LEFT, padx=10)

    def Remove(*args):
        for i in args:
            i.destroy()

        if btn["state"] == NORMAL:
            btn["state"] = DISABLED
        else:
            btn["state"] = NORMAL

    def PredictCaries(Img1):
        # Giving the path of our model
        model = tensorflow.keras.models.load_model("models/Caries_Detection.h5",compile=False)
        Tpred = model.predict(Img1)
        Tpred = Tpred.argmax(axis=1)
        btn3 = Button(frm, text="Fill Details", command=lambda: CreateForm(lbl0,lbl, root))
        btn3.pack(side=tk.LEFT, padx=10)
        # Checking whether tooth is Single root or multiroot
        if (Tpred.any() == 0):
            lbl = 'Caries'
            lbl2 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="RED")
            lbl2.place(x=120, y=350)
        else:
            lbl = 'No-Caries'
            lbl2 = Label(root, text=lbl, font=("Comic Sans MS", 15, "bold"), bg="WHITE", fg="GREEN")
            lbl2.place(x=120, y=350)
            score = 60

    def Clear_all(*args):
        for i in args:
            i.destroy()
    img = ImageTk.PhotoImage(PIL.Image.open("Background_Image.jpg"))
    l = Label(image=img)
    l.pack()
    lbl = Label(root)
    lbl.pack()
    lbl1 = Label(root, text='Caries:', font=("Comic Sans MS", 15, "bold"))
    lbl1.place(x=0, y=350)

    lbl2 = Label(root, text='........', font=("Comic Sans MS", 19, "bold"))
    lbl2.place(x=120, y=350)

    root.title("Endodentics")
    root.resizable(width=False, height=False)
    height = 600
    width = 675
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # root.geometry("675x600")
    btn = Button(frm, text="Browse Image", command=selectimage)
    btn.pack(side=tk.LEFT)

    btn3 = Button(frm, text="EXIT", command=lambda: exit())
    btn3.pack(side=tk.LEFT, padx=10)
    btn5 = Button(frm, text="BACK", command=lambda: Menu(root))
    btn5.pack(side=tk.LEFT, padx=10)
    root.mainloop()