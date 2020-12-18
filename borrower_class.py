class Borrower:
    

    def __init__(self, borrower_name, borrower_id, book_id, issue_date):
        self.borrower_name = borrower_name 
        self.borrower_id = borrower_id
        self.book_id = book_id
        self.issue_date = issue_date
      
    # @property
    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)

    # @property
    # def fullname(self):
    #     return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Borrower('{}', {}, {}, '{}')".format(self.borrower_name, self.borrower_id, self.book_id, self.issue_date)