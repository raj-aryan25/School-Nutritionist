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
                        logoutput = Label(frame, text="User ID or Password\nnot entered",font=stylelogin,width=25)
                        logoutput.place(x=30,y=380)
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
        Label(frame,text="Enter Login Credentials",width=30,bg='#17A589',fg='white',font=('Tahoma',20)).place(x=21,y=30)
        Label(frame,text='User ID', width = 16,bg='#CBFFA0',fg='#FFA0A0', font = stylelogin).place(x=50,y=140)
        Label(frame,text='Password', width = 16,bg='#CBFFA0',fg='#FFA0A0', font = stylelogin).place(x=50,y=240)
        userid=Entry(frame,textvariable=uid,bg='#D7BDE2',width = 15,font=stylelogin);userid.place(x=270,y=140)
        password=Entry(frame,textvariable=pwd,bg='#D7BDE2',width = 15,font=stylelogin);password.place(x=270,y=240)
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
      def gender_selection():
                 sgender = gender.get()
                 
      frame.tkraise()
      stylesignup = ("Helvetica", 15)
      name=StringVar()
      uid=StringVar()
      pwd=StringVar()
      gender=StringVar()
      phone=IntVar()
      Label(frame,text="Enter your details",width=30,bg='#17A589',fg='white',font=('Tahoma',20)).place(x=21,y=30)
      Label(frame,text='Enter your Name', width = 16,bg='cyan',fg='red', font = stylesignup).place(x=50,y=120)
      Label(frame,text='Enter User ID', width = 16,bg='cyan',fg='red', font = stylesignup).place(x=50,y=180)
      Label(frame,text='Enter Password', width = 16,bg='cyan',fg='red', font = stylesignup).place(x=50,y=240)
      Label(frame,text='Select your gender', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=300)
      R1= Radiobutton(frame, text="Male",variable=gender,value='male',command=gender_selection,font=stylesignup)
      R1.place(x=100, y=380)
      R2= Radiobutton(frame, text="Female",variable=gender,value='female',command=gender_selection,font=stylesignup)
      R2.place(x=200, y=380)
      R3= Radiobutton(frame, text="Other",variable=gender,value='other',command=gender_selection,font=stylesignup)
      R3.place(x=300, y=380)
      Label(frame,text='Enter phone number', width = 16,bg='olive',fg='red', font = stylesignup).place(x=50,y=450)
      uname = Entry(frame, textvariable=name, bg="#D7BDE2", width =15, font=stylesignup); uname.place(x=270, y=120)
      userid=Entry(frame,textvariable=uid,bg='#D7BDE2',width = 15,font=stylesignup); userid.place(x=270,y=180)
      password=Entry(frame,textvariable=pwd,bg='#D7BDE2',width = 15,font=stylesignup,show="*"); password.place(x=270,y=240)
      phone=Entry(frame,textvariable=phone,bg='#D7BDE2',width = 15,font=stylesignup); phone.place(x=270,y=440)
      
