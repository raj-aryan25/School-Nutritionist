from tkinter import *
import mysql.connector

exe=mysql.connector.connect(user = 'root', host = 'localhost', database = 'rajlakshya', password = 'tiger')
cur = exe.cursor()

def signup():
    uname = username.get()
    id = userid.get()
    pwd = password.get()
    query = 'insert into user values("{}","{}","{}")'.format(uname,id,pwd)
    cur.execute(query)
    cur.execute("commit")

def login():
    id = userid.get()
    pwd = password.get()
    query1 = 'select count(*) from user where userid="{}"'.format(id)
    cur.execute(query1)
    ans = cur.fetchone()
    if ans = 1:
        query2 = 'select count(*) from user where userid="{}" and password="{}"'.format(id,pwd)
        cur.execute(query2); verify = cur.fetchone()
        if verify = 1:
            if_login = Label(loginframe, text="Login Successful!",width = 400, height = 400)
            if_login.place(x=2,y=2)
        else:
            if_login = Label(loginframe, text="Login Failed!\nWrong ID or Password!",width = 400, height = 400)
            if_login.place(x=2,y=2)
