from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql
import mysql.connector
import mysql.connector.plugins
def Fetch(root2):
    root2.destroy()
    root = Tk()
    root.title('Fetch Details')
    root.geometry('600x600')
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
    l4 = Label(root, text='History', padx=5, pady=5)
    l4.place(x=150, y=290)
    l5= Label(root, text='Date', padx=5, pady=5)
    l5.place(x=150, y=330)

    t1 = Entry(root)
    t1.place(x=225, y=200)
    t2 = Entry(root)
    t2.place(x=225, y=230)
    t3 = Entry(root, bg="white", width=25)
    t3.place(x=225, y=265)
    t4= Entry(root,bg="white",width=25)
    t4.place(x=225,y=300)
    t5 = Entry(root, bg="white", width=25)
    t5.place(x=225, y=330)

    def QUERY(t1, t2, t3, t4, t5, t,Btn):
        Btn.destroy()
        l=[]
        Id = t.get()
        print(Id)
        mysqldb = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="1234",
                                          database="Endodontics")
        mycursor = mysqldb.cursor()
        try:
            mycursor.execute('SELECT * from Endodontics WHERE PatientId="{}"'.format(Id))
            query=mycursor.fetchone()
            for i in query:
                l.append(i)
            print(l)
            t1.insert(0,l[1])
            t2.insert(0,l[2])
            t3.insert(0,l[3])
            t4.insert(0,l[4])
            t5.insert(0,l[5])

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
    def Remove(Btn1,t,t1,t2,t3,t4,t5):
        Btn1.destroy
        t.delete(0, tk.END)
        t1.delete(0,tk.END)
        t2.delete(0, tk.END)
        t3.delete(0, tk.END)
        t4.delete(0, tk.END)
        t5.delete(0, tk.END)

        Btn = Button(root, text="Fetch Data", command=lambda: QUERY(t1, t2, t3, t4, t5, t, Btn))
        Btn.place(x=200, y=100)
        Btn=Button(root,text="Fetch Data",command=lambda:QUERY(t1,t2,t3,t4,t5,t,Btn))
        Btn.place(x=200,y=100)
        btn=Button(root,text="Back",command=lambda:Menu(root))
        btn.place(x=0,y=0)


    root.mainloop()
