def addstudent():
    def submitadd():
        print('Added')
    addroot = Toplevel(master=DataEnteryFrame)
    addroot.grab_set()
    addroot.geometry("470x470+220+100")
    addroot.title("Add Student")
    addroot.resizable(False, False)
    addroot.configure(bg="lightyellow")
    
    ######################## Labels- add student
    idlabel = Label(addroot, text="Enter ID:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    idlabel.place(x=10, y=20)
    
    namelabel = Label(addroot, text="Enter Name:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    namelabel.place(x=10, y=80)
    
    mobilelabel = Label(addroot, text="Enter Mobile No.:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    mobilelabel.place(x=10, y=140)
   
    emaillabel = Label(addroot, text="Enter Email:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    emaillabel.place(x=10, y=200)
    
    genderlabel = Label(addroot, text="Enter Gender:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    genderlabel.place(x=10, y=260)
    
    doblabel = Label(addroot, text="Enter D.O.B:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    doblabel.place(x=10, y=320)
    
    addresslabel = Label(addroot, text="Enter Address:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    addresslabel.place(x=10, y=380)

    ######################## Entries- add student
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    addressval = StringVar()

    identry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, "bold "), textvariable=idval)
    identry.place(x=180, y=20)

    nameentry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, "bold"), textvariable=nameval)
    nameentry.place(x=180, y=80)

    mobileentry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, "bold"), textvariable=mobileval)
    mobileentry.place(x=180, y=140)
    
    emailentry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=emailval)
    emailentry.place(x=180, y=200)
    
    genderentry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=genderval)
    genderentry.place(x=180, y=260)

    dobentry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=dobval)
    dobentry.place(x=180, y=320)

    addressentry = Entry(addroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=addressval)
    addressentry.place(x=180, y=380)

    submitbutton = Button(addroot, text="Submit", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), width=10, command=submitadd)
    submitbutton.place(x=180, y=430)

    addroot.mainloop() 
 #########################################################
def searchstudent():
    def search():
        print('Searched')
    
    searchroot = Toplevel(master=DataEnteryFrame)
    searchroot.grab_set()
    searchroot.geometry("470x550+220+100")
    searchroot.title("Add Student")
    searchroot.resizable(False, False)
    searchroot.configure(bg="lightyellow")
    
    ######################## Labels- add student
    idlabel = Label(searchroot, text="Enter ID:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    idlabel.place(x=10, y=20)
    
    namelabel = Label(searchroot, text="Enter Name:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    namelabel.place(x=10, y=80)
    
    mobilelabel = Label(searchroot, text="Enter Mobile No.:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    mobilelabel.place(x=10, y=140)
   
    emaillabel = Label(searchroot, text="Enter Email:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    emaillabel.place(x=10, y=200)
    
    genderlabel = Label(searchroot, text="Enter Gender:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    genderlabel.place(x=10, y=260)
    
    doblabel = Label(searchroot, text="Enter D.O.B:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    doblabel.place(x=10, y=320)
    
    addresslabel = Label(searchroot, text="Enter Address:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    addresslabel.place(x=10, y=380)

    datelabel = Label(searchroot, text="Enter Date:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    datelabel.place(x=10, y=430)

    ######################## Entries- add student
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    addressval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, "bold "), textvariable=idval)
    identry.place(x=180, y=20)

    nameentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, "bold"), textvariable=nameval)
    nameentry.place(x=180, y=80)

    mobileentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, "bold"), textvariable=mobileval)
    mobileentry.place(x=180, y=140)
    
    emailentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=emailval)
    emailentry.place(x=180, y=200)
    
    genderentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=genderval)
    genderentry.place(x=180, y=260)

    dobentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=dobval)
    dobentry.place(x=180, y=320)

    addressentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=addressval)
    addressentry.place(x=180, y=380)

    dateentry = Entry(searchroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=dateval)
    dateentry.place(x=180, y=430)

    submitbutton = Button(searchroot, text="Submit", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), width=10, command=search)
    submitbutton.place(x=180, y=480)

    searchroot.mainloop() 
 ##############################################################3333   
def deletestudent():
    print("Delete Student")
def showstudent():
    print("Show Student")
