from tkinter import *
import csv
import datetime

root = Tk()
root.title('Attendace System')
root.geometry('1960x650')
#background color
root.configure(background='cyan')
# adding firm name frame
header = Frame(root,bg='cyan',bd=10,relief=RIDGE)
header.pack(side=TOP)

# adding the label
header_name=Label(header,font=('Consolas Constantia', 35,'bold'),text="CYGNUS What's AI",bg='black',fg='cyan',justify=CENTER)
header_name.grid(row=0)
#__________________________>> creating variables
Email_ID = StringVar()
Batch = StringVar()
Batch.set("Select Batch")

Subject = StringVar()
Subject.set("Select Subject")

Year=IntVar()
Semester =IntVar()
# adding the label to buttons
Email_ID_label= Label(root,font=('Consolas Constantia', 14,'bold'),text="Email ID",bg='cyan',fg='black')
Email_ID_label.place(x=140,y=120)
Email_ID_entry=Entry(root,width=40,textvariable=Email_ID)
Email_ID_entry.place(x=140,y=150)

Batch_label= Label(root,font=('Consolas Constantia', 14,'bold'),text="Batch",bg='cyan',fg='black')
Batch_label.place(x=140,y=180)
#create drop down
Drop = OptionMenu(root,Batch,"A1","A2")
Drop.place(x=140,y=210)

Subject_label= Label(root,font=('Consolas Constantia', 14,'bold'),text="Subject",bg='cyan',fg='black')
Subject_label.place(x=140,y=250)
#create  drop down
Drop = OptionMenu(root,Subject,"SC","CD","AA","DIP","NLP","OS")
Drop.place(x=140,y=280)

Year_label= Label(root,font=('Consolas Constantia', 14,'bold'),text="Year",bg='cyan',fg='black')
Year_label.place(x=140,y=310)
Year_entry=Entry(root,width=40,textvariable=Year)
Year_entry.place(x=140,y=340)

Sem_label= Label(root,font=('Consolas Constantia', 14,'bold'),text="Semester",bg='cyan',fg='black')
Sem_label.place(x=140,y=370)
Sem_entry=Entry(root,width=40,textvariable=Semester)
Sem_entry.place(x=140,y=400)

def nextPage():
    ws.destroy()
    import page2
root.mainloop()