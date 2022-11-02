use F006JPH_db;


-- view LeadAuthorManuscripts
CREATE VIEW LeadAuthorManuscripts AS
select lname, idAuthor, idManuscript, status_name as status
from Person join Author on Person.idPerson = Author.Person_idPerson 
join Manuscript on Author.idAuthor = Manuscript.primary_author
join manuscript_status on Manuscript.status = manuscript_status.idmanuscript_status
order by lname, idAuthor, modified_at ASC;


-- view AnyAuthorManuscripts
CREATE VIEW AnyAuthorManuscripts AS
select fname, lname, Author_idAuthor as idAuthor, idManuscript, status_name as status 
from Person join Author_order on Person.idPerson = Author_order.Author_idAuthor
join Manuscript on Author_order.Manuscript_idManuscript = Manuscript.idManuscript
join manuscript_status on Manuscript.status = manuscript_status.idmanuscript_status
order by lname, modified_at ASC;

-- view PublishedIssues
CREATE VIEW PublishedIssues AS
select year, period, title, begining_page_number as page_numbers
from Publication_Issue join Manuscript on Publication_Issue.idPublication = Manuscript.issue
where publication_status = 'Published'
order by year, idPublication, begining_page_number;

-- view ReviewQueue
CREATE VIEW ReviewQueue AS
select primary_author, idManuscript, Reviewer_idReviewer as idReviewer
from Manuscript join Manuscript_feedback on Manuscript.idManuscript = Manuscript_feedback.Manuscript_idManuscript
where status = 2
order by modified_at;


-- view WhatsLeft
CREATE VIEW WhatsLeft AS
select idManuscript, status, modified_at from Manuscript;


-- view ReviewStatus
-- DROP function if exists get_reviewer_id;
DELIMITER &&
create function get_reviewer_id() returns INT deterministic
BEGIN
	declare reviewer_id INT;
	set @reviewer_id=1;
    return @reviewer_id;
END &&
DELIMITER ;

CREATE VIEW ReviewStatus AS
select Reviewer_idReviewer as idReviewer, Manuscript_idManuscript as idManuscript, 
Appropriateness, Clarity, Methodology, Experimental_results from Manuscript_feedback where 
Reviewer_idReviewer = get_reviewer_id();