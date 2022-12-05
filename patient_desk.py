from tkinter import *
import mysql.connector
import table_graphs as tg
from tkinter import messagebox

exe = mysql.connector.connect(user= 'root',host='localhost',database='schoolnutritionist',password='tiger')
cur=exe.cursor()

main = ''
iron = 0; calcium = 0; proteins = 0; vit_d = 0; vit_c = 0
report_img =''
def options(uid):
    global report_img
    def existing_record():
        query = '''select * from patient_nutrilvl where userid = "{}"'''.format(uid)
        cur.execute(query)
        data = cur.fetchone()
        if data[1] == None:
            messagebox.showerror("Error","No Existing Records")
        else:
            optionframe.pack_forget()
            tg.reports(uid, data[6])
    def new_record():
        optionframe.pack_forget()
        entry_of_food(uid)
    optionframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
    optionframe.pack(fill = BOTH, padx=30,pady=30)
    report_img = PhotoImage(file='reports.png')
    report_img_lbl = Label(optionframe, image=report_img)
    report_img_lbl.place(x=90,y=25)
    Button(optionframe,text='View Previous Record',width = 25,bg='pink',font=('Roboto',20),command=existing_record).place(x=650,y=200)
    Button(optionframe,text='Create New Record',width = 25,bg='pink',font=('Roboto',20),command=new_record).place(x=650,y=300)

