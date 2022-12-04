#treeview properties to set dimension
from tkinter import *
import mysql.connector
from tkinter import messagebox
import patient_desk as pd

exe = mysql.connector.connect(
        user='root',host='localhost',database='schoolnutritionist',password='tiger25dec')
cur = exe.cursor()
userid=''
password=''

def login(frame):
    global userid,password
    frame.tkraise()
    stylelogin = ("Helvetica",18)
    uid=StringVar()
    pwd=StringVar()
    Label(frame,text="Enter Login Credentials",width=25,bg='#17A589',fg='white',font=('Tahoma',24)).place(x=23,y=30)
    Label(frame,text='User ID', width = 12,bg='#CBFFA0',fg='#FFA0A0', font = stylelogin).place(x=50,y=140)
    Label(frame,text='Password', width = 12,bg='#CBFFA0',fg='#FFA0A0', font = stylelogin).place(x=50,y=240)
    userid=Entry(frame,textvariable=uid,bg='#D7BDE2',width = 14,font=stylelogin);userid.place(x=270,y=140)
    password=Entry(frame,textvariable=pwd,bg='#D7BDE2',width = 14,font=stylelogin,show='*');password.place(x=270,y=240)

def log_in(frame):
    stylelogin2 = ("Helvetica",20)
    uid=userid.get()
    pwd=password.get()
    if uid == "" or pwd == "":
        messagebox.showerror("Error","User ID or Password\nnot entered")

    else:
        query1 = '''select * from user where userid = "{}" and password="{}"'''.format(uid,pwd)
        cur.execute(query1)
        ans = cur.fetchone()
        if ans!= None:
            pd.options(uid)
            return 'success'
        else:
            messagebox.showerror("Error","Invalid Credentials\nLogin Failed")
            return 'failed'

def signup(frame):
      def sign_up():
            name = uname.get()
            uid = userid.get()
            pwd = password.get()
            sgender = gender.get()
            phone_no = phone.get()
            if name =='' or uid=='' or pwd=='':
                  messagebox.showerror("Error","Name, Username and Pasword\nare mandatory fields")
            else:
                query1 = '''select * from user where userid = "{}"'''.format(uid)
                cur.execute(query1)
                confirmation = cur.fetchone()
                if confirmation != None:
                    messagebox.showerror("Error","Login ID already exists")
                else:
                    query2 = '''insert into user values("{}","{}","{}","{}",{})'''.format(name,uid,pwd,sgender,phone_no)
                    cur.execute(query2)
                    cur.execute('commit')
                    query3 = '''insert into patient_intake(userid) values("{}")'''.format(uid)
                    cur.execute(query3)
                    cur.execute('commit')
                    query4 = '''insert into patient_nutrilvl(userid) values("{}")'''.format(uid)
                    cur.execute(query4)
                    cur.execute('commit')
                    signup_btn.destroy()
                    Label(frame,text='Sign up Successful',width = 16,bg='#FADBD8',font=stylesignup,fg='red').place(x=285,y=480)

      frame.tkraise()
      stylesignup = ("Helvetica", 15)
      name=StringVar()
      uid=StringVar()
      pwd=StringVar()
      gender=StringVar()
      phone=IntVar(); phone.set("")
      Label(frame,text="Enter your details",width=30,bg='#17A589',fg='white',font=('Tahoma',20)).place(x=21,y=30)
      Label(frame,text='Enter your Name', width = 16,bg='cyan',fg='red', font = stylesignup).place(x=50,y=120)
      Label(frame,text='Enter User ID', width = 16,bg='cyan',fg='red', font = stylesignup).place(x=50,y=180)
      Label(frame,text='Enter Password', width = 16,bg='cyan',fg='red', font = stylesignup).place(x=50,y=240)
      Label(frame,text='Select your gender', width = 25,bg='olive',fg='red', font = stylesignup).place(x=100,y=300)
      R1= Radiobutton(frame, text="Male",variable=gender,value='male',font=stylesignup,bg="#FADBD8")
      R1.place(x=100, y=350)
      R2= Radiobutton(frame, text="Female",variable=gender,value='female',font=stylesignup,bg="#FADBD8")
      R2.place(x=190, y=350)
      R3= Radiobutton(frame, text="Other",variable=gender,value='other',font=stylesignup,bg="#FADBD8")
      R3.place(x=300, y=350)
      Label(frame,text='Enter phone number', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=410)
      uname = Entry(frame, textvariable=name, bg="#D7BDE2", width =15, font=stylesignup); uname.place(x=270, y=120)
      userid=Entry(frame,textvariable=uid,bg='#D7BDE2',width = 15,font=stylesignup); userid.place(x=270,y=180)
      password=Entry(frame,textvariable=pwd,bg='#D7BDE2',width = 15,font=stylesignup,show="*"); password.place(x=270,y=240)
      phone=Entry(frame,textvariable=phone,bg='#D7BDE2',width = 15,font=stylesignup); phone.place(x=270,y=410)
      signup_btn = Button(frame,text='Sign Up',command=sign_up,font=stylesignup)
      signup_btn.place(x=300,y=480)