def updatestudent():
    def update():
        print('Updated')
    updateroot = Toplevel(master=DataEnteryFrame)
    updateroot.grab_set()
    updateroot.geometry("470x650+220+100")
    updateroot.title("Add Student")
    updateroot.resizable(False, False)
    updateroot.configure(bg="lightyellow")
    
    ######################## Labels- add student
    idlabel = Label(updateroot, text="Enter ID:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    idlabel.place(x=10, y=20)
    
    namelabel = Label(updateroot, text="Enter Name:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    namelabel.place(x=10, y=70)
    
    mobilelabel = Label(updateroot, text="Enter Mobile No.:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    mobilelabel.place(x=10, y=120)
   
    emaillabel = Label(updateroot, text="Enter Email:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    emaillabel.place(x=10, y=180)
    
    genderlabel = Label(updateroot, text="Enter Gender:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    genderlabel.place(x=10, y=220)
    
    doblabel = Label(updateroot, text="Enter D.O.B:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w') 
    doblabel.place(x=10, y=280)
    
    addresslabel = Label(updateroot, text="Enter Address:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    addresslabel.place(x=10, y=320)
    
    datelabel = Label(updateroot, text="Enter Date:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    datelabel.place(x=10, y=380)
   
    timelabel = Label(updateroot, text="Enter Time:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    timelabel.place(x=10, y=420)

 ######################## Entries- add student
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    addressval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    

    identery = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, "bold "), textvariable=idval)
    identery.place(x=180, y=20)

    nameentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, "bold"), textvariable=nameval)
    nameentry.place(x=180, y=70)

    mobileentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, "bold"), textvariable=mobileval)
    mobileentry.place(x=180, y=120)
    
    emailentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=emailval)
    emailentry.place(x=180, y=180)
    
    genderentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=genderval)
    genderentry.place(x=180, y=220)

    dobentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=dobval)
    dobentry.place(x=180, y=280)

    addressentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=addressval)
    addressentry.place(x=180, y=320)

    dateentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=dateval)
    dateentry.place(x=180, y=380)
    
    timeentry = Entry(updateroot, width=25, bd=5, font=("times new roman", 12, " bold"), textvariable=timeval)
    timeentry.place(x=180, y=420)
    
    updatebutton = Button(updateroot, text="Submit", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), width=10, command=update)
    updatebutton.place(x=180, y=480)

    updateroot.mainloop() 
###############################################################3
def exportstudent():
    print("Export Student")
def exitstudent():
    res = messagebox.askyesno("Exit Student Management System", "Do you want to exit?")
    if res == True:
        root.destroy()
    
###################################################
def Connectdb():
    def submitdb():
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("400x250+800+250")
    dbroot.resizable(False, False)
    dbroot.configure(bg="lightyellow")
 ########################################################
   
    hostlabel = Label(dbroot, text="Enter Host:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    hostlabel.place(x=10, y=20)

    userlabel = Label(dbroot, text="Enter User:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    userlabel.place(x=10, y=80)

    passwordlabel = Label(dbroot, text="Enter Password:", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), relief=SOLID, borderwidth=3, width=15,anchor='w')
    passwordlabel.place(x=10, y=140)
################################### Entries

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, width=25, bd=5, font=("times new roman", 12, "bold "),textvariable=hostval)
    hostentry.place(x=180, y=20)

    userentery = Entry(dbroot, width=25, bd=5, font=("times new roman", 12, "bold "),textvariable=userval)
    userentery.place(x=180, y=80)

    passwordentry = Entry(dbroot, width=25, bd=5, font=("times new roman", 12, "bold"),textvariable=passwordval)
    passwordentry.place(x=180, y=140)

######################## Buttons
    submitbutton = Button(dbroot, text="Submit", bg="lightgreen", fg="black", font=("times new roman", 12, "bold"), width=10, command=submitdb)
    submitbutton.place(x=150, y=200)
    dbroot.mainloop()
##########################

def tick():
    time_string = time.strftime("%H:%M:%S")
    timeLabel.config(text=f"Time: {time_string}")
    timeLabel.after(200, tick)
    date_string = time.strftime("%d/%m/%Y")
    dateLabel.config(text=f"Date: {date_string}")
    

