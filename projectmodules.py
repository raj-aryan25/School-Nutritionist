from tkinter import *
import mysql.connector

exe=mysql.connector.connect(user = 'root', host = 'localhost', database = 'rajlakshya', password = 'tiger')
cur = exe.cursor()

def signup():
    uname = username.get()
    id = userid.get()
    pwd = password.get()
    query = 'insert into user values("{}","{}","{}")'.format(uname,uid,pwd)
    cur.execute(query)
    cur.execute("commit")

def login():
    uid = userid.get()
    pwd = password.get()
    query1 = 'select count(*) from user where userid="{}"'.format(uid)
    cur.execute(query1)
    ans = cur.fetchone()
    if ans[0] == 1:
        query2 = 'select count(*) from user where userid="{}" and password="{}"'.format(uid,pwd)
        cur.execute(query2)
        verify = cur.fetchone()
        if verify[0] == 1:
            if_login = Label(loginframe, text="Login Successful!",width = 30)
            if_login.place(x=50,y=250)
        else:
            if_login = Label(loginframe, text="Login Failed!\nWrong ID or Password!",width = 30)
            if_login.place(x=50,y=250)
    else:
        if_login = Label(loginframe, text="No such Userid found",width = 30)
        if_login.place(x=50,y=250)
