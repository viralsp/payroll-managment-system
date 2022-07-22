from asyncio.windows_events import NULL
from dataclasses import InitVar
from multiprocessing.sharedctypes import Value
from sqlite3 import Cursor
import string
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  
import mysql.connector
from admin_homepage import*
from tkinter import messagebox
from emp_homepage import*



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"D:\python_emp\bgi.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=480)
        
        img1=Image.open(r"D:\python_emp\bgi1.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label

        emp3_id=StringVar()

        id=lbl=Label(frame,text="ID :",font=("times new roman",19),fg="white",bg="black")
        id.place(x=75,y=155)

        self.id1=Entry(frame,font=("times new roman",15,"bold"),textvariable=emp3_id)
        self.id1.place(x=60,y=185)
        #print(emp3_id)

        username=lbl=Label(frame,text="Username :",font=("times new roman",19),fg="white",bg="black")
        username.place(x=75,y=220)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=60,y=250)

        password=lbl=Label(frame,text="Password :",font=("times new roman",19),fg="white",bg="black")
        password.place(x=75,y=285)

        self.pass1=Entry(frame,show="*",font=("times new roman",15,"bold"))
        self.pass1.place(x=60,y=315)

        i = IntVar()
        r1 = Radiobutton(frame, text="Admin", value=1, variable=i)
        r1.place(x=60, y=365)
        r2 = Radiobutton(frame, text="Employee", value=2, variable=i)
        r2.place(x=180, y=365)
        
        

        #a ="Shubham"
        #b ="123"
        def login1():
            root.destroy()
            Admin_Homepage()
        
       
            

        def login2():
            if(self.txtuser.get()=="" or self.pass1.get()=="" or self.id1.get()==""):
                messagebox.showwarning("WARNING", "username or password can not be empty")
            else :
                if(i.get()==1):
                    #con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
                    #cursor = con.cursor()
                    #cursor.execute("select * from admin_login_detail where uname=%s and password=%s and admin_id=%s",(self.txtuser.get(),self.pass1.get(),self.id1.get()))
                    #a=cursor.fetchone()
                    #cursor.execute("commit")
                    #con.close()
                    #print(a)
                    
                    if(a==None):
                        messagebox.showerror("ERROR","Invalid username or password")
                    else:
                        root.destroy()
                        #print(a[0][1])
                        #print(type(a))
                        Admin_Homepage()
                else :
                    #con = mysql.connector.connect(host="localhost",user="root",password="Viral@1112",database="emp_payroll")
                    #cursor = con.cursor()
                    #cursor.execute("select * from emp_login_detail where  uname=%s and password=%s and emp_id=%s",(self.txtuser.get(),self.pass1.get(),self.id1.get()))
                    #a=cursor.fetchone()
                    
                    #cursor.execute("commit")
                    #con.close()
                    if(a==None):
                        messagebox.showerror("ERROR","Invalid username or password")
                    else:
                        root.destroy()
                        
                        emp_homepage(emp3_id.get())
                    






        loginbtn=Button(frame,text="Login",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970",command=lambda:login1())
        loginbtn.place(x=100,y=415,width=120,height=35)



        


if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()
