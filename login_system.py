#importing modules
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
import csv
from tkinter.scrolledtext import *
import tkinter as tk
from tkinter import ttk

root=Tk()
root.title("Login System")
#root.geometry("1920x1080")
root.attributes("-fullscreen",True)
root.configure(bg="#a1c4fd")
#sql connect

conn=sqlite3.connect("data.db")
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS user_info(first_name TEXT,last_name TEXT,dob TEXT,phone_number REAL,email TEXT,gender TEXT,username TEXT,password TEXT)')

#functions

def login():
    
    c.execute('SELECT username,password FROM user_info')
    data=c.fetchall()

    for i in data:    
        if(u.get()=="" or p.get==""):
            messagebox.showerror("Error","All fields are reqired!")
        elif u.get()==i[0] and p.get()==i[1]:
            messagebox.showinfo("Successfull","Login successfull")
        else:
            messagebox.showerror("Error","Invalid user name or password")


def adminster_login_function(): 
    if(u.get()=="venkatesh" or p.get=="#Venkatesh16"):
        messagebox.showerror("Error","All fields are reqired!")
    elif u.get()=="" and p.get()=="":
        messagebox.showinfo("Successfull","Login successfull")
        Login_Frame.destroy()
        adminster_privilage()
    else:
        messagebox.showerror("Error","Invalid user name or password")

def show_user_info():
    c.execute('SELECT * FROM user_info')
    data=c.fetchall()
    for i in data:
        tree.insert("",tk.END,values=i)

def export_as_csv():
    filename=str(export_btn_e.get())
    myfilename=filename+'.csv'
    with open(myfilename,'w') as f:
        writer=csv.writer(f)
        c.execute('SELECT * FROM user_info')
        data=c.fetchall()
        writer.writerow(['first name','last name','Date of birth','Phone number','Email','Gender','username','password'])
        writer.writerows(data)
        messagebox.showinfo(title="Exported",message='"Exported as {}"'.format(myfilename))

def delete_user_funtion():
    c.execute('SELECT * FROM user_info WHERE username="{}"'.format(delete_user_e.get()))
    data=c.fetchall()
    if(len(data)==0):
        messagebox.showerror("Error","No username exist")
    else:
        c.execute('DELETE FROM user_info WHERE username="{}"'.format(delete_user_e.get()))
        conn.commit()
        messagebox.showinfo("Success","Deleted successfully")        
def searching():
    user_name=str(search_entry.get())
    c.execute('SELECT * FROM user_info WHERE username="{}"'.format(user_name))
    data=c.fetchall()
    data[3]=int(data[3])
    for i in data:
        tree1.insert("",tk.END,values=i)
def clear_tree():
    tree.delete(*tree.get_children())
    

