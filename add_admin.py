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
import mysql.connector


class add_admin:
    def __init__(self):
        self.root=Tk()
        self.root.title("ADD_ADMIN")
        self.root.geometry("700x500+50+100")
        self.root.configure(bg="#b8c6db")

        username=lbl=Label(self.root,text="Admin Name :",font=("times new roman",19),fg="white",bg="black")
        username.place(x=150,y=50,width=180,height=45)
        self.admin_name=Entry(self.root,font=("times new roman",15,"bold"))
        self.admin_name.place(x=360,y=50,width=250,height=45)

        userid=lbl=Label(self.root,text="Admin ID :",font=("times new roman",19),fg="white",bg="black")
        userid.place(x=150,y=120,width=180,height=45)
        self.admin_id=Entry(self.root,font=("times new roman",15,"bold"))
        self.admin_id.place(x=360,y=120,width=250,height=45)

        password1=lbl=Label(self.root,text="Password :",font=("times new roman",19),fg="white",bg="black")
        password1.place(x=150,y=190,width=180,height=45)
        self.pass1=Entry(self.root,font=("times new roman",15,"bold"))
        self.pass1.place(x=360,y=190,width=250,height=45)

        #back1=Button(self.root,text="Back",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        #back1.place(x=150,y=250,width=124,height=45)

        def admin():
            if(self.admin_name.get()=="" or self.admin_id.get()=="" or self.pass1.get()==""):
                messagebox.showwarning("WARNING","All fields are required")
            else:
                con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
                cursor = con.cursor()
                cursor.execute("insert into admin_login_detail values(%s,%s,%s);",(self.admin_name.get(),self.pass1.get(),self.admin_id.get()))
                cursor.execute("commit")
                con.close()
                self.root.destroy()
                messagebox.showinfo("Info","New Admin added successfully")

        submit=Button(self.root,text="Submit",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FF6347",command=lambda:admin())
        submit.place(x=360,y=260,width=150,height=45)

