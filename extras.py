from tkinter import *

main = Tk()
main.geometry("1300x700")
main.title("School Nutritionist")
main.configure(bg='#ebf5fb')
main.resizable(False,False)
heading = Label(main,text="NUTRITION MANAGEMENT",bg="#D35400",fg="white", font = ("Arial",30))
heading.pack(fill=BOTH,padx=20,pady=10)

mainframe = Frame(main, bg = '#d2fc82', width = 1000, height = 580)
mainframe.pack(fill = BOTH, padx=20,pady=20)
style = ("Arial",30)
disease = "None"
Label(mainframe,text="Report",bg='yellow',width = 40,font=style).place(x=25,y=25)
Label(mainframe,text="Disease Identified",width = 20).place(x=50,y=100)
Label(mainframe,text=disease,width=40).place(x=400,y=100)
Label(mainframe,text="Suggestions",width = 20).place(x=50,y=200)
Button(mainframe,text = "Graph",font=style,width = 20).place(x=100,y=300)






main.mainloop()
