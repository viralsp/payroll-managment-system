from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from PIL import Image,ImageTk 
from add_employee_details import*
from add_admin import*
from update_employee_details import*
from login import*
from payment import*
from leave import*

class Admin_Homepage:
    def __init__(self):
        self.root=Tk()
        self.root.title("Admin Page")
        self.root.geometry("700x500+250+100")
        self.root.configure(bg="#b8c6db")

        #self.bg=Image.open(r"C:\Users\Reliance\Desktop\Employee Pay Project\login_form\bgi6.jpg")
        #self.bg=self.bg.resize((1000,650),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(self.bg)
        #lbl_bg=Label(self.root,image=self.photoimage1)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        def logout():
            self.root.destroy()
            

        logoutbtn=Button(self.root,text="EXIT",command=lambda:logout(),font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#FF6347")
        logoutbtn.place(x=400,y=400,width=180,height=45)

        add_empbtn=Button(self.root,text="Add Employee Details",command=lambda:add_employee_details(),font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        add_empbtn.place(x=100,y=100,width=500,height=45)

        add_Nadmn=Button(self.root,text="Add New Admin",command=lambda:add_admin(),font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        add_Nadmn.place(x=100,y=200,width=230,height=45)

        payment=Button(self.root,text="Payment",font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970",command=lambda:payed())
        payment.place(x=370,y=200,width=230,height=45)

        Update_details=Button(self.root,text="Update Details",command=lambda:update_employee_details(),font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        Update_details.place(x=100,y=300,width=230,height=45)

        leavebtn=Button(self.root,text="Leave",command=lambda:leave_record(),font=("times new roman",19,"bold"),bd=3,relief=RIDGE,fg="white",bg="#191970")
        leavebtn.place(x=370,y=300,width=230,height=45)




