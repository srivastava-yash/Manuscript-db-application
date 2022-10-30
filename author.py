import constants
from db import DB

class author:

    def __init__(self, db):
        self.db = db

    def register_author(self, fname, lname, email, affiliation):
        person_value_tuple = tuple([fname, lname, email])
        person_id = self.db.insert_if_not_exists(constants.PERSON, constants.PERSON_VALUE_LIST, person_value_tuple)

        affiliation_value_tuple = tuple([affiliation])
        affiliation_id = self.db.insert_if_not_exists(
            constants.AFFILIATION, constants.AFFILIATION_VALUE_LIST, affiliation_value_tuple
        )

        author_value_tuple = tuple([str(affiliation_id), str(person_id)])
        author_id = self.db.insert_if_not_exists(constants.AUTHOR, constants.AUTHOR_VALUE_LIST, author_value_tuple)

        return author_id



if __name__ == "__main__":
    db = DB()
    author_utility = author(db)
    print(author_utility.register_author("Cardi", "B", "cardi.b@gmail.com", "Hollywood"))
    db.close_connection()

