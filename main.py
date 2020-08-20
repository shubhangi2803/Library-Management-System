
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBooks import *
from DeleteBook import *
from ViewBooks import *
from SearchBook import *
from IssueBook import *

mypass = "shubhu" #Database password
mydatabase="library"  #Database name

# Enter Table Names here
empTable = "empdetail" #Employee Table
stuTable = "studetail" #Student Table

root = Tk()
root.title("Library_Manager")
root.geometry("700x570")
root.resizable(width=False,height=False)
count = 0
empFrameCount = 0

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()


 # Employee menu after login
def empMenu():

    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,labelFrame,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#aef35a",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="DASHBOARD", fg='black', font='helvetica 12 bold')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)

    btn1 = Button(root,text="Add Book",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=addBooks)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Book",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=delete)
    btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View Books",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=View)
    btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Issue Book",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command = issueBook)
    btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Search Book",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=searchBook)
    btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    backBtn = Button(root,text="Back",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=Employee)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)

# Student menu after login
def stuMenu():

    global headingFrame1,headingFrame2,headingLabel,SubmitBtn,Canvas1,btn1,btn2,btn3,btn4,btn5,backBtn
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    SubmitBtn.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#aef35a",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="DASHBOARD", fg='black', font='helvetica 12 bold')
    headingLabel.place(relx=0.25,rely=0.15, relwidth=0.5, relheight=0.5)

    btn1 = Button(root,text="View Books",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=View)
    btn1.place(relx=0.28,rely=0.35, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Search Book",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=searchBook)
    btn2.place(relx=0.28,rely=0.45, relwidth=0.45,relheight=0.1)

    backBtn = Button(root,text="Back",bg='#f2f2f4', fg='black', command=Student)
    backBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)


