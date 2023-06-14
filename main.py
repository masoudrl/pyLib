import tkinter as tk
from tkinter import ttk
import sqlite3
root= tk.Tk()
root.geometry('800x500')
root.resizable(False, False)
root.title('PyLib')

#create register new book window
def registerNewBookWindow():
    new= tk.Toplevel(root)
    new.geometry('500x500')
    new.title('Register New Book')
    new.resizable(False, False)
    new.iconbitmap('pics/reg-icon.ico')
    #Define items in new window
    fontConf= 'arial 12'
    booknameLabel= tk.Label(new, text='Book name: ', font=(fontConf))
    booknameInput= tk.Text(new, height=1,width=12)
    authornameLabel= tk.Label(new, text='Author: ', font=(fontConf))
    authornameInput= tk.Text(new, height=1,width=12)
    publisherLabel= tk.Label(new, text='Publisher: ', font=(fontConf))
    publisherInput= tk.Text(new, height=1,width=12 )
    publishyearLabel= tk.Label(new, text='Publish year: ', font=(fontConf))
    publishyearInput= tk.Text(new, height=1,width=12 )
    inStockCountLabel= tk. Label(new, text='Nr Available: ', font=(fontConf))
    inStockCounInput= tk.Text(new, height=1,width=12)
    # bookIdLabel= tk.Label(new, text='Book ID: ', font=(fontConf))
    # bookIdInput= tk.Text(new, width=12, height=1)
    ageClassificationLabel= tk.Label(new, text='Ages: ', font=(fontConf))
    ageMenu= tk.StringVar()
    ageMenu.set('Select')
    ageClassificationInput= tk.OptionMenu(new, ageMenu,"Children","Youth","Adult")
    genreLabel= tk.Label(new, text='Genre: ', font=(fontConf))
    genreMenu= tk.StringVar()
    genreMenu.set('Select')
    genreInput= tk.OptionMenu(new, genreMenu,"literature","historical","economic","poetry")
    pageNumbersLabel= tk.Label(new, text='Page Numbers:', font=(fontConf))
    pageNumbersInput= tk.Text(new, width=12, height=1)
    #submit button
    def submitted():
        book_fill= str(booknameInput.get("1.0",'end-1c'))
        author_fill= str(authornameInput.get("1.0",'end-1c'))
        pub_fill= str(publisherInput.get("1.0",'end-1c'))
        puby_fill= int(publishyearInput.get("1.0",'end-1c'))
        pn_fill= int(pageNumbersInput.get("1.0",'end-1c'))
        gen_fill= str(genreMenu.get())
        ac_fill= str(ageMenu.get())
        sc_fill= int(inStockCounInput.get("1.0",'end-1c'))
        all_fill= book_fill and author_fill and pub_fill and puby_fill and pn_fill and sc_fill and ac_fill and gen_fill
                
        
        if all_fill:
            conn2= sqlite3.connect('lib.db')
            c=conn2.cursor()
            nb= Book(bookname= book_fill,
                     author= author_fill,
                     publisher= pub_fill,
                     in_stock_count= sc_fill,
                     genre=gen_fill,
                     age_classification= ac_fill,
                     number_pages= pn_fill,
                     publish_year= puby_fill)
            c.execute("""INSERT INTO books (book_name, author, publisher, stock_count, genre,
            age_class, number_page, publish_year )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(nb.bookname,nb.author,nb.publisher,
                                                nb.in_stock_count, nb.genre, nb.age_classification,
                                                nb.number_pages, nb.publish_year))
            conn2.commit()
            conn2.close()
            submittedLabel= tk.Label(new, text="Submitted "+book_fill+" book successfully.")
            submittedLabel.place(x=170,y=280)
    submitButton= tk.Button(new, text='Submit', bg='#16a085', font=(fontConf),
                            fg='#ecf0f1', width=6, command=submitted)
    

    #grid new window
    #line 1
    booknameLabel.grid(row=0, column=0, pady=20, padx=(20,0))
    booknameInput.grid(row=0, column=1, pady=20)
    authornameLabel.grid(row=0, column=2, pady=20, padx=(40,0))
    authornameInput.grid(row=0, column=3, pady=20)
    #line 2
    publisherLabel.grid(row=1, column=0, pady=20, padx=(20,0))
    publisherInput.grid(row=1, column=1, pady=20)
    publishyearLabel.grid(row=1, column=2, pady=20, padx=(40,0))
    publishyearInput.grid(row=1, column=3, pady=20)
    #line3
    inStockCountLabel.grid(row=2, column=0, pady=20, padx=(20,0))
    inStockCounInput.grid(row=2, column=1, pady=20)
    pageNumbersLabel.grid(row=2, column=2, pady=20, padx=(40,0))
    pageNumbersInput.grid(row=2, column=3, pady=20)
    #line 4
    ageClassificationLabel.grid(row=3, column=0, pady=20, padx=(20,0))
    ageClassificationInput.grid(row=3, column=1, pady=20)
    genreLabel.grid(row=3, column=2, pady=20, padx=(40,0))
    genreInput.grid(row=3, column=3, pady=20)
    #line 5
    # pageNumbersLabel.grid(row=4, column=0, pady=20, padx=(20,0))
    # pageNumbersInput.grid(row=4, column=1, pady=20)
    submitButton.grid(row=4, column=0, pady=20, padx=(30,0))
#create Database and Tables
conn= sqlite3.connect('lib.db')
c=conn.cursor()
'''
booksTable= """CREATE TABLE books(
             book_id INTEGER PRIMARY KEY AUTOINCREMENT,
             book_name varchar(100) NOT NULL,
             author varchar(100) NOT NULL,
             publisher varchar(100) NOT NULL,
             stock_count int NOT NULL,
             genre varchar(100) NOT NULL,
             age_class varchar(100) NOT NULL,
             number_page int NOT NULL,
             publish_year int NOT NULL)"""

c.execute(booksTable)

c.execute("""INSERT INTO books
            (book_name, author, publisher, stock_count, genre, age_class, number_page, publish_year )
            VALUES ('sample book1','sample author1','sample publisher1',5,'poem','adult',48,2005)
            """)
'''
conn.commit()
conn.close()
#define icon
root.iconbitmap('pics\icon.ico')
#define image
bg= tk.PhotoImage(file="pics/wp2.png")
#create label
myLabel= tk.Label(root, image=bg)
myLabel.place(x=0, y=0, relheight=1, relwidth=1)
#create frames
menuFrame= tk.Frame(root)
mainFrame= tk.Frame(root)
#create menu frame
fgColorCode='#2d3436'
bgColorCode='#74b9ff'
fontConfig='arial 16'
registerNewBook= tk.Button(menuFrame, text='ثبت کتاب جدید',bg= bgColorCode,
                           fg= fgColorCode, font=fontConfig, width= 9,
                           justify=tk.RIGHT, command=registerNewBookWindow)
registerNewBook.grid(row=0, column=5)

bookLists= tk.Button(menuFrame, text='لیست کتاب ها',bg= bgColorCode,
                           fg= fgColorCode, font=fontConfig, width= 9,
                           justify=tk.RIGHT)
bookLists.grid(row=0, column=4)

loanedBooks= tk.Button(menuFrame, text='کتب امانت داده شده',bg= bgColorCode,
                           fg= fgColorCode, font=fontConfig, width= 11,
                           justify=tk.RIGHT)
loanedBooks.grid(row=0, column=3)

registerNewUser= tk.Button(menuFrame, text='ثبت عضو جدید',bg= bgColorCode,
                           fg= fgColorCode, font=fontConfig, width= 9,
                           justify=tk.RIGHT)
registerNewUser.grid(row=0, column=2)

usersList= tk.Button(menuFrame, text='مشاهده اعضا',bg= bgColorCode,
                           fg= fgColorCode, font=fontConfig, width= 9,
                           justify=tk.RIGHT)
usersList.grid(row=0, column=1)

newLoanBook= tk.Button(menuFrame, text='ثبت امانت جدید',bg= bgColorCode,
                           fg= fgColorCode, font=fontConfig, width= 9,
                           justify=tk.RIGHT)
newLoanBook.grid(row=0, column=0)

menuFrame.pack(pady=20)
root.mainloop()