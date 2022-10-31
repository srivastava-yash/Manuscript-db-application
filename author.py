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

    def login(self, author_id):
        author_select_query = f"SELECT * from Author where idAuthor = {author_id}"
        author_results = self.db.fetchAll(author_select_query)
        person_id = author_results[0][2]

        person_select_query = f"SELECT * from Person where idPerson={person_id}"
        person_results = self.db.fetchAll(person_select_query)

        login_str = "Fname | Lname | email" + constants.EOD
        login_str += f"{person_results[0][1]} | {person_results[0][2]} | {person_results[0][3]}" + constants.EOD

        status_author = self.get_status(author_id)
        login_str += status_author

        return login_str

    def get_status(self, author_id):
        manuscript_select_query = f"SELECT * from Manuscript where primary_author = {author_id}"
        manuscript_results = self.db.fetchAll(manuscript_select_query)

        status_author = "ManuscriptID | Status | Title" + constants.EOD
        for result in manuscript_results:
            status_author += (str(result[0]) + " | " + str(result[1]) + " | " + result[4] + constants.EOD)

        return status_author



if __name__ == "__main__":
    db = DB()
    author_utility = author(db)
    # print(author_utility.register_author("Cardi", "B", "cardi.b@gmail.com", "Hollywood"))
    print(author_utility.login(1))
    db.close_connection()

