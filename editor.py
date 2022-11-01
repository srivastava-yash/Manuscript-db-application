from unittest import result
import constants
from db import DB

class editor:

    def __init__(self, db):
        self.db = db

    def is_editor(self, person_id):
        select_query = f"SELECT * from {constants.EDITOR} where Person.idPerson = {person_id}"
        results = self.db.fetchAll(select_query)

        return len(results) == 1

    def retrieve_manuscript_status(self, query):
        results  = self.db.fetchAll(query)
        print(results)
        return results

    def assign_reviewer(self, manuscriptid , reviewer_id):
        manuscript_feedback_value_tuple = tuple([manuscriptid , reviewer_id])
        assign_reviewer_id = self.db.insert_if_not_exists(constants.MANUSCRIPT_FEEDBACK, constants.MANUSCRIPT_FEEDBACK_VALUE_LIST, manuscript_feedback_value_tuple)
        manuscript_status = "2"
        self.db.update_if_exists(constants.MANUSCRIPT, constants.MANUSCRIPT_ID_VALUE_LIST, constants.MANUSCRIPT_SET_STATUS_VALUE_LIST, manuscriptid, manuscript_status)
        return assign_reviewer_id

    def reject(self,manuscriptid):
        manuscript_status = "3"
        self.db.update_if_exists(constants.MANUSCRIPT, constants.MANUSCRIPT_ID_VALUE_LIST, constants.MANUSCRIPT_SET_STATUS_VALUE_LIST, manuscriptid, manuscript_status)
        return manuscriptid

    def accept(self,manuscriptid):
        manuscript_status = "4"
        total_reviews_query = f"SELECT * FROM Manuscript_feedback WHERE idManuscript={manuscriptid}"
        total_reviews = self.db.intermediate_query(total_reviews_query)
        if len(total_reviews) > 3:
            accept_query = f"UPDATE Manuscript SET status={manuscript_status} WHERE idManuscript={manuscriptid}"
            self.db.query(accept_query)
        # self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_VALUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,manuscriptid,manuscript_status)
        return manuscriptid

    def schedule(self,manuscriptid,issue):
        # manuscript_status = "5"
        # schedule_value_tuple = tuple([str(manuscriptid) , str(issue) , str(issue) + ") <" + "100"])
        # self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_SCHEDULE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,schedule_value_tuple,manuscript_status)
        manuscript_status = "5"
        total_pages_query = f"(SELECT SUM(ending_page_number - begining_page_number) FROM Manuscript where issue = {issue} and status = '5') < 100 "
        total_pages = self.db.intermediate_query(total_pages_query)
        curr_page_sum_query  = f"(SELECT SUM(ending_page_number - begining_page_number) FROM Manuscript where issue = {issue} and idManuscript = {manuscriptid}) < 100"
        curr_page_sum = self.db.intermediate_query(curr_page_sum_query)
        total_pages += curr_page_sum
        if total_pages < 100:
            publish_query = f"UPDATE Manuscript SET status = {manuscript_status} where idManuscript = {manuscriptid} AND issue = {issue}"
        self.db.query(publish_query)
        self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ID_VALUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,manuscriptid,manuscript_status)
        return manuscriptid


    def publish(self,issue):
        manuscript_status = "7"
        issue_value_tuple = tuple([issue , "6"])
        self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ISSUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,issue_value_tuple,manuscript_status)
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
    # print(editor_utility.assign_reviewer("1","1"))
    # print(editor_utility.retrieve_manuscript_status("Select * from Manuscript ORDER BY status, idManuscript"))
    # print(editor_utility.reject("1"))
    print(editor_utility.accept("1"))
    # print(editor_utility.publish("1"))
    # print(editor_utility.schedule("1","1"))
    db.close_connection()

