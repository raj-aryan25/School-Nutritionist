from tkinter import *
import mysql.connector

main = Tk()
main.geometry("1300x700")
main.title("School Nutritionist")
main.configure(bg='#ebf5fb')
main.resizable(False,False)
heading = Label(main,text="NUTRITION MANAGEMENT",bg="#D35400",fg="white", font = ("Arial",30))
heading.pack(fill=BOTH,padx=20,pady=10)
welcomeframe = Frame(main, bg='#85C1E9', width = 500,height = 550)
welcomeframe.place(x=750,y=90)
sideframe = Frame(main,bg= "olive", width = 600,height = 565)
sideframe.place(x=50,y=80)
projectname = Label(sideframe, width = 14,text="School\nNutritionist",fg="#E74C3C",font=("Tahoma",50))
projectname.place(x=22,y=30)
welcome = '''Welcome to School Nutritionist
Your own School Nutrition Management System'''
Label(sideframe,text=welcome,font=).place(x=22,y=250)





#mainframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
#mainframe.pack(fill = BOTH, padx=20,pady=20)
main.mainloop()
