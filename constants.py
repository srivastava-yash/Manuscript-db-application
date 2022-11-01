"""
File to store the static variables in one place
"""

## Table names
PERSON = "Person"
AUTHOR = "Author"
AFFILIATION = "Affiliation"
MANUSCRIPT_FEEDBACK = "Manuscript_feedback"
MANUSCRIPT = "Manuscript"

## command constants
REGISTER_AUTHOR = "register author"
LOGIN = "login"
SUBMIT = "submit"

PERSON_VALUE_LIST = "fname,lname,email"
AFFILIATION_VALUE_LIST = "name"
AUTHOR_VALUE_LIST = "Affiliation_idAffiliation, Person_idPerson"
MANUSCRIPT_FEEDBACK_VALUE_LIST = "manuscriptid , reviewer_id"
MANUSCRIPT_VALUE_LIST = "idManuscript"
MANUSCRIPT_SET_STATUS_VALUE_LIST = "status"

# MANUSCRIPT_SCHEDULE_LIST = "idManuscript,status,(SELECT SUM(ending_page_number - begining_page_number) FROM Manuscript where issue "
MANUSCRIPT_ISSUE_LIST = "issue,status"