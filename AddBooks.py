from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql



def bookRegister():

    bid = en1.get()
    title = en2.get()
    subject = en3.get()
    author = en4.get()
    status = en5.get()
    status = status.lower()

    insertBooks = "insert into "+bookTable+" values('"+bid+"','"+title+"','"+subject+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
    except:
        messagebox.showinfo("Error!","Can't add data into Database")

    en1.delete(0, END)
    en2.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)


def addBooks():

    global en1,en2,en3,en4,en5,Canvas1,con,cur,bookTable,root

    root = Tk()
    root.title("Library_Manager")
    root.geometry("700x570")
    root.resizable(width=False,height=False)

    mypass = "lenovo@330" #Database password
    mydatabase="library"  #Database name

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    bookTable = "books" # Book Table

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


    Canvas1 = Canvas(root)

    Canvas1.config(bg="#b3d1ff",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    labelFrame = Frame(root,bg='#b3d1ff')
    labelFrame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)


    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='#b3d1ff', fg='black', font='helvetica 10 bold')
    lb1.place(relx=0.05,rely=0.1)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.1, relwidth=0.62)

    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='#b3d1ff', fg='black', font='helvetica 10 bold')
    lb2.place(relx=0.05,rely=0.25)

    en2 = Entry(labelFrame)
    en2.place(relx=0.3,rely=0.25, relwidth=0.62)

    # Book Subject
    lb3 = Label(labelFrame,text="Subject : ", bg='#b3d1ff', fg='black', font='helvetica 10 bold')
    lb3.place(relx=0.05,rely=0.4)

    en3 = Entry(labelFrame)
    en3.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Book Author
    lb4 = Label(labelFrame,text="Author : ", bg='#b3d1ff', fg='black', font='helvetica 10 bold')
    lb4.place(relx=0.05,rely=0.55)

    en4 = Entry(labelFrame)
    en4.place(relx=0.3,rely=0.55, relwidth=0.62)

    # Book Status
    lb5 = Label(labelFrame,text="Status(Avail/Issued) : ", bg='#b3d1ff', fg='black', font='helvetica 10 bold')
    lb5.place(relx=0.05,rely=0.75)

    en5 = Entry(labelFrame)
    en5.place(relx=0.3,rely=0.75, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#f2f2f4', fg='black',command=bookRegister, font='helvetica 12 bold')
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=root.quit)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
