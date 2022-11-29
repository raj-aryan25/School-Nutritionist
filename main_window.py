from tkinter import *
import mysql.connector

def nextscr():
        welcomeframe.destroy()
        sideframe.destroy()
main = Tk()
main.geometry("1300x700")
main.title("School Nutritionist")
main.configure(bg='#ebf5fb')
main.resizable(False,False)
style1= ("Helvetica",18)
heading = Label(main,text="NUTRITION MANAGEMENT",bg="#D35400",fg="white", font = ("Arial",30))
heading.pack(fill=BOTH,padx=20,pady=10)
welcomeframe = Frame(main, bg='#85C1E9', width = 500,height = 550)
welcomeframe.place(x=700,y=90)
sideframe = Frame(main,bg= "#ebf5fb", width = 600,height = 565)
sideframe.place(x=50,y=80)
img1 = PhotoImage(file="dietician1.png")
img_lbl= Label(sideframe,image = img1,width = 400,height=400)
img_lbl.place(x=50,y=10)
projectname = Label(sideframe,bg='#A3E4D7', width = 14,text="SCHOOL\nNUTRITIONIST",fg="#E74C3C",font=("Tahoma",50))
projectname.place(x=22,y=400)

#btn1 = Button(welcomeframe,text="delete",command=deleteh)
#btn1.place(x=20,y=200)

welcome = '''Welcome to School Nutritionist\n
Your own School Nutrition Management System'''
Label(welcomeframe,text=welcome,font=("Tahoma",16)).place(x=22,y=30)
Label(welcomeframe,text='Login to Continue', font = style1,width=30).place(x=30,y=180)
Button(welcomeframe,text="Login",font=style1).place(x=80,y=280)

Label(welcomeframe,text='Login to Continue', font = style1,width=30).place(x=30,y=180)
Button(welcomeframe,text="Login",font=style1).place(x=80,y=280)






#mainframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
#mainframe.pack(fill = BOTH, padx=20,pady=20)
main.mainloop()
