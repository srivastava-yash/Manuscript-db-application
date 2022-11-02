import constants
from db import DB

class reviewer:

    def __init__(self, db):
        self.db = db
        self.current_reviewer = None

    def is_reviewer(self, person_id):
        select_query = f"SELECT * from {constants.REVIEWER} where Person_idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return len(results) == 1


    def get_reviewer_id(self, person_id):
        select_query = f"SELECT * from {constants.REVIEWER} where Person_idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return results[0][0]


    def register_reviewer(self, fname, lname, icodes):
        person_name_tuple_list = tuple([fname, lname])
        person_id = self.db.insert_if_not_exists(
            constants.PERSON, constants.PERSON_NAMES_VALUE_LIST, person_name_tuple_list
        )

        reviewer_tuple_list = tuple([str(1), str(person_id)])
        reviewer_id = self.db.insert_if_not_exists(
            constants.REVIEWER, constants.REVIEWER_VALUE_LIST, reviewer_tuple_list
        )

        for icode in icodes:
            icode_value_tuple = tuple([icode])
            icode_id = self.db.insert_if_not_exists(
                constants.ICODE, constants.ICODE_VALUE_LIST, icode_value_tuple
            )

            reviewer_interest_value_tuple = tuple([reviewer_id, icode_id])
            ri_id = self.db.insert_if_not_exists(
                constants.REVIEWER_INTEREST, constants.REVIEWER_INTEREST_VALUE_LIST, reviewer_interest_value_tuple
            )

        return person_id

    def login(self, reviewer_id):
        reviewer_select_query = f"SELECT * FROM {constants.REVIEWER} join {constants.PERSON} " \
                                f"on Person_idPerson = idPerson where idReviewer = {reviewer_id}"
        reviewer_results = self.db.fetchAll(reviewer_select_query)

        if len(reviewer_results) == 0:
            return constants.REVIEWER_DNE

        manuscript_feedback_select_query = \
            f"SELECT * from {constants.MANUSCRIPT_FEEDBACK} join {constants.MANUSCRIPT} " \
            f"on Manuscript_idManuscript = idManuscript " \
            f"join {constants.MANUSCRIPT_STATUS} on status = idmanuscript_status " \
            f"where Reviewer_idReviewer = {reviewer_id} order by status"
        manuscript_results = self.db.fetchAll(manuscript_feedback_select_query)

        login_str = "fname | lname" + constants.EOD
        login_str += (reviewer_results[0][4] + " " + reviewer_results[0][5] + constants.EOD)

        login_str += "ManuscriptID | Title | Status" + constants.EOD

        for result in manuscript_results:
            login_str += f"{result[1]} | {result[12]} | {result[21]}"

        self.current_reviewer = reviewer_id
        return login_str

    def accept_reject_manuscript(self, manuscript_id, scores):
        if self.current_reviewer is None:
            return constants.REVIEWER_NOT_LOGGED_IN

        manuscript_select_query = f"SELECT * FROM {constants.MANUSCRIPT_FEEDBACK} " \
                                  f"where Manuscript_idManuscipt = {manuscript_id} " \
                                  f"and Reviewer_idReviewer = {self.current_reviewer}"
        manuscript_feedback_results = self.db.fetchAll(manuscript_select_query)

        if len(manuscript_feedback_results) == 0:
            return constants.REVIEWER_NOT_AUTHORISED

        result = self.db.update_if_exists(
            constants.MANUSCRIPT_FEEDBACK, constants.MANUSCRIPT_FEEDBACK_MAN_ID_VALUE_LIST,
            constants.MANUSCRIPT_FEEDBACK_SET_SCORES_LIST, str(manuscript_id), tuple(scores)
        )

        if result is None:
            return constants.SERVER_ERROR
        return "Scores Updated Successfully"

    def resign(self, person_id):
        delete_query = f"DELETE from {constants.REVIEWER} where Perdon_idPerson = {person_id}"
        self.db.execute_query(delete_query)

    def logout(self):
        self.current_reviewer = None


if __name__ == "__main__":
    db = DB()
    reviewer = reviewer(db)
    print(reviewer.login(1))
    db.close_connection()
