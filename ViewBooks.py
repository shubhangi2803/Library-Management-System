from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "shubhu" #Database password
mydatabase="library"  #Database name

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

bookTable = "books" #Book Table

def View():

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

    Canvas1.config(bg="#aef35a",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    labelFrame = Frame(root,bg='#aef35a')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    headingFrame1 = Frame(root,bg="#000000",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingFrame2 = Frame(headingFrame1,bg="#f2f2f4")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="VIEW BOOKS", fg='black', font='helvetica 12 bold')
    headingLabel.place(relx=0.25,rely=0.2, relwidth=0.5, relheight=0.5)


    y = 0.25

    Label(labelFrame, text="%-10s%-30s%-20s%-30s%-20s"%('BID','Title','Subject','Author','Status'),bg='#aef35a',fg='black', font='helvetica 10 bold').place(relx=0.08,rely=0.1)
    getBooks = "select * from "+bookTable
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-30s%-20s%-30s%-20s"%(i[0],i[1],i[2],i[3],i[4]),bg='#aef35a',fg='black', font='helvetica 10').place(relx=0.09,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Bad Format!","Can't fetch files from database")

    root.mainloop()
