import constants
from db import DB

class author:

    def __init__(self, db):
        self.db = db
        self.current_author = None

    def is_author(self, person_id):
        select_query = f"SELECT * from {constants.AUTHOR} where Person_idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return len(results) == 1

    def get_author_id(self, person_id):
        select_query = f"SELECT * from {constants.AUTHOR} where Person_idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return results[0][0]

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

    def login(self, author_id, person_id):
        person_select_query = f"SELECT * from Person where idPerson={person_id}"
        person_results = self.db.fetchAll(person_select_query)

        login_str = "Fname | Lname | email" + constants.EOD
        login_str += f"{person_results[0][1]} | {person_results[0][2]} | {person_results[0][3]}" + constants.EOD

        status_author = self.get_status(author_id)
        login_str += status_author
        self.current_author = author_id

        return login_str

    def get_status(self, author_id):
        if author_id is None and self.current_author is None:
            return ""
        if author_id is None:
            author_id = self.current_author
        manuscript_select_query = f"SELECT * from Manuscript where primary_author = {author_id}"
        manuscript_results = self.db.fetchAll(manuscript_select_query)

        status_author = "ManuscriptID | Status | Title" + constants.EOD
        for result in manuscript_results:
            status_author += (str(result[0]) + " | " + str(result[1]) + " | " + result[4] + constants.EOD)

        return status_author

    def insert_co_author(self, fname, lname, man_id, order):

        person_value_list = tuple([fname, lname])
        person_id = self.db.insert_if_not_exists(
            constants.PERSON, constants.PERSON_NAMES_VALUE_LIST, person_value_list
        )

        author_value_list = tuple([str(person_id)])
        author_id = self.db.insert_if_not_exists(
            constants.AUTHOR, constants.AUTHOR_PERSON_VALUE_LIST, author_value_list
        )

        author_order_value_list = tuple([str(man_id), str(author_id), str(order)])
        author_order_id = self.db.insert_if_not_exists(
            constants.AUTHOR_ORDER, constants.AUTHOR_ORDER_VALUE_LIST, author_order_value_list
        )

        if author_order_id is None:
            return False
        return True

    def submit_manuscript(self, input_list):
        if self.current_author is None:
            return constants.AUTHOR_NOT_LOGGED_IN

        icode_value_tuple = tuple([input_list[3]])
        icode_id = self.db.insert_if_not_exists(
            constants.ICODE, constants.ICODE_VALUE_LIST, icode_value_tuple
        )

        manuscript_title = input_list[1]
        status = 1

        manuscript_value_tuple = tuple(
            [str(status), str(icode_id), manuscript_title, str(self.current_author)]
        )
        manuscript_id = self.db.insert_if_not_exists(
            constants.MANUSCRIPT, constants.MANUSCRIPT_VALUE_LIST, manuscript_value_tuple
        )

        author_order = 1
        author_select = f"SELECT * FROM {constants.AUTHOR} join {constants.PERSON} on Person_idPerson = idPerson where idAuthor = {self.current_author}"
        author_results = self.db.fetchAll(author_select)

        self.insert_co_author(author_results[0][4],author_results[0][5], manuscript_id, author_order)
        author_order += 1
        for i in range(4,len(input_list)-1,2):
            fname = input_list[i]
            lname = input_list[i+1]
            if not self.insert_co_author(fname, lname, manuscript_id, author_order):
                print("Some error occured while storing co authors")
            author_order += 1

        return manuscript_id

    def logout(self):
        self.current_author = None


if __name__ == "__main__":
    db = DB()
    author = author(db)
    # print(author.register_author("Cardi", "B", "cardi.b@gmail.com", "Hollywood"))
    # print(author.get_author_id(1))
    # input_list = list(["submit", "DBMS", "1", "db"])
    # print(author.submit_manuscript(input_list))
    authors_list = list("1")
    input_list = list(["submit", "TT", "Dartmouth", "DB", "2", "3", "4", "file"])
    authors_list = authors_list + input_list[len(input_list) - 4:len(input_list) - 1]
    print(authors_list)
    db.close_connection()

