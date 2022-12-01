#treeview properties to set dimension
from tkinter import *
import mysql.connector
exe = mysql.connector.connect(
        user='root',host='localhost',database='schoolnutritionist',password='tiger')
cur = exe.cursor()

def login(frame):
        def log_in():
                uid=userid.get()
                pwd=password.get()
                if uid == "" or pwd == "":
                        print("No userid or or pwd found")
                        logoutput = Label(frame, text="User ID or Password\nnot entered",font=stylelogin)
                        logoutput.place(x=20,y=400)
                else:
                        query1 = '''select * from user where userid = "{}" and password="{}"'''.format(uid,pwd)
                        cur.execute(query1)
                        ans = cur.fetchone()
                        if ans!= None:
                                logoutput = Label(frame, text="Log In Successful\nOpening Main Window",font=stylelogin)
                                logoutput.place(x=20,y=400)
                        else:
                                logoutput = Label(frame, text="Invalid Credentials\nLogin Failed",font=stylelogin)
                                logoutput.place(x=20,y=400)
                                        
        frame.tkraise()
        stylelogin = ("Helvetica",15)
        uid=StringVar()
        pwd=StringVar()
        Label(frame,text="Enter Login Credentials",width=30,bg='#0E6655',fg='white',font=('Tahoma',20)).place(x=21,y=30)
        Label(frame,text='User ID', width = 16,bg='olive',fg='red', font = stylelogin).place(x=50,y=160)
        Label(frame,text='Password', width = 16,bg='olive',fg='red', font = stylelogin).place(x=50,y=260)
        userid=Entry(frame,textvariable=uid,bg='#D7BDE2',width = 15,font=stylelogin);e1.place(x=270,y=160)
        password=Entry(frame,textvariable=pwd,bg='#D7BDE2',width = 15,font=stylelogin);e2.place(x=270,y=260)
        Button(frame,text="Login",command=log_in,bg='olive',fg='white',font=stylelogin,width=14).place(x=250,y=340)
        
        
def signup(frame):
      '''
      def sign_up:
            name = uname.get()
            uid = userid.get()
            pwd=password.get()
            if name ='' or uid=='' or pwd=='':
                  print("Name, Username and Pasword\nare mandatory fields")
      '''
      frame.tkraise()
      stylesignup = ("Helvetica", 15)
      name=StringVar()
      uid=StringVar()
      pwd=StringVar()
      gender=StringVar()
      phone=IntVar()
      Label(frame,text="Enter your details",width=30,bg='#0E6655',fg='white',font=('Tahoma',20)).place(x=21,y=30)
      Label(frame,text='Enter your Name', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=120)
      Label(frame,text='Enter User ID', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=180)
      Label(frame,text='Enter Password', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=240)
      Label(frame,text='Select your gender', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=300)
      
      Label(frame,text='Enter phone number', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=450)
      userid=Entry(frame,textvariable=uid,bg='#D7BDE2',width = 15,font=stylesingup);e1.place(x=270,y=180)
      password=Entry(frame,textvariable=pwd,bg='#D7BDE2',width = 15,font=stylesignup);e2.place(x=270,y=240)