# Adding Employee In Database
def gettingEmpDetails():

    EmpId = en1.get()
    name = en2.get()
    password = en3.get()
    dept = en4.get()
    doj = en5.get()
    sal = en6.get()

    try:
        if (type(int(EmpId)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Employee ID should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Employee ID should be an integer")
        return

    try:
        if (type(float(sal)) == float or type(int(sal)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Salary should be a float/int value")
            return
    except:
        messagebox.showinfo("Invalid Value","Salary should be a float/int value")
        return

    sql = "insert into "+empTable+" values ('"+EmpId+"','"+name+"','"+password+"','"+dept+"','"+doj+"','"+sal+"')"
    try:
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showinfo("Error!","Cannot add data to Database")

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)

# Adding Student In Database
def gettingStuDetails():

    Rollno = en1.get()
    name = en2.get()
    password = en3.get()
    dept = en4.get()
    sem = en5.get()
    batch = en6.get()

    try:
        if (type(int(Rollno)) == int):
            pass
        else:
            messagebox.showinfo("Invalid Value","Roll number should be an integer")
            return
    except:
        messagebox.showinfo("Invalid Value","Roll number should be an integer")
        return


    sql = "insert into "+stuTable+" values ('"+Rollno+"','"+name+"','"+password+"','"+dept+"','"+sem+"','"+batch+"')"
    try:
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showinfo("Error!","Cannot add data to Database")

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)

# Checking Login Credentials From Database
def gettingLoginDetails():

    login = en1.get()
    name = en2.get()
    password = en3.get()
    role = en4.get()
    role.lower()

    if (role == 'emp'):
        sqlLoginID = "select empid from "+empTable+" where password = '"+password+"'"
        sqlName = "select name from "+empTable+" where password = '"+password+"'"

        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]

            if(getLoginID == login and getName == name):
                empMenu()
                messagebox.showinfo("Success","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("Failure","Please check your credentials")
    elif (role == 'stu'):
        sqlLoginID = "select rollno from "+stuTable+" where password = '"+password+"'"
        sqlName = "select name from "+stuTable+" where password = '"+password+"'"

        try:
            cur.execute(sqlLoginID)
            for i in cur:
                getLoginID = i[0]
            cur.execute(sqlName)
            for i in cur:
                getName = i[0]

            if(getLoginID == login and getName == name):
                stuMenu()
                messagebox.showinfo("Success","You have successfully logged in")
            else:
                messagebox.showerror("Failure","Can't log in, check your credentials")
        except:
            messagebox.showinfo("Failure","Please check your credentials")
    else:
        messagebox.showinfo("Exception","Role can only be emp or stu")
        return


    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)

# Employee Registration
def EmpRegister():

    global labelFrame

    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()

    global en1,en2,en3,en4,en5,en6

    labelFrame = Frame(root,bg='#aef35a')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)

    # Employee ID
    lb1 = Label(labelFrame,text="User ID : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb1.place(relx=0.05,rely=0.05)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)

    #Employee Name
    lb2 = Label(labelFrame,text="Name : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb2.place(relx=0.05,rely=0.2)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)

    #Employee Paswword
    lb3 = Label(labelFrame,text="Password : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb3.place(relx=0.05,rely=0.35)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)

    #Employee Department
    lb4 = Label(labelFrame,text="Department : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb4.place(relx=0.05,rely=0.5)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.5, relwidth=0.62)

    #Employee Date of Joining
    lb5 = Label(labelFrame,text="DOJ : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb5.place(relx=0.05,rely=0.65)

    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.65, relwidth=0.62)

    # Employee Salary
    lb5 = Label(labelFrame,text="Salary : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb5.place(relx=0.05,rely=0.8)

    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.8, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=gettingEmpDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)


# Login both for Employee and Student
def Login():

    global labelFrame

    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()

    global en1,en2,en3,en4,SubmitBtn,btn1,btn2

    labelFrame = Frame(root,bg='#aef35a')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.3)

    # Login ID
    lb1 = Label(labelFrame,text="User ID : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb1.place(relx=0.05,rely=0.1)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)

    # Name
    lb2 = Label(labelFrame,text="Name : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb2.place(relx=0.05,rely=0.3)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.3, relwidth=0.62)

    # Password
    lb3 = Label(labelFrame,text="Password : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb3.place(relx=0.05,rely=0.5)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.5, relwidth=0.62)

    # Role
    lb4 = Label(labelFrame,text="Role: ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb4.place(relx=0.05,rely=0.7)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.7, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=gettingLoginDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Registration
def studentRegister():

    global labelFrame

    global count
    count += 1

    if(count>=2):
        labelFrame.destroy()

    global en1,en2,en3,en4,en5,en6

    labelFrame = Frame(root,bg='#aef35a')
    labelFrame.place(relx=0.2,rely=0.44,relwidth=0.6,relheight=0.42)

    # Student Roll no
    lb1 = Label(labelFrame,text="User ID : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb1.place(relx=0.05,rely=0.05)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.05, relwidth=0.62)

    # Sudent Name
    lb2 = Label(labelFrame,text="Name : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb2.place(relx=0.05,rely=0.2)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.2, relwidth=0.62)

    # Student Password
    lb3 = Label(labelFrame,text="Password : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb3.place(relx=0.05,rely=0.35)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.35, relwidth=0.62)

    # Student Department
    lb4 = Label(labelFrame,text="Dept : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb4.place(relx=0.05,rely=0.5)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.5, relwidth=0.62)

     # Student Semester
    lb5 = Label(labelFrame,text="Semester : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb5.place(relx=0.05,rely=0.65)

    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.65, relwidth=0.62)

    # Student Batch
    lb6 = Label(labelFrame,text="Batch : ", bg='#aef35a', fg='black', font='helvetica 10 bold')
    lb6.place(relx=0.05,rely=0.8)

    en6 = Entry(labelFrame)
    en6.place(relx=0.3,rely=0.8, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=gettingStuDetails)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

# Employee Home Page
def Employee():

    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#aef35a",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="HELLO  EMPLOYEE", fg='black',font='helvetica 12 bold')
    headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)

    btn1 = Button(root,text="Register",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=EmpRegister)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)

    btn2 = Button(root,text="Login",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)

    btn3 = Button(root,text="Quit",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Student Home Page
def Student():

    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    Canvas1.destroy()
    btn1.destroy()
    btn2.destroy()

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#aef35a",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="HELLO  STUDENT", font='helvetica 12 bold',fg='black')
    headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)

    btn1 = Button(root,text="Register",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=studentRegister)
    btn1.place(relx=0.28,rely=0.3, relwidth=0.2,relheight=0.1)

    btn2 = Button(root,text="Login",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=Login)
    btn2.place(relx=0.53,rely=0.3, relwidth=0.2,relheight=0.1)

    btn3 = Button(root,text="Quit",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=root.quit)
    btn3.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

# Take n greater than 0.25 and less than 5
same=True
n=0.3

# Adding a background image
background_image =Image.open("library_2.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(350,400,image = img)
Canvas1.config(bg="#aef35a",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#000000",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="WELCOME TO LIBRARY", fg='black', font='helvetica 13 bold')
headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)

btn1 = Button(root,text="Employee",bg='#f2f2f4', fg='black', font='helvetica 14 bold', command=Employee)
btn1.place(relx=0.25,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="Student",bg='#f2f2f4', fg='black', font='helvetica 14 bold', command=Student)
btn2.place(relx=0.55,rely=0.3, relwidth=0.2,relheight=0.1)

root.mainloop()
