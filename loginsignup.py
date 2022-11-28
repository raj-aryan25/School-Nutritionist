from tkinter import *
import mysql.connector

exe = mysql.connector.connect(user='root', host='localhost',database='rajlakshya',password='tiger25dec')
cur = exe.cursor()

def signupgo():
    def signup():
        uname = uname_txt.get()
        uid = uid_txt.get()

























def signupgo(frame,frame2):
    def signup():
        uname = str(uname_txt.get())
        uid = str(uid_txt.get())
        pwd = str(pwd_txt.get())
        phone = str(phone_txt.get())
        print(uname)

        query1 = 'select count(*) from user where userid = "{}"'.format(uid)
        cur.execute(query1)
        ans = cur.fetchone()
        print(ans)
        if ans[0] == 1:
            msg = Text(frame,text='User ID already exists!' ,width = 40,bg='cyan'); msg.place(x=80,y=280)
        elif ans[0] == 0:
            query2 = 'insert into user values("{}","{}","{}",{})'.format(uname,uid,pwd,phone)
            cur.execute(query2)
            cur.execute('commit')
            msg = Text(frame,text='Sign Up Successful!' ,width = 40,bg='cyan'); msg.place(x=80,y=280)
        else:
            msg = Text(frame,text='Error! Try again' ,width = 40,bg='cyan'); msg.place(x=80,y=280)

    frame2.place_forget()
    frame.place(x=50,y=100)
    uname_lbl = Label(frame, text = 'Name', width = 25);  uname_lbl.place(x=40,y=80)
    uid_lbl = Label(frame, text = 'Username', width = 25);  uid_lbl.place(x=40,y=120)
    pwd_lbl = Label(frame, text = 'Username', width = 25);  pwd_lbl.place(x=40,y=160)
    phone_lbl = Label(frame, text = 'Username', width = 25);   phone_lbl.place(x=40,y=200)
    uname_txt = Entry(frame,width = 25);    uname_txt.place(x=150,y=80)
    uid_txt = Entry(frame,width = 25);  uid_txt.place(x=150,y=120)
    pwd_txt = Entry(frame,width = 25);  pwd_txt.place(x=150,y=160)
    phone_txt = Entry(frame,width = 25);   phone_txt.place(x=150,y=200)
    signup_btn = Button(frame, text='Signup',width=20,command=signup())
    signup_btn.place(x=180,y=280)
