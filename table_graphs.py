from tkinter import *
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from tkinter import ttk

exe = mysql.connector.connect(user='root',host='localhost',password='tiger',database='schoolnutritionist')
cur = exe.cursor()
main = ''
mainframe = ''
low_intake=''
suggestions=''

img_report = ''

def low_nutrients(uid,age):

    global low_intake, suggestions
    low_values = []
    query1 = '''select * from patient_nutrilvl where userid = "{}"'''.format(uid)
    cur.execute(query1)
    patient_data = list(cur.fetchone())
    patient_data = patient_data[1:6]
    query2 = '''select * from age_group where AgeGrp = "{}"'''.format(age)
    cur.execute(query2)
    age_data = list(cur.fetchone())
    age_data = age_data[1:6]
    if patient_data[0] < age_data[0]:
        low_values.append('Iron')
        suggestions += '\n> Low Intake of Iron.\n - Consume Chicken, Dark Chocolate, Spinach, \n   Legumes.'
    if patient_data[1] < age_data[1]:
        low_values.append('Calcium')
        suggestions += '\n> Low Intake of Calcium.\n - Consume Milk, Yogurt, Almonds, Broccoli'
    if patient_data[2] < age_data[2]:
        low_values.append('Proteins')
        suggestions += '\n> Low Intake of Proteins.\n - Consume Eggs, Milk, Peas, Soybean'
    if patient_data[3] < age_data[3]:
        low_values.append('Vitamin D')
        suggestions += '\n> Low Intake of Vitamin D.\n - Consume Milk, Egg, Mushroom, VitaminD \n   supplements'
    if patient_data[4] < age_data[4]:
        low_values.append('Vitamin C')
        suggestions += '\n> Low Intake of Vitamin C.\n - Consume Orange, Kiwi, Sprouts, Guava'
    if low_values == []:
        low_intake = 'None  '
        suggestions = 'Your Nutrition levels are good.\nGood job.\nKeep it Maintained'
    else:
        for i in low_values:
            low_intake = low_intake + i + ', '



def table(uid,age):
    global img_report
    def go_back():
        tableframe.pack_forget()
        reportframe.pack(fill = BOTH,padx=20,pady=20)
    global reportframe
    query1 = '''select * from patient_nutrilvl where userid = "{}"'''.format(uid)
    cur.execute(query1)
    patient_data = list(cur.fetchone())
    patient_data = patient_data[1:6]
    query2 = '''select * from age_group where AgeGrp = "{}"'''.format(age)
    cur.execute(query2)
    age_data = list(cur.fetchone())
    age_data = age_data[1:6]
    reportframe.pack_forget()
    tableframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
    tableframe.pack(fill=BOTH,padx=20,pady=20)
    Label(tableframe, text='Table',font=('Helvetica',30),bg='#F7BD7A',width = 20).place(x=620,y=80)
    style_ttk = ttk.Style()
    style_ttk.configure("Trreview", bg='yellow',fg='red',rowheight = 25,fieldbackground='grey')
    table = ttk.Treeview(tableframe,height=10,column=(1,2,3,4),show="headings")
    table.place(x=500,y=200)
    table.column(1,anchor=CENTER, stretch=NO, width=100)
    table.column(2,anchor=CENTER, stretch=NO, width=200)
    table.column(3,anchor=CENTER, stretch=NO, width=200)
    table.column(4,anchor=CENTER, stretch=NO, width=200)
    table.heading(1,text="S. No.")
    table.heading(2,text="Nutrient")
    table.heading(3,text="Normal Levels")
    table.heading(4,text="Your Levels")
    table.insert('', 'end', text="1", values=('1','Iron(mg)',age_data[0],patient_data[0]))
    table.insert('', 'end', text="2", values=('2','Calcium(mg)',age_data[1],patient_data[1]))
    table.insert('', 'end', text="3", values=('3','Proteins(g)',age_data[2],patient_data[2]))
    table.insert('', 'end', text="4", values=('4','Vitamin D(IU)',age_data[3],patient_data[3]))
    table.insert('', 'end', text="5", values=('5','Vitamin C(mg)',age_data[4],patient_data[4]))
    img_report = PhotoImage(file="reports.png")
    img1 = Label(tableframe,image = img_report)
    img1.place(x=35,y=35)
    Button(tableframe,text='Go Back',command=go_back,font=20,width = 16).place(x=750,y=480)


