from tkinter import *
import mysql.connector
import projectmodules as pm
com = mysql.connector.connect(user = 'root',host='localhost',database='project',password='tiger25dec')

def next():
    age=str(click_age)
    output1 = Label(top,text=age,width=20,bg='white')
    output1.place(x=80,y=100)

age_options = ['Primary', 'Senior','Teacher']
top = Tk()
top.geometry("1080x600")
top.title("Disease and Nutrition")
top.configure(bg="#EBF5FB")
heading = Label(top,text="NUTRITION MANAGEMENT",bg="#D35400",fg="white", font = ("Arial",30))
heading.pack(fill=BOTH,padx=10,pady=10)
click_age = StringVar()
click_age.set("Infant")
agedrop = OptionMenu(top, click_age, *age_options)
agedrop.place(x=50,y=50)
btn1 = Button(top,text = "Next",command=next)
btn1.place(x=250,y=50)
'''frame1 = Frame(top,bg='#58D68D', width = 400, height=450)
frame1.pack(side='right',padx = 50)
img1 = PhotoImage(file='diet1.png')
lblimg1 = Label(top,image = img1)
lblimg1.place(x=10,y=80)
'''



top.mainloop()