def adminster_privilage():
    global tree
    global export_btn_e
    global sc
    global adminster_login
    global tree1
    
    adminster_login=Frame(root,bg="#a1c4fd")
    adminster_login.place(x=0,y=0)
    
    #adminster_login.configure(width="1350",height="750")
    export_btn=Button(adminster_login,text="Export all details",width="20",bg="#0ca2f2",fg="white",command=export_as_csv)
    export_btn.place(x=20,y=28)
    export_btn_e=Entry(adminster_login,text="enter your file name",width="25",bd="5",font=("",10))
    export_btn_e.place(x=250,y=28)
    show_btn=Button(adminster_login,text="Show all user info",width="20",bg="#0ca2f2",fg="white",command=show_user_info)
    show_btn.grid(row=0,column=1,pady=30,padx=30)
    sc_clear_info=Button(adminster_login,text="Clear",fg="white",bg="#0ca2f2",width="15",command=clear_tree)
    sc_clear_info.place(x=1200,y=30)
    tree=ttk.Treeview(adminster_login,column=("column1","column2","column3","column4","column5","column6","column7","column8"),show="headings")
    tree.heading("#1",text="First Name")
    tree.heading("#2",text="Last Name")
    tree.heading("#3",text="Date of Birth")
    tree.heading("#4",text="Phone number ")
    tree.heading("#5",text="Email")
    tree.heading("#6",text="Gender")
    tree.heading("#7",text="username")
    tree.heading('#8',text='password')
    
    tree.column('#1',minwidth=0,width=189)
    tree.column('#2',minwidth=0,width=189)
    tree.column('#3',minwidth=0,width=189)
    tree.column('#4',minwidth=0,width=189)
    tree.column('#5',minwidth=0,width=189)
    tree.column('#6',minwidth=0,width=189)
    tree.column('#7',minwidth=0,width=189)
    tree.column('#8',minwidth=0,width=189)

    tree.grid(row=10,column=0,columnspan=2,padx=13,pady=5)

    global search_entry
    global delete_user_e
    
    delete_user=Label(adminster_login,text="Enter the username to delete",bg="#a1c4fd",fg="white",font=("",15))
    delete_user.place(x=20,y=330)
    delete_user_e=Entry(adminster_login,bd=5,width="25")
    delete_user_e.place(x=300,y=330)
    delete_user_btn=Button(adminster_login,text="Click here to delete the user",bg="#0ca2f2",fg="white",command=delete_user_funtion)
    delete_user_btn.place(x=500,y=330)

    search_btn=Button(adminster_login,text="Search",width="15",bg="#0ca2f2",fg="white",command=searching)
    search_btn.place(x=300,y=400)
    search_entry=Entry(adminster_login,width="25",bd=5)
    search_entry.place(x=100,y=400)
    
    tree1=ttk.Treeview(adminster_login,column=("column1","column2","column3","column4","column5","column6","column7","column8"),show="headings")
    tree1.heading("#1",text="First Name")
    tree1.heading("#2",text="Last Name")
    tree1.heading("#3",text="Date of Birth")
    tree1.heading("#4",text="Phone number ")
    tree1.heading("#5",text="Email")
    tree1.heading("#6",text="Gender")
    tree1.heading("#7",text="username")
    tree1.heading('#8',text='password')
    
    tree1.column('#1',minwidth=0,width=189)
    tree1.column('#2',minwidth=0,width=189)
    tree1.column('#3',minwidth=0,width=189)
    tree1.column('#4',minwidth=0,width=189)
    tree1.column('#5',minwidth=0,width=189)
    tree1.column('#6',minwidth=0,width=189)
    tree1.column('#7',minwidth=0,width=189)
    tree1.column('#8',minwidth=0,width=189)

    tree1.grid(rows=12,columnspan=2,pady=120)

    sc_clear=Button(adminster_login,text="Clear",fg="white",bg="#0ca2f2",width="15",command=lambda:sc.delete('1.0',END))
    sc_clear.place(x=100,y=720)

    btn_back=Button(root,text="<-",width="5",height="2",bg="white",bd="5",command=rollback_frames_admin)
    btn_back.place(x=1403,y=18)

    close_btn=Button(root,text='X',bg="white",bd=5,width=5,height=2,command=quit)
    close_btn.place(x=1463,y=18)

def rollback_frames_admin():
    adminster_login.destroy()
    login_frame_function()


def rollback_frames():
    Login_Frame.tkraise()
  
def check_username():
    c.execute('SELECT * FROM user_info WHERE username="{}"'.format(eun.get()))
    data=c.fetchall()
    if(len(data)==0):
        return True
    else:
        return False

    

def create_user_frame_function():
    #variables for new loginers
    global fname
    fname=StringVar()
    global dob
    dob=StringVar()
    global pno
    pno=IntVar()
    global email
    email=StringVar()
    global g
    g=StringVar()
    global un
    un=StringVar()
    global ps
    ps=StringVar()
    global lname
    lname=StringVar()

    global efname
    global edob
    global epno
    global eemail
    global eg
    global eun
    global eps
    global elname
    global Create_user_Frame

    Create_user_Frame=Frame(root,bg="white")
    Create_user_Frame.place(x=450,y=120)

    lblfname=Label(Create_user_Frame,text="Enter your First name:",font=("times new roman",12,"bold"),bg="white")
    lblfname.grid(row=1,column=0)
    efname=Entry(Create_user_Frame,bd=5,textvariable=fname,font=("",15),width="35")
    efname.grid(row=1,column=1,pady=13,padx=10)
    
    lbllname=Label(Create_user_Frame,text="Enter your Last name:",font=("times new roman",12,"bold"),bg="white")
    lbllname.grid(row=2,column=0)
    elname=Entry(Create_user_Frame,bd=5,textvariable=lname,font=("",15),width="35")
    elname.grid(row=2,column=1,pady=13,padx=10)
    
    lbldob=Label(Create_user_Frame,text="Enter your Date of birth:",font=("times new roman",12,"bold"),bg="white")
    lbldob.grid(row=3,column=0)
    edob=Entry(Create_user_Frame,bd=5,textvariable=dob,font=("",15),width="35")
    edob.grid(row=3,column=1,pady=13,padx=10)
    
    lblpno=Label(Create_user_Frame,text="Enter your Phone number:",font=("times new roman",12,"bold"),bg="white")
    lblpno.grid(row=4,column=0)
    epno=Entry(Create_user_Frame,bd=5,textvariable=pno,font=("",15),width="35")
    epno.grid(row=4,column=1,pady=13,padx=10)
    
    lblemail=Label(Create_user_Frame,text="Enter your Email address:",font=("times new roman",12,"bold"),bg="white")
    lblemail.grid(row=5,column=0)
    eemail=Entry(Create_user_Frame,bd=5,textvariable=email,font=("",15),width="35")
    eemail.grid(row=5,column=1,pady=13,padx=10)

    lblgen=Label(Create_user_Frame,text="Enter your gender",font=("times new roman",12,"bold"),bg="white")
    lblgen.grid(row=6,column=0)
    eg=Entry(Create_user_Frame,bd=5,textvariable=g,font=("",15),width="35")
    eg.grid(row=6,column=1)

    lblun=Label(Create_user_Frame,text="Enter your Username:",font=("times new roman",12,"bold"),bg="white")
    lblun.grid(row=7,column=0)
    eun=Entry(Create_user_Frame,bd=5,textvariable=un,font=("",15),width="35")
    eun.grid(row=7,column=1,pady=12,padx=10)
    ''' if(len(eun.get())!=0):
        if(check_username()):
            pass
                '''
    lblps=Label(Create_user_Frame,text="Enter your Password:",font=("times new roman",12,"bold"),bg="white")
    lblps.grid(row=8,column=0)
    eps=Entry(Create_user_Frame,bd=5,textvariable=ps,show="*",font=("",15),width="35")
    eps.grid(row=8,column=1,pady=10,padx=10)

    btn_add=Button(Create_user_Frame,text="Add",width="15",bg="#0ca2f2",fg="white",command=add_details_of_loginer)
    btn_add.grid(row=9,column=1,padx=10,pady=20)

