from tkinter import*
from tkinter import ttk
from sqlite3 import *
import os.path
from class_book import *
from borrower_class import *
from book_db_class import *
      

if os.path.isfile('libra.db') is False:
    db=Database('libra.db')
    db.create_tables()
else:
    db=Database('libra.db')



class main_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1350x700")
        self.root.maxsize(1350,700)

        #############
        #FRAMES Config
        #############

        #left frame for book inputs
        input_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#e6b8b8")
        input_frame.place(x=0,y=0,width=550,height=500)

        #left bottom frame for button input
        button_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#b8e6cf")
        button_frame.place(x=0,y=500,width=550,height=200)

        #right frame for book details
        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#e6b8b8")
        detail_frame.place(x=550,y=0,width=1000,height=700)


        
        ################### DETAIL FRAME CONETENTS ##################

        #display book frame in deatil frame
        display_books_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="#e6b8b8")
        display_books_frame.place(x=20,y=90,width=755,height=560)

        #display book frames view
        scroll_x=Scrollbar(display_books_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(display_books_frame,orient=VERTICAL)
        books_table=ttk.Treeview(display_books_frame,columns=("Book Id","Book Name","Author","Category","Price","Stock"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=books_table.xview)
        scroll_y.config(command=books_table.yview)
        books_table.heading("Book Id",text="Book Id")
        books_table.heading("Book Name",text="Book Name")
        books_table.heading("Author",text="Author")
        books_table.heading("Category",text="Category")
        books_table.heading("Price",text="Price")
        books_table.heading("Stock",text="Stock")
        books_table['show']='headings'
        books_table.column("Book Id",width=100)
        books_table.column("Book Name",width=150)
        books_table.column("Author",width=150)
        books_table.column("Category",width=150)
        books_table.column("Price",width=100)
        books_table.column("Stock",width=77)
        books_table.pack(fill=BOTH,expand=1)
        

        lable_search=Label(detail_frame,text="Search By",bg="#e6b8b8",font=("times new roman",16))
        lable_search.grid(row=0,column=0,pady=10,padx=10,sticky="w")


        search_by=StringVar()
        search_text=StringVar()
        combo_search=ttk.Combobox(detail_frame,width=10,font=("times new roman",12),state='readonly',textvariable=search_by)
        combo_search['values']=("book_id","book_name","author","category")
        combo_search.grid(row=0,column=2,pady=10,padx=10)

        txt_entry=Entry(detail_frame,width=20,textvariable=search_text)
        txt_entry.grid(row=0,column=3,padx=10,pady=10)

        # Functions

        def searching():
            #print(search_by.get())
            #print(search_text.get())     
            rows=db.display_search_book(search_by.get(),search_text.get())
            books_table.delete(*books_table.get_children())
            if len(rows)!=0:
                for row in rows:
                    books_table.insert('',END,values=row)
        
        
        def book_catalogue():
            display_book_data()
            

        # buttons in detail frame
        borr_btn=Button(detail_frame,text='Manage Borrower',width=15,height=2,command=issue_win)
        borr_btn.place(x=510,y=10)

        catal_btn=Button(detail_frame,text='Book Catalogue',width=15,height=2,command=book_catalogue)
        catal_btn.place(x=650,y=10)

        search_button=Button(detail_frame,text="Search",width=10,pady=5,command=searching)
        search_button.grid(row=0,column=4,padx=10,pady=10)


        ###############################################################################################
        ####----------------------------LEFT FRAME FOR BOOK ENTRY----------------------------------####
        ###############################################################################################
        

        #INPUT_FRAME {LABLES} && {ENTRY_BOX}
        book_name=Label(input_frame,text='Book Name',bg="#e6b8b8",font =('times new roman',13),pady=20)
        book_name.place(x=56,y=10)
        book_text=StringVar()
        book_entry=Entry(input_frame,textvariable=book_text)
        book_entry.place(x=180,y=30,width=250)

        book_id=Label(input_frame,text='Book ID',bg="#e6b8b8",font =('times new roman',13),pady=20)
        book_id.place(x=56,y=90)
        book_id_text=StringVar()
        book_id_entry=Entry(input_frame,textvariable=book_id_text)
        book_id_entry.place(x=180,y=110,width=250)

        author=Label(input_frame,text='Author ',bg="#e6b8b8",font =('times new roman',13),pady=20)
        author.place(x=56,y=170)
        author_text=StringVar()
        author_entry=Entry(input_frame,textvariable=author_text)
        author_entry.place(x=180,y=190,width=250)

        category=Label(input_frame,text='Category',bg="#e6b8b8",font =('times new roman',13),pady=20)
        category.place(x=56,y=250)
        category_text=StringVar()
        category_entry=Entry(input_frame,textvariable=category_text)
        category_entry.place(x=180,y=270,width=250)

        Price=Label(input_frame,text='Price',bg="#e6b8b8",font =('times new roman',13),pady=20)
        Price.place(x=56,y=330)
        price_text=StringVar()
        price_entry=Entry(input_frame,textvariable=price_text)
        price_entry.place(x=180,y=350,width=250)

        stock=Label(input_frame,text='Stock',bg="#e6b8b8",font =('times new roman',13),pady=20)
        stock.place(x=56,y=410)
        stock_text=StringVar()
        stock_entry=Entry(input_frame,textvariable=stock_text)
        stock_entry.place(x=180,y=430,width=250)
        

        ################################
        # Functions For Buttons        #
        ################################
            
        def display_book_data():        
            rows=db.display_book()
            books_table.delete(*books_table.get_children())
            if len(rows)!=0:
                for row in rows:
                    books_table.insert('',END,values=row)

        def add():
            bk=Book(book_id_text.get(),book_text.get(),author_text.get(),category_text.get(),price_text.get(),int(stock_text.get()))
            db.add_book(bk)
            display_book_data()
            #clear()
            print("BOOK ADDED...")
            

        def update_b():
            print("in update")
            bk=Book(book_id_text.get(),book_text.get(),author_text.get(),category_text.get(),price_text.get(),stock_text.get())
            print(price_text.get)
            db.update(bk,price_text.get(),stock_text.get())
            x=db.display_book()
            print(x) 
            print("updated")
            display_book_data()
            
        
        def remove():
            bk=Book(book_id_text.get(),book_text.get(),author_text.get(),category_text.get(),price_text.get(),int(stock_text.get()))
            db.remove_book(bk)
            x=db.display_book()
            print(x)

            display_book_data()
            print("BOOK REMOVED...")

        def clear():
            book_text.set("")
            book_id_text.set("")
            author_text.set("")
            category_text.set("")
            price_text.set("")
            stock_text.set("")
            print("Inputs Cleared...")

        def get_cursor(ev):
            cursor_row=books_table.focus()
            contents=books_table.item(cursor_row)
            row=contents['values']
            book_id_text.set(row[0])
            book_text.set(row[1])
            author_text.set(row[2])
            category_text.set(row[3])
            price_text.set(row[4])
            stock_text.set(row[5])
        
        books_table.bind("<ButtonRelease-1>",get_cursor)

        #adding buttons

        add_btn=Button(button_frame,text='Add Book',width=20,height=2,command=add)
        add_btn.place(x=40,y=20)

        update_btn=Button(button_frame,text='Update Book',width=20,height=2,command=update_b)
        update_btn.place(x=350,y=20)

        remove_btn=Button(button_frame,text='Remove Book',width=20,height=2,command=remove)
        remove_btn.place(x=40,y=100)

        clear_btn=Button(button_frame,text='Clear',width=20,height=2,command=clear)
        clear_btn.place(x=350,y=100)


class Issue:
    def __init__(self,root):
        self.root=root
        self.root.title("Manage Borrower")
        self.root.geometry("700x700+0+0")
       
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE)
        Manage_Frame.place(x=20,y=0,width=650,height=250)

        bor_name=StringVar()
        lbl_bor_name=Label(Manage_Frame,text="Borrower Name",font=("times new roman",15,"bold"),fg="black")
        lbl_bor_name.grid(row=0,column=0,pady=0,padx=5,sticky="w")

        txt_bor_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=bor_name)
        txt_bor_name.grid(row=0,column=3,pady=10,padx=20)

        bor_id=StringVar()
        lbl_bor_id=Label(Manage_Frame,text="Borrower Id",font=("times new roman",15,"bold"),fg="black")
        lbl_bor_id.grid(row=1,column=0,pady=0,padx=5,sticky="w")

        txt_bor_id=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=bor_id)
        txt_bor_id.grid(row=1,column=3,pady=10,padx=20)

        book_id=StringVar()
        lbl_book_id=Label(Manage_Frame,text="Book Id",font=("times new roman",15,"bold"),fg="black")
        lbl_book_id.grid(row=2,column=0,pady=0,padx=5,sticky="w")

        txt_book_id=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=book_id)
        txt_book_id.grid(row=2,column=3,pady=10,padx=20)

        issue_date=StringVar()
        lbl_issue_date=Label(Manage_Frame,text="Issue Date",font=("times new roman",15,"bold"),fg="black")
        lbl_issue_date.grid(row=3,column=0,pady=0,padx=5,sticky="w")

        txt_issue_date=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,textvariable=issue_date)
        txt_issue_date.grid(row=3,column=3,pady=10,padx=20)
        
        
        def display_borrower_data():
            borrower_table.delete(*borrower_table.get_children())
            rows=db.display_borrower()
            if len(rows)!=0:
                for row in rows:
                    borrower_table.insert('',END,values=row)

        def issues():
            br=Borrower(txt_bor_name.get(),txt_bor_id.get(),txt_book_id.get(),txt_issue_date.get())
            db.issue_book(br)
            display_borrower_data()
            print("issued")
        
        def return_bk():
            br=Borrower(txt_bor_name.get(),txt_bor_id.get(),txt_book_id.get(),txt_issue_date.get())
            db.return_book(br)
            display_borrower_data()
            print("returned...")

        

        issuebtn=Button(Manage_Frame,text="Issue book",width=10,command=issues)
        issuebtn.grid(row=3,column=7,padx=10,pady=0)

        returnbtn=Button(Manage_Frame,text="Return book",width=10,command=return_bk)
        returnbtn.grid(row=3,column=8,padx=10,pady=0)

        table_Frame=Frame(self.root,bd=4,relief=RIDGE)
        table_Frame.place(x=20,y=251,width=650,height=400)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)
        borrower_table=ttk.Treeview(table_Frame,columns=("Borrower Name","Borrower Id","Book Id","Issue Date"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=borrower_table.xview)
        scroll_y.config(command=borrower_table.yview)
        borrower_table.heading("Borrower Name",text="Borrower Name")
        borrower_table.heading("Borrower Id",text="Borrower Id")
        borrower_table.heading("Book Id",text="Book Id")
        borrower_table.heading("Issue Date",text="Issue Date")
        borrower_table['show']='headings'
        borrower_table.column("Borrower Name",width=100)
        borrower_table.column("Borrower Id",width=100)
        borrower_table.column("Book Id",width=100)
        borrower_table.column("Issue Date",width=100)
        borrower_table.pack(fill=BOTH,expand=1)


''' #This portion removed#
from tkinter import*
class return_book:
    def __init__(self,root):
        self.root=root
        self.root.title("RETURN BOOK")
        self.root.geometry("400x400")
        self.root.maxsize(400,200)

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,)
        Manage_Frame.place(x=0,y=0,width=400,height=200)

        bor_id=StringVar()
        book_id=StringVar()

        lbl_bor_id=Label(Manage_Frame,text="Borrower Id",font=("times new roman",15,"bold"),fg="black")
        lbl_bor_id.grid(row=0,column=0,pady=0,padx=5,sticky="w")

        txt_bor_id=Entry(Manage_Frame,font=("times new roman",15,"bold"),text=bor_id,bd=5,relief=GROOVE)
        txt_bor_id.grid(row=0,column=3,pady=10,padx=20)

        lbl_book_id=Label(Manage_Frame,text="Book Id",font=("times new roman",15,"bold"),fg="black")
        lbl_book_id.grid(row=1,column=0,pady=0,padx=5,sticky="w")

        txt_book_id=Entry(Manage_Frame,font=("times new roman",15,"bold"),text=book_id,bd=5,relief=GROOVE)
        txt_book_id.grid(row=1,column=3,pady=10,padx=20)


        #################################################################################################
        #functions
        #################################################################################################
        def return_bk():
            pass
        
        returnbtn=Button(Manage_Frame,text="return book",width=10,command=return_bk)
        returnbtn.place(x=20,y=150)        
'''


def issue_win():
	root=Tk()
	ob=Issue(root)
	root.mainloop()

''' #removed portion window #
def return_win():
    	root=Tk()
	ob=return_book(root)
	root.mainloop()
'''