def graph(uid,age):
    barWidth = 0.25
    fig = plt.subplots(figsize =(12, 8))
    query1 = '''select * from patient_nutrilvl where userid = "{}"'''.format(uid)
    cur.execute(query1)
    patient_data = list(cur.fetchone())
    patient_data = patient_data[1:6]
    query2 = '''select * from age_group where AgeGrp = "{}"'''.format(age)
    cur.execute(query2)
    age_data = list(cur.fetchone())
    age_data = age_data[1:6]
    patient_data[1] = round(patient_data[1]/100,2)
    age_data[1] = round(age_data[1]/100,2)
    patient_data[3] = round(patient_data[3]/100,2)
    age_data[3] = round(age_data[3]/100,2)

    br1 = np.arange(len(age_data))
    br2 = [x + barWidth for x in br1]

    plt.bar(br1, age_data, color ='g', width = barWidth,
            edgecolor ='grey', label ='Normal Data')
    plt.bar(br2, patient_data, color ='b', width = barWidth,
            edgecolor ='grey', label ='Patient Data')

    plt.xlabel('Nutrients', fontweight ='bold', fontsize = 15)
    plt.ylabel('Nutrition level', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(age_data))],
            ['Iron(mcg)', 'Calcium(g)', 'Proteins(cg)', 'Vitamin D(0.01 IU)', 'Vitamin C(mg)'])

    plt.legend()
    plt.show()

def chart(uid,age):
    query1 = '''select * from patient_nutrilvl where userid = "{}"'''.format(uid)
    cur.execute(query1)
    patient_data = list(cur.fetchone())
    patient_data = patient_data[1:6]
    query2 = '''select * from age_group where AgeGrp = "{}"'''.format(age)
    cur.execute(query2)
    age_data = list(cur.fetchone())
    age_data = age_data[1:6]
    x = np.array(['Iron(mg)','Calcium(mg)','Proteins(g)','Vitamin D(IU)','Vitamin C(mg)'])
    y = patient_data
    plt.plot(x, y,label='Your levels')

    x1 = ['Iron(mg)','Calcium(mg)','Proteins(g)','Vitamin D(IU)','Vitamin C(mg)']
    y1 = age_data
    plt.plot(x1, y1, '-.',label='Normal Levels')

    plt.xlabel("Nutrients")
    plt.ylabel("Nutrition level")
    plt.title('Nutrition Comparison')
    plt.legend(loc='upper left')
    plt.show()

def reports(uid,age):
    global reportframe, low_intake, suggestions
    reportframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
    reportframe.pack(fill = BOTH, padx=20,pady=20)
    style = ("Tahoma",20)
    low_nutrients(uid,age)
    report_lbl = Label(reportframe,text="REPORT",bg='yellow',fg='Purple',width = 54,font=('Candara',30,'bold'))
    report_lbl.place(x=25,y=25)
    Label(reportframe,text="Nutrients Deficient",width = 20,font=style,bg='#E59866',fg='#A9CCE3').place(x=195,y=100)
    Label(reportframe,text=low_intake[:-2],width=40,font=style,bg='#AED6F1',fg='#F39C12').place(x=585,y=100)
    Label(reportframe,text="Suggestions",width = 20,font = style,bg='#E59866',fg='#A9CCE3').place(x=195,y=165)
    suggestion_txt = Text(reportframe,width =45,height=12,bg='light cyan',font=("Courier",17,'bold'))
    suggestion_txt.insert(END, suggestions[1:])
    suggestion_txt.configure(state='disabled')
    suggestion_txt.place(x=100,y=225)
    Button(reportframe,text = "Table",font=style,width = 20,command =lambda:table(uid,age)).place(x=775,y=250)
    Button(reportframe,text = "Bar Graph",font=style,width = 20,command=lambda:graph(uid,age)).place(x=775,y=350)
    Button(reportframe,text = "Line Chart",font=style,width = 20,command=lambda:chart(uid,age)).place(x=775,y=450)
