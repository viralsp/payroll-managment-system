from sqlite3 import Cursor
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  
import mysql.connector
from admin_homepage import*
from tkinter import messagebox


class emp_homepage():
    def __init__(self,id): 
        self.root=Tk()
        self.root.title("Employee Page")
        self.root.geometry("700x500+150+100")
        self.root.configure(bg="#b8c6db")

        

        con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
        cursor = con.cursor()
        cursor.execute("select * from emp_detail where emp_id='"+id+"'")
        a=cursor.fetchone()
        cursor.execute("commit")
        con.close()
        #print(a[0])
        #print(type(a))

        frame=Frame(self.root,bg="white")
        frame.place(x=10,y=20,width=450,height=350)

        emp_name=lbl=Label(frame,text="Employee Name : "+a[0]+"",font=("times new roman",19),fg="Black",bg=None)
        emp_name.place(x=20,y=100)

        emp_id=lbl=Label(frame,text="Employee ID : "+str(a[1])+"",font=("times new roman",19),fg="Black",bg=None)
        emp_id.place(x=20,y=50)

        emp_mailid=lbl=Label(frame,text="Employee e-mail ID : "+a[4]+"",font=("times new roman",19),fg="Black")
        emp_mailid.place(x=20,y=150)

        emp_c_no=lbl=Label(frame,text="Employee Contact Number : "+str(a[3])+"",font=("times new roman",19),fg="Black",bg="#b8c6db")
        emp_c_no.place(x=20,y=200)

        emp_gender=lbl=Label(frame,text="Employee Gender : "+a[5]+"",font=("times new roman",19),fg="Black",bg="#b8c6db")
        emp_gender.place(x=20,y=250)

        

        

        


