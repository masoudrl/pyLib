import tkinter as tk
from tkinter import messagebox
from main import registerNewBook
class Book:
    def __init__(self, bookname, author, publisher, publish_year,
                 in_stock_count,genre,age_classification, number_pages,
                 book_id=None,loaned_count=0):
        self.bookname= bookname
        self.author= author
        self.publisher= publisher
        self.publish_year= publish_year
        self.in_stock_count= in_stock_count
        self.loaned_count= loaned_count
        self.genre= genre
        self.book_id= book_id
        self.age_classification= age_classification
        self.number_pages= number_pages
    #setter and getter bookname
    @property
    def bookname(self):
        return self.__bookname
    @bookname.setter
    def bookname(self, bookname):
        if isinstance(bookname, str) and 0<len(bookname)<=10:
            self.__bookname= bookname
        else:
            messagebox.showerror("Error","Errrrrrrrror!!!!")
            # error_message="error"
            # print(error_message)
    
    #setter and getter author
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self, author):
        if isinstance(author, str) and 0<len(author)<=100:
            self.__author= author
        else:
            error_message="error"
            print(error_message)
    
    #setter and getter publisher
    @property
    def publisher(self):
        return self.__publisher
    @publisher.setter
    def publisher(self, publisher):
        if isinstance(publisher, str) and 0<len(publisher)<=100:
            self.__publisher= publisher
        else:
            error_message="error"
            print(error_message)

    #setter and getter publish_year
    @property
    def publish_year(self):
        return self.__publish_year
    @publish_year.setter
    def publish_year(self, publish_year):
        import datetime
        today = datetime.date.today()
        year = today.year
        if isinstance(publish_year, int) and 0<publish_year<=year:
            self.__publish_year= publish_year
        else:
            error_message="There is no such year."
            return error_message

    #setter and getter in_stock_count
    @property
    def in_stock_count(self):
        return self.__in_stock_count
    @in_stock_count.setter
    def in_stock_count(self, in_stock_count):
        if isinstance(in_stock_count, int):
            self.__in_stock_count= in_stock_count
        else:
            error_message="error"
            print(error_message)

    #setter and getter loaned_count
    '''
    @property
    def loaned_count(self):
        return self.__loaned_count
    @loaned_count.setter
    def loaned_count(self, loaned_count):
        if isinstance(loaned_count, int) and 0<=loaned_count<=100:
            self.__loaned_count= loaned_count
        else:
            error_message="error"
            print(error_message)
    '''
    #setter and getter number_pages
    @property
    def number_pages(self):
        return self.__number_pages
    @number_pages.setter
    def number_pages(self, number_pages):
        if isinstance(number_pages, int):
            self.__number_pages= number_pages
        else:
            error_message="error"
            print(error_message)

    #setter and getter genre
    @property
    def genre(self):
        return self.__genre
    @genre.setter
    def genre(self, genre):
        genres=["literature","historical","economic","poetry"]
        if genre in genres:
            self.__genre= genre
        else:
            error_message="error"
            print(error_message)

    #setter and getter book_id
    '''
    @property
    def book_id(self):
        return self.__book_id
    @book_id.setter
    def book_id(self, book_id):
        if isinstance(book_id, int) and 0<book_id<=10000:
            self.__book_id= book_id
        else:
            error_message="error"
            print(error_message)
    '''
    #setter and getter age_classification
    @property
    def age_classification(self):
        return self.__age_classification
    @age_classification.setter
    def age_classification(self, age_classification):
        age_classifications=["Children","Youth","Adult"]
        if age_classification in age_classifications:
            self.__age_classification= age_classification
        else:
            error_message="error"
            print(error_message)

    def __str__(self):
        return f"book name:{self.bookname}"
    def __repr__(self):
        return self.__str__()

# b1= Book('bookkk','ali','ney',1400,5,0,'رمان',1,'بزرگسال',100)
# print(b1)