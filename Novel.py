from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
#Functions
import sqlite3 as sq
con = sq.connect("/Users/apple/Documents/GitHub/novel-tkinter-project-khanhnguyen21/DBNovel.db")
c = con.cursor()

def getNovel():
    novel = c.execute("SELECT Title, AuthorName FROM Book, Author, Wrote WHERE Book.ISBN = Wrote.ISBN AND Wrote.AuthorID = Author.AuthorID")
    data = c.fetchall()
    return data

def insertNovel(NovelName, Author, BookPrice, BookGenre):
    if NovelName and Author and BookPrice and BookGenre:
        try:
            insertAuthor = c.execute("INSERT INTO Author(AuthorName)Values(?)",(str(Author),))
            insertNovel = c.execute("INSERT INTO Book(Title, Price, Genre) Values(?, ?, ?)",(str(NovelName), int(BookPrice), str(BookGenre)))
            insertWrote = c.execute("INSERT INTO Wrote(AuthorID, ISBN)Values((SELECT MAX(AuthorID) FROM AUTHOR), (SELECT MAX(ISBN) FROM Book))")
            con.commit()
            messagebox.showinfo('Success', 'Data entered successfully')
        except ValueError:
            messagebox.showinfo('Error', 'Price not numeric. Please fix them.')
        except:
            messagebox.showinfo('Error', 'Unexpected error')
    else:
        messagebox.showinfo('Error', 'Please enter some data.')

#UI
def root():
    window = Tk()
    window.title("Novel Application")
    window.geometry("200x100")
    nList = Button(window, text="Novel List", command = listNovelWindow)
    nList.pack()

    inNovel = Button(window, text="Add Novel", command = addNovelWindow)
    inNovel.pack()

    ext = Button(window, text="Exit", command = lambda:endProgram(window))
    ext.pack()
    window.mainloop()

def endProgram(w):
    con.close()
    w.destroy()

def listNovelWindow():
    novels = getNovel()
    tbl = ""
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += "|"
        tbl += "\n"
        tbl += "\n"
    messagebox.showinfo("Novel List", tbl)

def addNovelWindow():
    addNovel = Tk()
    addNovel.title("Add Novel")
    addNovel.geometry("200x300")

    addNovelFrame = Frame(addNovel)
    addNovelFrame.pack(side = LEFT)

    novelTitle = tk.StringVar(addNovel)
    novelAuthor = tk.StringVar(addNovel)
    authorChoices = {'Haruki Murakami', 'Karl Popper', 'Yukio Mishima', 'Fyodor Dostoyevsky', "Marxim Gorky"}
    novelAuthor.set('Karl Popper')
    novelPrice = tk.StringVar(addNovel)
    novelGenre = tk.StringVar(addNovel)
    
    lblT = Label(addNovelFrame, text = 'Enter a novel title').pack()
    title = Entry(addNovelFrame, text = 'Novel Title Here', textvariable = novelTitle).pack()
    
    lblA = Label(addNovelFrame, text = 'Select the author').pack()
    author = OptionMenu(addNovelFrame, novelAuthor, *authorChoices).pack()

    lblP = Label(addNovelFrame, text = 'Enter the price').pack()
    author = Entry(addNovelFrame, text = 'Novel Price Here', textvariable = novelPrice).pack()

    lblG = Label(addNovelFrame, text = 'Enter the genre').pack()
    author = Entry(addNovelFrame, text = 'Novel Genre Here', textvariable = novelGenre).pack()
    
    add = Button(addNovelFrame, text="Add",
                 command = lambda: insertNovel(novelTitle.get(), novelAuthor.get(), novelPrice.get(), novelGenre.get())).pack()
    
    addNovel.mainloop()

root()

