from tkinter import *
import mysql.connector
import loginsignup as ls

exe = mysql.connector.connect(user='root', host='localhost',password='tiger25dec',database='rajlakshya')
cur = exe.cursor()

main = Tk()
main.geometry("1300x700")
main.title("School Nutritionist")
main.configure(bg='#ebf5fb')
main.resizable(False,False)
heading = Label(main,text="NUTRITION MANAGEMENT",bg="#D35400",fg="white", font = ("Arial",30))
heading.pack(fill=BOTH,padx=20,pady=10)

mainframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
mainframe.pack(fill = BOTH, padx=20,pady=20)





main.mainloop()
