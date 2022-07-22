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
from admin_homepage import *
import mysql.connector


class leave_record:
    def __init__(self):
        self.root=Tk()
        self.root.title("APPLY LEAVE")
        self.root.geometry("600x400+0+0")
        self.root.configure(bg="#b8c6db")

        emp_id=lbl=Label(self.root,text="Employee ID :",font=("times new roman",19),fg="white",bg="black")
        emp_id.place(x=100,y=50)
        self.emp_id=Entry(self.root,font=("times new roman",15,"bold"))
        self.emp_id.place(x=350,y=50)

        start1=lbl=Label(self.root,text="START DATE",font=("times new roman",19),fg="white",bg="black")
        start1.place(x=100,y=100)
        self.startdate=Entry(self.root,font=("times new roman",15,"bold"))
        self.startdate.place(x=350,y=100)

        end1=lbl=Label(self.root,text="END DATE",font=("times new roman",19),fg="white",bg="black")
        end1.place(x=100,y=150)
        self.enddate=Entry(self.root,font=("times new roman",15,"bold"))
        self.enddate.place(x=350,y=150)

        nodays1=lbl=Label(self.root,text="NUMBER OF DAYS",font=("times new roman",19),fg="white",bg="black")
        nodays1.place(x=100,y=200)
        self.no_of_days=Entry(self.root,font=("times new roman",15,"bold"))
        self.no_of_days.place(x=350,y=200)

        reason1=lbl=Label(self.root,text="REASON",font=("times new roman",19),fg="white",bg="black")
        reason1.place(x=100,y=250)
        self.reason=Entry(self.root,font=("times new roman",15,"bold"))
        self.reason.place(x=350,y=250)

        #back1=Button(self.root,text="Back",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        #back1.place(x=200,y=250,width=124,height=45)

        def leave1():
            if(self.emp_id.get()=="" or self.startdate.get()=="" or self.enddate.get()=="" or self.no_of_days.get()=="" or self.reason.get()==""):
                messagebox.showwarning("WARNING","All fields are required")
            else:
                con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
                cursor = con.cursor()
                cursor.execute("insert into leave_record values(%s,%s,%s,%s,%s);",(self.startdate.get(),self.emp_id.get(),self.enddate.get(),self.no_of_days.get(),self.reason.get()))
                cursor.execute("commit")
                con.close()
                self.root.destroy()
                messagebox.showinfo("Info","Leave Record updated successfully")


        submit=Button(self.root,text="Submit",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FF6347",command=lambda:leave1())
        submit.place(x=350,y=300,width=150,height=45)

