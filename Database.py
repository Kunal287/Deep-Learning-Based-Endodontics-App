import random
import string
from random import randrange

import mysql
import mysql.connector
import mysql.connector.plugins
from tkinter import messagebox



def Update(Name,Phone,Oral_Disease,Caries,Disease,Date):

    mysqldb= mysql.connector.connect(host="127.0.0.1",port=3306,user="root",passwd="1234",database="Endodontics")
    mycursor=mysqldb.cursor()
    str1="EN2022"
    for i in range(0,3,1):
        str1=str1+random.choice(string.ascii_uppercase)
    str2=str(randrange(1,100,1))
    PatientId=str1+str2
    print(PatientId)


    try:
        que="INSERT INTO PatientDetails (PatientendodonticsId,Name,Phone,Oral_Disease,Caries,History,Date) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val=(PatientId,Name,Phone,Oral_Disease,Caries,Disease,Date)
        mycursor.execute(que,val)
        mysqldb.commit()
        messagebox.showinfo("Insert Success", "Records Inserted Successfully")

    except ConnectionError:
        messagebox.showerror("Connection Lost", "Check Your Connection and Try again")
        mysqldb.rollback()
        mysqldb.close()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

