import sqlite3
from class_book import Book
from borrower_class import Borrower


class Database:

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
    
    def create_tables(self):
        self.c.execute("""CREATE TABLE books (
                    book_id integer(20) primary key not null,
                    book_name varchar(255),
                    author varchar(255),
                    category varchar(20),
                    price integer(20),
                    in_stock integer(20)
                    )""")
        self.c.execute("""CREATE TABLE borrowers (
                    borrower_name varchar(255),
                    borrower_id integer(20) primary key not null,
                    book_id integer(20),
                    issue_date varchar(20),
                    FOREIGN KEY (book_id) REFERENCES books(book_id)
                    )""")
        self.conn.commit()    


    def add_book(self, book):
        with self.conn:
            self.c.execute("INSERT INTO books VALUES (:book_id, :book_name, :author, :category, :price, :in_stock)", 
                {'book_id': book.book_id, 'book_name': book.book_name, 'author': book.author, 'category': book.category, 'price': book.price, 'in_stock': book.in_stock})


    def issue_book(self, borrower):
        with self.conn:
            self.c.execute("INSERT INTO borrowers VALUES (:borrower_name, :borrower_id, :book_id, :issue_date)",
                {'borrower_name' : borrower.borrower_name, 'borrower_id' : borrower.borrower_id, 'book_id' : borrower.book_id, 'issue_date' : borrower.issue_date})        

    
    def display_book(self):
        with self.conn:
            self.c.execute("SELECT * FROM books")
        return self.c.fetchall()


    def display_borrower(self):
        with self.conn:
            self.c.execute("SELECT * FROM borrowers")
        return self.c.fetchall()    


    def update(self, book, price, in_stock):
        with self.conn:
            self.c.execute("""UPDATE books SET price = :price, in_stock = :in_stock 
                        WHERE book_id = :book_id""",
                    {'book_id': book.book_id, 'price': price, 'in_stock': in_stock})


    def remove_book(self,book):
        with self.conn:
            self.c.execute("DELETE from books WHERE book_id = :book_id",
                    {'book_id': book.book_id})

    
    def return_book(self,borrower):
        with self.conn:
            self.c.execute("DELETE from borrowers WHERE book_id = :book_id AND borrower_id = :borrower_id",
                  {'book_id': borrower.book_id, 'borrower_id': borrower.borrower_id})


    def display_search_book(self,search_by,search_text):
        print(search_by)
        print(search_text)

        with self.conn:
            self.c.execute("SELECT * FROM books WHERE " + str(search_by)+" LIKE "+ "\'%"+str(search_text)+"%\'")
        return self.c.fetchall()

        

    
    def __del__(self):
        self.conn.close()