def entry_of_food(uid):
    global main
    def food_intake(uid):
        def food_set_no(food,food_item):
            global iron, calcium, proteins, vit_d, vit_c
            query1 = '''select * from common_food where food = "{}"'''.format(food)
            cur.execute(query1)
            food_data = cur.fetchone()
            food_nutri = []
            for i in range(1,6):
                food_value = round((float(food_item)*food_data[i]),2)
                food_nutri.append(food_value)
            iron += food_nutri[0]
            calcium += food_nutri[1]
            proteins += food_nutri[2]
            vit_d += food_nutri[3]
            vit_c += food_nutri[4]

        def food_set_g(food,food_item):
            global iron, calcium, proteins, vit_d, vit_c
            query1 = '''select * from common_food where food = "{}"'''.format(food)
            cur.execute(query1)
            food_data = cur.fetchone()
            food_nutri = []
            for i in range(1,6):
                food_value = round(((float(food_item)/100)*food_data[i]),2)
                food_nutri.append(food_value)
            iron += food_nutri[0]
            calcium += food_nutri[1]
            proteins += food_nutri[2]
            vit_d += food_nutri[3]
            vit_c += food_nutri[4]

        apple = apple_entry.get()
        orange = orange_entry.get()
        spinach = spinach_entry.get()
        legume = legume_entry.get()
        peas = peas_entry.get()
        milk = milk_entry.get()
        yogurt = yogurt_entry.get()
        eggs = eggs_entry.get()
        fish = fish_entry.get()
        chicken = chicken_entry.get()
        age = clicked.get()

        query1 = '''delete from patient_intake where userid = "{}"'''.format(uid)
        query2 = '''select * from common_food'''
        query3 = '''insert into patient_intake values("{}",{},{},{},{},{},{},{},{},{},{})'''.format(uid,apple,orange,spinach,legume,peas,milk,\
                                                                                                    yogurt,eggs,fish,chicken)
        query4 = '''select * from patient_intake where userid = "{}"'''.format(uid)
        cur.execute(query1); cur.execute('commit')
        cur.execute(query2)
        nutrivalues_main = cur.fetchall()
        cur.execute(query3)
        cur.execute('commit')
        cur.execute(query4)
        patient_food = cur.fetchone()
        food_set_no('apple',apple)
        food_set_no('orange',orange)
        food_set_g('spinach',spinach)
        food_set_g('legumes',legume)
        food_set_g('peas',peas)
        food_set_no('milk',milk)
        food_set_no('yogurt',yogurt)
        food_set_no('eggs',eggs)
        food_set_g('fish',fish)
        food_set_g('chicken',chicken)
        query5 = '''delete from patient_nutrilvl where userid = "{}"'''.format(uid)
        query6 = '''insert into patient_nutrilvl values("{}",{},{},{},{},{},"{}")'''.format(uid,iron,calcium,proteins,vit_d,vit_c,age)
        cur.execute(query5)
        cur.execute('commit')
        cur.execute(query6)
        cur.execute('commit')
        mainframe.destroy()
        tg.reports(uid, age)

    style = ("Calibri", 22)
    mainframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
    mainframe.pack(fill = BOTH, padx=20,pady=20)
    age_options = ["Primary","Secondary","Teacher"]
    clicked = StringVar()
    clicked.set(age_options[0])
    apple = DoubleVar(); orange = DoubleVar(); spinach = DoubleVar(); legume = DoubleVar(); peas = DoubleVar()
    milk = DoubleVar(); yogurt = DoubleVar(); eggs = DoubleVar(); fish = DoubleVar(); chicken = DoubleVar()
    age_grp = OptionMenu(mainframe, clicked, *age_options)
    age_grp.place(x=480,y=490)
    age_grp.configure(bg='red',fg='white')

    Label(mainframe, text = 'Enter average daily consumption',width = 78,font=style).place(x=40,y=30)
    Label(mainframe,bg='#F1948A', text = "Apple(no.)", width = 20,font = style).place(x=50,y=120)
    Label(mainframe,bg='#F1948A', text = "Oranges(no.)", width = 20,font = style).place(x=50,y=190)
    Label(mainframe,bg='#F1948A', text = "Green Veggies(in g)", width = 20,font = style).place(x=50,y=260)
    Label(mainframe,bg='#F1948A', text = "Legumes(in g)", width = 20,font = style).place(x=50,y=330)
    Label(mainframe,bg='#F1948A', text = "Green peas(in g)", width = 20,font = style).place(x=50,y=400)
    Label(mainframe,bg='#F1948A', text = "Milk(no.of cups)", width = 20,font = style).place(x=670,y=120)
    Label(mainframe,bg='#F1948A', text = "Yogurt(no.of cups)", width = 20,font = style).place(x=670,y=190)
    Label(mainframe,bg='#F1948A', text = "Eggs(no.)", width = 20,font = style).place(x=670,y=260)
    Label(mainframe,bg='#F1948A', text = "Fish(in g)", width = 20,font = style).place(x=670,y=330)
    Label(mainframe,bg='#F1948A', text = "Chicken(in g)", width = 20,font = style).place(x=670,y=400)

    apple_entry = Entry(mainframe,textvariable = apple,bg='#82E0AA', width = 12,font = style)
    apple_entry.place(x=400,y=120)
    orange_entry = Entry(mainframe,textvariable = orange,bg='#82E0AA', width = 12,font = style)
    orange_entry.place(x=400,y=190)
    spinach_entry = Entry(mainframe,textvariable = spinach,bg='#82E0AA', width = 12,font = style)
    spinach_entry.place(x=400,y=260)
    legume_entry = Entry(mainframe,textvariable = legume,bg='#82E0AA', width = 12,font = style)
    legume_entry.place(x=400,y=330)

    peas_entry = Entry(mainframe,textvariable = peas,bg='#82E0AA', width = 12,font = style)
    peas_entry.place(x=400,y=400)
    milk_entry = Entry(mainframe,textvariable = milk,bg='#82E0AA', width = 12,font = style)
    milk_entry.place(x=1020,y=120)
    yogurt_entry= Entry(mainframe,textvariable = yogurt,bg='#82E0AA', width = 12,font = style)
    yogurt_entry.place(x=1020,y=190)
    eggs_entry = Entry(mainframe,textvariable = eggs,bg='#82E0AA', width = 12,font = style)
    eggs_entry.place(x=1020,y=260)
    fish_entry = Entry(mainframe,textvariable = fish,bg='#82E0AA', width = 12,font = style)
    fish_entry.place(x=1020,y=330)
    chicken_entry = Entry(mainframe,textvariable = chicken,bg='#82E0AA', width = 12,font = style)
    chicken_entry.place(x=1020,y=400)
    Label(mainframe,text = "Select\nAge group",font=style).place(x=300,y=470)
    submitbtn = Button(mainframe, text = "Submit",width = 12,font=style,bg='#7FB3D5',command=lambda:food_intake(uid))
    submitbtn.place(x=800,y=470)
