"""
File to store the static variables in one place
"""

## Table names
PERSON = "Person"
AUTHOR = "Author"
AFFILIATION = "Affiliation"
ICODE = "Icode"
MANUSCRIPT = "Manuscript"


## command constants
REGISTER_AUTHOR = "register author"
LOGIN = "login"
SUBMIT = "submit"

## Value lists
PERSON_VALUE_LIST = "fname,lname,email"
AFFILIATION_VALUE_LIST = "name"
AUTHOR_VALUE_LIST = "Affiliation_idAffiliation, Person_idPerson"
ICODE_VALUE_LIST = "description"
MANUSCRIPT_VALUE_LIST = "status,Icode_idIcode,title,primary_author"


## Error Messages
AUTHOR_DNE = "Author not logged in / Please login"
ICODE_DNE = "Invalid Command | Icode not found at the right position"

EOD = "\n"