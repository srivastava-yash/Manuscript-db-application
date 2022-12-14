"""
File to store the static variables in one place
"""

## Table names
PERSON = "Person"
AUTHOR = "Author"
EDITOR = "Editor"
AFFILIATION = "Affiliation"
MANUSCRIPT_FEEDBACK = "Manuscript_feedback"
MANUSCRIPT = "Manuscript"
ICODE = "Icode"
REVIEWER = "Reviewer"
REVIEWER_INTEREST = "Reviewer_interest"
MANUSCRIPT_STATUS = "manuscript_status"
AUTHOR_ORDER = "Author_order"
ICODE = "Icode"
PUBLICATION_ISSUE = "Publication_Issue"

## command constants
REGISTER_AUTHOR = "register author"
REGISTER_REVIEWER = "register reviewer"
REGISTER_EDITOR = "register editor"
LOGIN = "login"
SUBMIT = "submit"
ACCEPT = "accept"
REJECT = "reject"
EXIT = "exit"
QUIT = "quit"
STATUS = "status"
ASSIGN = "assign"
SCHEDULE = "schedule"
PUBLISH = "publish"
RESET = "reset"
RESIGN = "resign"

## Value lists
PERSON_VALUE_LIST = "fname,lname,email"
PERSON_NAMES_VALUE_LIST = "fname,lname"
AFFILIATION_VALUE_LIST = "name"
AUTHOR_VALUE_LIST = "Affiliation_idAffiliation,Person_idPerson"
AUTHOR_PERSON_VALUE_LIST = "Person_idPerson"
MANUSCRIPT_FEEDBACK_VALUE_LIST = "Manuscript_idManuscript,Reviewer_idReviewer"
MANUSCRIPT_FEEDBACK_MAN_ID_VALUE_LIST = "Manuscript_idManuscript,Reviewer_idReviewer"
MANUSCRIPT_FEEDBACK_SET_SCORES_LIST = "Appropriateness,Clarity,Methodology,Experimental_results"
MANUSCRIPT_ID_VALUE_LIST = "idManuscript"
MANUSCRIPT_SET_STATUS_VALUE_LIST = "status"
MANUSCRIPT_ISSUE_LIST = "issue,status"
ICODE_VALUE_LIST = "description"
MANUSCRIPT_VALUE_LIST = "status,Icode_idIcode,title,primary_author"
REVIEWER_VALUE_LIST = "Affiliation_idAffiliation,Person_idPerson"
REVIEWER_INTEREST_VALUE_LIST = "Reviewer_idReviewer,Icode_idIcode"
AUTHOR_ORDER_VALUE_LIST = "Manuscript_idManuscript,Author_idAuthor,order"
EDITOR_VALUE_LIST = "Person_idPerson"
PUBLICATION_VALUE_LIST = "year,period,publication_status"

## Error Messages
AUTHOR_NOT_LOGGED_IN = "Author not logged in / Please login"
ICODE_DNE = "Invalid Command | Icode not found at the right position"
REVIEWER_DNE = "Reviewer not found"
REVIEWER_NOT_LOGGED_IN = "Reviewer not logged in / Please login"
REVIEWER_NOT_AUTHORISED = "Not Authorised to review this manuscript"
SERVER_ERROR = "Some error occurred"
INVALID_COMMAND = "Invalid command / invalid number of arguments"

EOD = "\n"