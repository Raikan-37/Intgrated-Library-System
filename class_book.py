class Book:
    

    def __init__(self, book_id, book_name, author, category, price, in_stock):
        self.book_id = book_id 
        self.book_name = book_name
        self.author = author
        self.category = category
        self.price = price
        self.in_stock = in_stock

    def __repr__(self):
        return "Book({}, '{}', '{}', '{}', '{}', {}, {})".format(self.book_id, self.book_name, self.author, self.category, self.price, self.in_stock)
