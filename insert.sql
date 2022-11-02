use F006JPH_db;

INSERT INTO Person (fname, lname, email)
VALUES
("Yash" , "Srivastava","yash.srivastava.gr@dartmouth.edu"),
("Neel" , "Gandhi","neel.gandhi.gr@dartmouth.edu"),
("Ed" , "Sheeran","ed.sheeran@gmail.com"),
("Adam" , "Levine","adam.levine@gmail.com"),
("Dua" , "Lipa","dua.lipa@gmail.com"),
("Taylor" , "Swift","taylor.swift@gmail.com"); 

select * from Person;


INSERT INTO Affiliation (name)
VALUES
("Dartmouth_College"),
("Hollywood");

select * from Affiliation;

INSERT INTO Author (Affiliation_idAffiliation, Person_idPerson)
VALUES
(1 , 1),
(1 , 2);

select * from Author;


INSERT INTO Editor (Person_idPerson)
VALUES
(3);

select * from Editor;


INSERT INTO Reviewer (Affiliation_idAffiliation, Person_idPerson)
VALUES
(1,1),
(1,2),
(2,3);
select * from Reviewer;


INSERT INTO manuscript_status(status_name)
VALUES
("submitted"),
("under review"),
("rejected"),
("accepted"),
("in typesetting"),
("scheduled for publication"),
("published");

select * from manuscript_status;


INSERT INTO Publication_Issue(year, period, publication_status)
VALUES
(2021, 1, "unpublished"),
(2021, 2, "unpublished");

select * from Publication_Issue;

INSERT INTO Icode(description)
VALUES
("ml"),
("robotics"),
("computer systems"),
("hci"),
("db");

INSERT INTO Manuscript(status, Icode_idIcode, title, primary_author, Editor_idEditor)
VALUES
(1, 1, "deep learning", 1, 1);


INSERT INTO Manuscript_feedback(Manuscript_idManuscript, Reviewer_idReviewer)
VALUES
(1,1);

select * from Icode;

INSERT INTO Reviewer_interest(Reviewer_idReviewer, Icode_idIcode)
VALUES
(1, 1),
(1, 2),
(1, 3);

-- SET SQL_SAFE_UPDATES = 0;
-- update Reviewer_interest set Icode_idIcode = 1 where idReviewer_interest = 1;
-- SET SQL_SAFE_UPDATES = 1;

select * from Reviewer_interest;


-- INSERT INTO Manuscript(status, Icode_idIcode, title, primary_author, issue, Editor_idEditor)
-- VALUES
-- (1, 9, "deep learning 2", 1, 1, 1);

select * from Manuscript;

INSERT INTO Author_order(Manuscript_idManuscript, Author_idAuthor, Author_order.order)
VALUES
(1,1,1),
(1,2,2);

