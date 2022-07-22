from inspect import FrameInfo
from pickle import FRAME
from tkinter import*
from tkinter import ttk
import tkinter
from turtle import bgcolor
from PIL import Image,ImageTk 
from ast import Lambda
from multiprocessing import connection
from pydoc import text
from sqlite3 import Cursor
from tkinter import font
from admin_homepage import*
from tkinter import messagebox
import mysql.connector


class payed:
    def __init__(self):
        self.root=Tk()
        self.root.title("PAYMENT")
        self.root.geometry("750x650+150+50")
        self.root.configure(bg="#b8c6db")

        

        userid=lbl=Label(self.root,text="Employee ID:",font=("times new roman",19),fg="white",bg="black")
        userid.place(x=110,y=50,width=230,height=45)
        self.emp_id=Entry(self.root,font=("times new roman",15,"bold"))
        self.emp_id.place(x=390,y=50,width=250,height=45)

        transaction=lbl=Label(self.root,text="Transaction id :",font=("times new roman",19),fg="white",bg="black")
        transaction.place(x=110,y=120,width=230,height=45)
        self.trans_id=Entry(self.root,font=("times new roman",15,"bold"))
        self.trans_id.place(x=390,y=120,width=250,height=45)

        date=lbl=Label(self.root,text="Date of payment :",font=("times new roman",19),fg="white",bg="black")
        date.place(x=110,y=190,width=230,height=45)
        self.dT=Entry(self.root,font=("times new roman",15,"bold"))
        self.dT.place(x=390,y=190,width=250,height=45)

        salary=lbl=Label(self.root,text="Salary :",font=("times new roman",19),fg="white",bg="black")
        salary.place(x=110,y=260,width=230,height=45)
        self.sal=Entry(self.root,font=("times new roman",15,"bold"))
        self.sal.place(x=390,y=260,width=250,height=45)

        bonus=lbl=Label(self.root,text="Bonus :",font=("times new roman",19),fg="white",bg="black")
        bonus.place(x=110,y=330,width=230,height=45)
        self.bon=Entry(self.root,font=("times new roman",15,"bold"))
        self.bon.place(x=390,y=330,width=250,height=45)


        #dept=lbl=Label(self.root,text="Department_id:",font=("times new roman",19),fg="white",bg="black")
        #dept.place(x=250,y=350)
        #self.dept_id=Entry(self.root,font=("times new roman",15,"bold"))
        #self.dept_id.place(x=550,y=350)

        
        #back1=Button(self.root,text="Back",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        #back1.place(x=700,y=500,width=124,height=45)

        def pay():
            if(self.emp_id.get()=="" or self.trans_id.get()=="" or self.sal.get()=="" or self.dT.get()==""):
                messagebox.showwarning("WARNING","Some fields are missing")
            else:
                con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
                cursor = con.cursor()
                cursor.execute("insert into payment values(%s,%s,%s,%s,%s);",(self.emp_id.get(),self.trans_id.get(),self.dT.get(),self.sal.get(),self.bon.get()))
                cursor.execute("commit")
                con.close()
                self.root.destroy()
                messagebox.showinfo("Info","Payment done successfully")

        submit=Button(self.root,text="Submit",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FF6347",command=lambda:pay())
        submit.place(x=390,y=400,width=150,height=45)
        self.root.mainloop()