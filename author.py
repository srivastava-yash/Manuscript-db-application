import constants
from db import DB

class AuthorUtilty:
    def __int__(self, db):
        self.db = db

    def register_author(self, fname, lname, email, affiliation):
        query_to_check_person = f"SELECT * from Person where fname = '{fname}' and lname = '{lname}' and email = '{email}'"
        results = self.db.fetchAll(query_to_check_person)
        if len(results) == 0:
            pass

