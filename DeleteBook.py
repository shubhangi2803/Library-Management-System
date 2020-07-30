from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "lenovo@330" #Database password
mydatabase="library"  #Database name

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" #Book Table


def deleteBook():

    bid = en1.get()

    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
    except:
        messagebox.showinfo("Check Credentials!","Please check Book ID")

    en1.delete(0, END)


def delete():

    global en1,en2,en3,en4,en5,Canvas1,con,cur,bookTable,root

    root = Tk()
    root.title("Library_Manager")
    root.geometry("700x570")
    root.resizable(width=False,height=False)


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
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.3)

    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="DELETE BOOK", fg='black', font='helvetica 12 bold')
    headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)

    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='#b3d1ff', fg='black', font='helvetica 10 bold')
    lb2.place(relx=0.05,rely=0.5)

    en1 = Entry(labelFrame)
    en1.place(relx=0.3,rely=0.5, relwidth=0.62)

    #Submit Button
    SubmitBtn = Button(root,text="Submit",bg='#f2f2f4', fg='black', font='helvetica 12 bold',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.75, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#f2f2f4', fg='black', font='helvetica 12 bold', command=root.quit)
    quitBtn.place(relx=0.53,rely=0.75, relwidth=0.18,relheight=0.08)

    root.mainloop()
