from unittest import result
import constants
from db import DB

class editor:

    def __init__(self, db):
        self.db = db

    def retrieve_manuscript_status(self, query):
        results  = self.db.fetchAll(query)
        print(results)
        return results

    def assign_reviewer(self, manuscriptid , reviewer_id):
        manuscript_feedback_value_tuple = tuple([manuscriptid , reviewer_id])
        assign_reviewer_id = self.db.insert_if_not_exists(constants.MANUSCRIPT_FEEDBACK, constants.MANUSCRIPT_FEEDBACK_VALUE_LIST, manuscript_feedback_value_tuple)
        manuscript_status = "2"
        self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ID_VALUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,manuscriptid,manuscript_status)
        return assign_reviewer_id

    def reject(self,manuscriptid):
        manuscript_status = "3"
        self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ID_VALUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,manuscriptid,manuscript_status)
        return manuscriptid

    def accept(self,manuscriptid):
        manuscript_status = "4"
        self.db.update_if_not_exists(constants.MANUSCRIPT,constants.MANUSCRIPT_ID_VALUE_LIST,constants.MANUSCRIPT_SET_STATUS_VALUE_LIST,manuscriptid,manuscript_status)
        return manuscriptid



if __name__ == "__main__":
    db = DB()
    editor_utility = editor(db)
    # print(editor_utility.register_author("Cardi", "B", "cardi.b@gmail.com", "Hollywood"))
    print(editor_utility.assign_reviewer("1","1"))
    print(editor_utility.retrieve_manuscript_status("Select * from Manuscript ORDER BY status, idManuscript"))
    print(editor_utility.reject("1"))
    print()
    db.close_connection()

