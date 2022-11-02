# Database Group 16

    

Academic Journal Manuscript Management System 

## Main.py
Main python file contains driver function to test your application with commands coming in via `stdin` from terminal.
> Input Format
> `Function_name  Argument1  -----------  -----------  Argument N`
### Author Functionality

Author Functionality include registeration, login and submit manuscript in academic journal manuscript management System alongside checking status of all author’s manuscripts currently in the system where author is the primary author.`Author.py` comprises source code for all author functionalities. 

> REGISTER a new Author
> `register author <fname> <lname> <email> <affiliation>`
> Sample Input Command
> `register author "Joe" "Biden" "joe.biden@dartmouth.edu" "Dartmouth"`

> LOGIN
> `login <id>`
> Sample Input Command
> `login 1`

> MANUSCRIPT SUBMISSION
> `submit <title> <Affiliation> <ICode> <author2> <author3> <author4> <filename>`
> Sample Input Command
> `submit "TT" "Dartmouth" "DB" 2 3 4 file`

> AUTHOR MANUSCRIPT'S STATUS
> `status`
> Sample Input Command
> `status`


### Editor Functionality

Editor Functionality include registeration and login in academic journal manuscript management System.Alongwith,assigning,accepting,rejecting,scheduling,publishing and checking status of manuscript in database.Lastly,editor has capacity to reset entire database to it's initial state.`Editor.py` comprises source code for all editor functionalities. 
 
> REGISTER a new Editor
> `register editor <fname> <lname>`
> Sample Input Command
> `register editor "Berry" "Langer"`

> LOGIN
> `login <editor_id>`
> Sample Input Command
> `login 2`

> MANUSCRIPT STATUS
> `status`
> Sample Input Command
> `status`

> Assign Manuscript
> `assign <manuscriptid> <reviewer_id>`
> Sample Input Command
> `assign 1 1`

> Reject Manuscript
> `reject <manuscriptid>`
> Sample Input Command
> `reject 2`

> Accept Manuscript
> `accept <manuscriptid>`
> Sample Input Command
> `accept 1`

> Schedule Manuscript
> `schedule <manuscriptid> <issue>`
> Sample Input Command
> `schedule 1 1`

> Publish Manuscript
> `publish <issue>`
> Sample Input Command
> `publish 1`

> Reset
> `reset`
> Sample Input Command
> `reset`

### Reviewer Functionality

Reviewer Functionality include registration,login and option to resign.Reviewer gives 10-point ACME scale (10 is best) for **A**ppropriateness, **C**larity, **M**ethodology, and **E**xperimental results, for a total score of up to 40 points for assigned manuscript as a feedback.`Reviewer.py` comprises source code for all reviewer functionalities. 

> REGISTER a new Reviewer
> `register reviewer <fname> <lname> <ICode 1> <ICode 2> <ICode 3>`
> Sample Input Command
> `register reviewer "Paul" "Adam" 1 2 3`

> LOGIN
> `login <editor_id>`
> Sample Input Command
> `login 2`

accept_reject_manuscript function is used for assigning accept and reject alongwith ACME scores to manuscript

> ACCEPT
> `accept manuscriptid ascore cscore mscore escore`
> Sample Input Command
> `accept 1 10 10 10 10`

> REJECT
> `reject manuscriptid ascore cscore mscore escore`
> Sample Input Command
> `reject 2 3 2 1 0`

> RESIGN
> `resign`
> Sample Input Command
> `resign`



`
  