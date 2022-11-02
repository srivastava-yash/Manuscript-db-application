import constants
import random
from db import DB

class editor:

    def __init__(self, db):
        self.db = db

    def is_editor(self, person_id):
        select_query = f"SELECT * from {constants.EDITOR} where Person_idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return len(results) == 1

    def get_status(self):
        status_select_query = f"Select title, status_name from {constants.MANUSCRIPT} join {constants.MANUSCRIPT_STATUS} " \
                              f" on status = idmanuscript_status ORDER BY status, idManuscript"
        status_results = self.db.fetchAll(status_select_query)

        status = "title | status" + constants.EOD
        for status_result in status_results:
            status += status_result[0] + status_result[1] + constants.EOD

        return status


    def login(self, person_id):
        editor_select_query = f"SELECT * FROM {constants.PERSON} where idPerson = {person_id}"
        editor_results = self.db.fetchAll(editor_select_query)

        login_str = "fname | lname" + constants.EOD
        login_str += editor_results[0][1] + editor_results[0][2] + constants.EOD

        login_str += self.get_status()
        return login_str

    def register_editor(self, fname, lname):
        person_tuple = tuple([fname, lname])
        person_id = self.db.insert_if_not_exists(
            constants.PERSON, constants.PERSON_NAMES_VALUE_LIST, person_tuple
        )

        editor_tuple = tuple(str(person_id))
        editor_id = self.db.insert_if_not_exists(
            constants.EDITOR, constants.EDITOR_VALUE_LIST, editor_tuple
        )

        return person_id

    def assign_reviewer(self, manuscriptid , person_id):
        reviewer_select = f"SELECT * from {constants.REVIEWER} where Person_idPerson = {person_id}"
        reviewer_results = self.db.fetchAll(reviewer_select)
        if len(reviewer_results) == 0:
            return -1

        reviewer_id = reviewer_results[0][0]
        print(reviewer_id)
        manuscript_feedback_value_tuple = tuple([str(manuscriptid) , str(reviewer_id)])
        assign_reviewer_id = self.db.insert_if_not_exists(
            constants.MANUSCRIPT_FEEDBACK, constants.MANUSCRIPT_FEEDBACK_VALUE_LIST,
            manuscript_feedback_value_tuple
        )
        manuscript_status_tuple = tuple(["2"])
        manuscriptid_tuple = tuple([str(manuscriptid)])
        self.db.update_if_exists(
            constants.MANUSCRIPT, constants.MANUSCRIPT_ID_VALUE_LIST,
            constants.MANUSCRIPT_SET_STATUS_VALUE_LIST, manuscriptid_tuple, manuscript_status_tuple
        )
        return assign_reviewer_id

    def reject(self,manuscriptid):
        manuscript_status = "3"
        self.db.update_if_exists(
            constants.MANUSCRIPT, constants.MANUSCRIPT_ID_VALUE_LIST,
            constants.MANUSCRIPT_SET_STATUS_VALUE_LIST, tuple([str(manuscriptid)]),
            tuple([str(manuscript_status)])
        )
        return manuscriptid

    def accept(self,manuscriptid):
        manuscript_status = "4"
        total_reviews_query = f"SELECT * FROM {constants.MANUSCRIPT_FEEDBACK} WHERE Manuscript_idManuscript={manuscriptid}"
        total_reviews = self.db.fetchAll(total_reviews_query)
        if len(total_reviews) > 3:
            accept_query = f"UPDATE Manuscript SET status={manuscript_status} WHERE idManuscript={manuscriptid}"
            self.db.execute_query(accept_query)
            return "Manuscript Accepted"
        return "Not enough reviews yet"

    def schedule(self,manuscriptid,issue):
        issue.replace('"', '')
        issue_year = issue.split('-')[0]
        issue_period = issue.split('-')[1]

        issue_tuple = tuple([str(issue_year),str(issue_period), "unpublished"])
        issue_id = self.db.insert_if_not_exists(
            constants.PUBLICATION_ISSUE, constants.PUBLICATION_VALUE_LIST, issue_tuple
        )

        beg_page_num = random.randint(1,100)
        end_page_num = beg_page_num + 20

        manuscript_status = "5"
        total_pages_query = f"SELECT SUM(ending_page_number - begining_page_number) FROM Manuscript where issue = {issue_id} and status = 5"
        total_pages = len(self.db.fetchAll(total_pages_query))

        manuscript_pages = end_page_num - beg_page_num
        print(manuscript_pages)

        curr_page_sum = total_pages + manuscript_pages
        if curr_page_sum < 100:
            publish_query = f"UPDATE Manuscript SET status = {manuscript_status} and issue = {issue_id} " \
                            f"and begining_page_number = {beg_page_num} and ending_page_number = {end_page_num} " \
                            f"where idManuscript = {manuscriptid}"
            self.db.execute_query(publish_query)
            self.db.update_if_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ID_VALUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,manuscriptid,manuscript_status)
        return manuscriptid


    def publish(self,issue):
        manuscript_status = "7"
        issue_year = issue.split('-')[0]
        issue_period = issue.split('-')[1]

        issue_tuple = tuple([str(issue_year), str(issue_period), "unpublished"])
        issue_id = self.db.insert_if_not_exists(
            constants.PUBLICATION_ISSUE, constants.PUBLICATION_VALUE_LIST, issue_tuple
        )
        issue_value_tuple = tuple([str(issue_id) , "6"])
        self.db.update_if_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ISSUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,issue_value_tuple,manuscript_status)
        return issue

    def reset(self):
        filename = 'tables.sql'
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()

        # all SQL commands (split on ';')
        sqlCommands = sqlFile.split(';')
        return self.db.exceute_commands(sqlCommands)

if __name__ == "__main__":
    db = DB()
    editor_utility = editor(db)
    print(editor_utility.assign_reviewer("1","1"))
    # print(editor_utility.retrieve_manuscript_status("Select * from Manuscript ORDER BY status, idManuscript"))
    # print(editor_utility.reject("1"))
    print(editor_utility.accept("1"))
    # print(editor_utility.publish("1"))
    # print(editor_utility.schedule("1","1"))
    db.close_connection()

