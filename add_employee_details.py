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


class add_employee_details:
    def __init__(self):
        self.root=Tk()
        self.root.title("ADD_EMPLOYEE_DETAILS")
        self.root.geometry("750x650+150+50")
        self.root.configure(bg="#b8c6db")

        

        username=lbl=Label(self.root,text="Employee Name :",font=("times new roman",19),fg="white",bg="black")
        username.place(x=110,y=50,width=230,height=45)
        self.emp_name=Entry(self.root,font=("times new roman",15,"bold"))
        self.emp_name.place(x=390,y=50,width=250,height=45)

        contact_no=lbl=Label(self.root,text="Contact Number :",font=("times new roman",19),fg="white",bg="black")
        contact_no.place(x=110,y=120,width=230,height=45)
        self.contact_number=Entry(self.root,font=("times new roman",15,"bold"))
        self.contact_number.place(x=390,y=120,width=250,height=45)

        address=lbl=Label(self.root,text="Address :",font=("times new roman",19),fg="white",bg="black")
        address.place(x=110,y=190,width=230,height=45)
        self.Address1=Entry(self.root,font=("times new roman",15,"bold"))
        self.Address1.place(x=390,y=190,width=250,height=45)

        email=lbl=Label(self.root,text="Email-ID :",font=("times new roman",19),fg="white",bg="black")
        email.place(x=110,y=260,width=230,height=45)
        self.email_id=Entry(self.root,font=("times new roman",15,"bold"))
        self.email_id.place(x=390,y=260,width=250,height=45)

        gend=lbl=Label(self.root,text="Gender :",font=("times new roman",19),fg="white",bg="black")
        gend.place(x=110,y=330,width=230,height=45)
        self.gender=Entry(self.root,font=("times new roman",15,"bold"))
        self.gender.place(x=390,y=330,width=250,height=45)

        id=lbl=Label(self.root,text="Employee ID :",font=("times new roman",19),fg="white",bg="black")
        id.place(x=110,y=400,width=230,height=45)
        self.emp_id=Entry(self.root,font=("times new roman",15,"bold"))
        self.emp_id.place(x=390,y=400,width=250,height=45)

        #dept=lbl=Label(self.root,text="Department_id:",font=("times new roman",19),fg="white",bg="black")
        #dept.place(x=250,y=350)
        #self.dept_id=Entry(self.root,font=("times new roman",15,"bold"))
        #self.dept_id.place(x=550,y=350)

        date=lbl=Label(self.root,text="Date of Birth :",font=("times new roman",19),fg="white",bg="black")
        date.place(x=110,y=470,width=230,height=45)
        self.date1=Entry(self.root,font=("times new roman",15,"bold"))
        self.date1.place(x=390,y=470,width=250,height=45)

        #back1=Button(self.root,text="Back",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        #back1.place(x=700,y=500,width=124,height=45)

        def emp():
            if(self.emp_id.get()=="" or self.email_id.get()=="" or self.emp_name.get()=="" or self.contact_number.get()==""):
                messagebox.showwarning("WARNING","Some fields are missing")
            else:
                con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
                cursor = con.cursor()
                cursor.execute("insert into emp_detail values(%s,%s,%s,%s,%s,%s,%s);",(self.emp_name.get(),self.emp_id.get(),self.Address1.get(),self.contact_number.get(),self.email_id.get(),self.gender.get(),self.date1.get()))
                cursor.execute("commit")
                con.close()
                self.root.destroy()
                messagebox.showinfo("Info","Employee details added successfully")

        submit=Button(self.root,text="Submit",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FF6347",command=lambda:emp())
        submit.place(x=390,y=550,width=150,height=45)
        self.root.mainloop()
        

