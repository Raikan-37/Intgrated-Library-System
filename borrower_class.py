class Borrower:
    

    def __init__(self, borrower_name, borrower_id, book_id, issue_date):
        self.borrower_name = borrower_name 
        self.borrower_id = borrower_id
        self.book_id = book_id
        self.issue_date = issue_date

    def __repr__(self):
        return "Borrower('{}', {}, {}, '{}')".format(self.borrower_name, self.borrower_id, self.book_id, self.issue_date)