def Introlable():
    print("This is Student Management System")
##############################################################
from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root = Tk()
root.title("Student Management System")
root.configure(bg="lightblue")
root.geometry("1154x600+50+50")
root.resizable(False, False)
################################# Frames #############
DataEnteryFrame = Frame(root, bg="lightgrey", relief=SOLID , borderwidth=5)
DataEnteryFrame.place(x=10, y=80, width=400, height=450)
##############################Frame for show data #############
frontlabel = Label(DataEnteryFrame, text="Enter Student Details", bg="lightgrey", fg="black", font=("times new roman", 20, "bold"))
frontlabel.pack(side=TOP, fill=X)

addbutton = Button(DataEnteryFrame, text="1. Add Student", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=addstudent)
addbutton.pack(side=TOP, expand=True)

searchbutton = Button(DataEnteryFrame, text="2. Search Student", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=searchstudent)
searchbutton.pack(side=TOP, expand=True)

deletebutton = Button(DataEnteryFrame, text="3 Delete Student", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=deletestudent)
deletebutton.pack(side=TOP, expand=True)

updatebutton = Button(DataEnteryFrame, text="4. Update Student", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=updatestudent)
updatebutton.pack(side=TOP, expand=True)

showallbutton = Button(DataEnteryFrame, text="5. Show All", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=showstudent)
showallbutton.pack(side=TOP, expand=True)

exportbutton = Button(DataEnteryFrame, text="6. Export data", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=exportstudent)
exportbutton.pack(side=TOP, expand=True)

exitbutton = Button(DataEnteryFrame, text="7. Exit", bg="violet", font=("times new roman", 12, "bold"),activebackground="lightgreen", relief=RIDGE, bd=3, activeforeground="black",width=25, command=exitstudent)
exitbutton.pack(side=TOP, expand=True)


##########################################

ShowDataFrame = Frame(root, bg="lightgrey", relief=SOLID , borderwidth=5)
ShowDataFrame.place(x=520, y=85, width=620, height=500)

style = ttk.Style()
style.configure("Treeview.Heading", font=("times new roman", 15, "bold"), foreground="black")
style.configure("Treeview", font=("times new roman", 12, "bold"), foreground="black", background="lightcyan")
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable = Treeview(ShowDataFrame, columns=("ID", "Name", "Mobile No.", "Email", "Gender", "D.O.B", "Address", "Date", "Time"), show='headings', xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading("ID", text="ID")
studenttable.heading("Name", text="Name")
studenttable.heading("Mobile No.", text="Mobile No")
studenttable.heading("Email", text="Email")
studenttable.heading("Gender", text="Gender")
studenttable.heading("D.O.B", text="D.O.B")
studenttable.heading("Address", text="Address")
studenttable.heading("Date", text="Date")
studenttable.heading("Time", text="Time")
studenttable.column("ID", width=50)
studenttable.column("Name", width=100)
studenttable.column("Mobile No.", width=100)
studenttable.column("Email", width=150)
studenttable.column("Gender", width=80)
studenttable.column("D.O.B", width=100)
studenttable.column("Address", width=150)
studenttable.column("Date", width=100)
studenttable.column("Time", width=100)
studenttable['show']='headings'
studenttable.pack(fill=BOTH, expand=1)

titleLabel = Label(root, text="Student Management System", bg="lightblue", fg="black", font=("times new roman", 30, "bold"))
titleLabel.pack(side=TOP, fill=X)
################################ Date and Time #############
dateLabel = Label(root, text=f"Date: {time.strftime('%d/%m/%Y')}", bg="lightblue", fg="black", font=("times new roman", 12, "bold"))
dateLabel.place(x=10, y=50)

timeLabel = Label(root, text=f"Time: {time.strftime('%H:%M:%S')}", bg="lightblue", fg="black", font=("times new roman", 12, "bold"))
timeLabel.place(x=1000, y=50)

#########################################Connect to Database#############
ConnectButton = Button(root, text="Connect To Database", bg="violet", fg="black", font=("times new roman", 12, "bold"), command=Connectdb)
ConnectButton.place(x=850, y=15)
root.mainloop()