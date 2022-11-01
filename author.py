import constants
from db import DB

class author:

    def __init__(self, db):
        self.db = db
        self.current_author = None

    def is_athor(self, person_id):
        select_query = f"SELECT * from {constants.AUTHOR} where Person.idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return len(results) == 1

    def register_author(self, fname, lname, email, affiliation):
        person_value_tuple = tuple([fname, lname, email])
        person_id = self.db.insert_if_not_exists(constants.PERSON, constants.PERSON_VALUE_LIST, person_value_tuple)

        affiliation_value_tuple = tuple([affiliation])
        affiliation_id = self.db.insert_if_not_exists(
            constants.AFFILIATION, constants.AFFILIATION_VALUE_LIST, affiliation_value_tuple
        )

        author_value_tuple = tuple([str(affiliation_id), str(person_id)])
        author_id = self.db.insert_if_not_exists(constants.AUTHOR, constants.AUTHOR_VALUE_LIST, author_value_tuple)

        return person_id

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
        self.current_author = author_id

        return login_str

    def get_status(self, author_id):
        manuscript_select_query = f"SELECT * from Manuscript where primary_author = {author_id}"
        manuscript_results = self.db.fetchAll(manuscript_select_query)

        status_author = "ManuscriptID | Status | Title" + constants.EOD
        for result in manuscript_results:
            status_author += (str(result[0]) + " | " + str(result[1]) + " | " + result[4] + constants.EOD)

        return status_author

    def submit_manuscript(self, input_list):
        if self.current_author is None:
            return constants.AUTHOR_NOT_LOGGED_IN

        icode_value_tuple = tuple([input_list[3]])
        icode_id = self.db.insert_if_not_exists(
            constants.ICODE, constants.ICODE_VALUE_LIST, icode_value_tuple
        )

        print(icode_id)

        affiliation_value_tuple = tuple([input_list[2]])
        affiliation_id = self.db.insert_if_not_exists(
            constants.AFFILIATION, constants.AFFILIATION_VALUE_LIST, affiliation_value_tuple
        )

        manuscript_title = input_list[1]
        status = 1

        manuscript_value_tuple = tuple(
            [str(status), str(icode_id), manuscript_title, str(self.current_author)]
        )
        manuscript_id = self.db.insert_if_not_exists(
            constants.MANUSCRIPT, constants.MANUSCRIPT_VALUE_LIST, manuscript_value_tuple
        )

        return manuscript_id


if __name__ == "__main__":
    db = DB()
    author = author(db)
    # print(author.register_author("Cardi", "B", "cardi.b@gmail.com", "Hollywood"))
    print(author.login(1))
    input_list = list(["submit", "DBMS", "1", "db"])
    print(author.submit_manuscript(input_list))
    db.close_connection()

