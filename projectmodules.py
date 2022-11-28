from tkinter import *
import mysql.connector

exe=mysql.connector.connect(user = 'root', host = 'localhost', database = 'rajlakshya', password = 'tiger25dec')
cur = exe.cursor()

def newreport(frame, userid):
    query1 = '''select * from patient_consum where userid = "{}"'''.format(userid)
    cur.execute(query1)
    ans = cur.fetchone()
    if ans != None:
        query2 = '''delete from patient_consum where userid = "{}"'''.format(userid)
        query3 = '''delete from patient_nut where userid = "{}"'''.format(userid)
        cur.execute(query2)
        cur.execute(query3)
        cur.execute('commit')
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_lbl = Label(frame,bg='#F1948A', text = "No. of chapatis", width = 40); roti_lbl.place(x=50,y=60)
    roti_txt = Entry(frame,bg='#82E0AA', width = 40); roti_txt.place(x=)