def add_details_of_loginer():
    if (check_username()):
        if(efname.get()=="" or elname.get=="" or edob.get=="" or epno.get=="" or eps.get==""or eun.get=="" or eg.get==""or eemail.get=="" ):
            messagebox.showerror("Error","All fields are reqired!")
        else:
            fname=str(efname.get())
            dob=str(edob.get())
            pno=int(epno.get())
            email=str(eemail.get())
            g=str(eg.get())
            un=str(eun.get())
            ps=str(eps.get())
            lname=str(elname.get())
            
            c.execute('INSERT INTO user_info(first_name,last_name,dob,phone_number,email,gender,username,password) VALUES (?,?,?,?,?,?,?,?)',(fname,lname,dob,pno,email,g,un,ps))
            conn.commit()
            messagebox.showinfo("success","Your data added successfully")
            Create_user_Frame.destroy()
    else:
        messagebox.showerror("Error","username cannot be same")
#pics
user_icon=ImageTk.PhotoImage(Image.open("login_icon.jpg"))
#variables
u=StringVar()
p=StringVar()
#layouts

title=Label(root,text="Login System",font=("times new roman",40,"bold"),bg="#3f2feb",fg="white",bd=10,relief=GROOVE)
title.place(x=0,y=0,relwidth=1)


def login_frame_function():

    global Login_Frame

    Login_Frame=Frame(root,bg="white",width="500",height="200")
    Login_Frame.place(x=450,y=120)

    logolbl=Label(Login_Frame,image=user_icon,bd=0)
    logolbl.grid(row=0,columnspan=3,pady=20)    

    lbluser=Label(Login_Frame,text="username",compound=LEFT,font=("times new roman",20,"bold"),bg="white",width="11",height="4")
    lbluser.grid(row=1,column=0,padx=10,pady=10)
    lblpass=Label(Login_Frame,text="password",compound=LEFT,font=("times new roman",20,"bold"),bg="white")
    lblpass.grid(row=2,column=0,padx=10,pady=10)

    textuser=Entry(Login_Frame,bd=5,textvariable=u,relief=GROOVE,font=("",15))
    textuser.grid(row=1,column=1,padx=20)
    textpass=Entry(Login_Frame,bd=5,show="*",textvariable=p,relief=GROOVE,font=("",15))
    textpass.grid(row=2,column=1,padx=20)

    btn_log=Button(Login_Frame,text="Login",width=15,bg="#0ca2f2",fg="white",command=login)
    btn_log.grid(row=3,column=2,pady=10)

    btn_create=Button(Login_Frame,text="create new login",width=15,bg="#0ca2f2",fg="white",command=create_user_frame_function)
    btn_create.grid(row=3,column=0,pady=10)

        
    adminster_login_btn=Button(Login_Frame,width=15,text="Admister login",bg="#0ca2f2",fg="white",command=adminster_login_function)
    adminster_login_btn.grid(row=3,column=1)

login_frame_function()

close_btn=Button(root,text='X',bg="white",bd=5,width=5,height=2,command=quit)
close_btn.place(x=1463,y=18)

btn_bck=Button(root,text="<-",width="5",height="2",bg="white",bd="5",command=rollback_frames)
btn_bck.place(x=1403,y=18)



root.mainloop()

