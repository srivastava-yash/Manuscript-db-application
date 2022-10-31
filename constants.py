"""
File to store the static variables in one place
"""

## Table names
PERSON = "Person"
AUTHOR = "Author"
AFFILIATION = "Affiliation"
MANUSCRIPT_FEEDBACK = "Manuscript_feedback"
MANUSCRIPT = "Manuscript"
ICODE = "Icode"

## command constants
REGISTER_AUTHOR = "register author"
LOGIN = "login"
SUBMIT = "submit"

## Value lists
PERSON_VALUE_LIST = "fname,lname,email"
AFFILIATION_VALUE_LIST = "name"
AUTHOR_VALUE_LIST = "Affiliation_idAffiliation, Person_idPerson"
MANUSCRIPT_FEEDBACK_VALUE_LIST = "manuscriptid , reviewer_id"
MANUSCRIPT_ID_VALUE_LIST = "idManuscript"
MANUSCRIPT_SET_STATUS_VALUE_LIST = "status"
ICODE_VALUE_LIST = "description"
MANUSCRIPT_VALUE_LIST = "status,Icode_idIcode,title,primary_author"

## Error Messages
AUTHOR_DNE = "Author not logged in / Please login"
ICODE_DNE = "Invalid Command | Icode not found at the right position"

EOD = "\n"