from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("registration form")
        self.root.state('zoomed')

        self.load=Image.open('bg.png')
        self.bg=ImageTk.PhotoImage(self.load)
        self.lbl=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.left=Image.open('sd.png')
        self.lg=ImageTk.PhotoImage(self.left)
        self.lbl1=Label(self.root,image=self.lg).place(x=200,y=150,width=425,height=600)
        #frame
        frame1= Frame(self.root,bg='white')
        frame1.place(x=625,y=150,width=700,height=600)

        title=Label(frame1,text='REGISTER HERE',font=("times new roman",30,'bold'),bg='white',fg='#65178a').place(x=50,y=30)

        #entry fields

        fname= Label(frame1, text='First Name', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_fname.place(x=50,y=130,width=250)

        lname= Label(frame1, text='Last Name', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_lname.place(x=370,y=130,width=250)

        contact= Label(frame1, text='Contact Number', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=160)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_contact.place(x=50,y=190,width=250)

        email= Label(frame1, text='Username', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=160)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_email.place(x=370,y=190,width=250)
        self.var_g=IntVar()
        gender= Label(frame1, text='Gender', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=220)
        g_radio_male=Radiobutton(frame1,text='Male',bg='#bcb5c0',padx=5,variable=self.var_g,value=1).place(x=50,y=250)
        g_radio_female = Radiobutton(frame1, text='Female',bg='#bcb5c0', padx=5,variable=self.var_g, value=2).place(x=130, y=250)

        age= Label(frame1, text='Age', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=220)
        self.txt_age=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_age.place(x=370,y=250,width=250)

        password= Label(frame1, text='Password', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=280)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg='#bcb5c0',show="*")
        self.txt_password.place(x=50,y=310,width=250)
        confirm_password= Label(frame1, text='Confirm password', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=280)
        self.txt_confirm_password=Entry(frame1,font=("times new roman",15),bg='#bcb5c0',show='*')
        self.txt_confirm_password.place(x=370,y=310,width=250)

        question= Label(frame1, text='Security Question', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=50, y=340)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",12),state='readonly',justify=CENTER)
        self.cmb_question['values']=('Select','In what city were you born?','What is your bestfriends name?',
                                'What was your favorite food as a child?')
        self.cmb_question.place(x=50,y=370,width=250)
        self.cmb_question.current(0)

        answer= Label(frame1, text='Answer', font=("times new roman", 15, 'bold'), bg='white',
                      fg='#51375d').place(x=370, y=340)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg='#bcb5c0')
        self.txt_answer.place(x=370,y=370,width=250)

        self.terms_chk=IntVar()
        terms=Checkbutton(frame1,text='I Agree To The Terms and Conditions',variable=self.terms_chk,onvalue=1,offvalue=0,bg='white').place(x=50, y=420)

        register_btn=Button(frame1,text="  Register  ",bg='#9a90e4',command=self.register_data).place(x=50,y=500,width=250)
        login_btn=Button(frame1,text="   Login  ",bg='#9a90e4',command=self.login_window).place(x=370,y=500,width=250)
    def clear_data(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_age.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_confirm_password.delete(0, END)
        self.cmb_question.delete(0, END)
        self.txt_answer.delete(0, END)
        self.var_g.set(0)


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()==""or self.txt_email.get()==""or self.txt_age.get()==""or self.var_g.get()==""or self.cmb_question.get()=='Select'or self.txt_password.get()==""or self.txt_confirm_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_password.get()!= self.txt_confirm_password.get():
            messagebox.showerror("Error","password and confirm password doesn't match",parent=self.root)
        elif self.terms_chk.get()==0:
            messagebox.showerror("Error","please agree to the terms and conditions",parent=self.root)
        elif self.txt_contact.get() is StringVar:
            messagebox.showerror("Error","Enter the correct contact number")
        elif len(self.txt_contact.get())!=10:
            messagebox.showerror("Error","Contact number should be 10 digit")
        else:
            try:
                con= mysql.connector.connect(
                    host='127.0.0.1',
                    user='root',
                    password='@!2002bisesh',
                    port=3306,
                    database='registration')
                cur=con.cursor()
                cur.execute("select * from customer_details where email=%s",self.txt_email.get())
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","User already exists,Please try again with another username.",parent=self.root)
                else:
                    cur.execute("insert into customer_details(fname,lname,contact_number,email,gender,age,password,security_question,answer)"
                                "values(%s,%s,%d,%s,%d,%d,%s,%s,%s)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_email.get(),
                                 self.var_g.get(),
                                 self.txt_age.get(),
                                 self.txt_password.get(),
                                 self.cmb_question.get(),
                                 self.txt_answer.get()
                                 )
                                )
                    con.commit()
                    con.close()
                    messagebox.showinfo("success","You have been successfully registered",parent=self.root)
                    self.clear_data()

            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}",parent=self.root)

    def login_window(self):
        self.root.destroy()
        import login

root=Tk()
obj=Register(root)
root.mainloop()
