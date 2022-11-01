use F006JPH_db;

-- Trigger 1
DELIMITER &&
CREATE TRIGGER validate_manuscript_icode BEFORE INSERT
ON Manuscript for each row
BEGIN
DECLARE msg varchar(65);
if not exists(select count(*) from Reviewer_interest where Icode_idIcode = new.Icode_idIcode group by Icode_idIcode)
THEN
set @msg = "Manuscript can not be submitted as no reviewers for this Interest Code";
signal sqlstate '45000' set message_text = @msg;
END IF;
END &&
DELIMITER ;

-- Trigger 1 Test
INSERT INTO Manuscript(status, Icode_idIcode, title, primary_author)
VALUES
(1, 1, "hci", 1);


-- Trigger 2 BEFORE UPDATE trigger for when the reviewer changes their interest
DROP PROCEDURE status_updation;
DELIMITER &&
CREATE PROCEDURE status_updation(icode_id INT, reviewer_id INT)
BEGIN
DECLARE icode_count INT;
set @icode_count = (select count(*) from Reviewer_interest where Icode_idIcode = icode_id);
INSERT INTO logs(count)
VALUES (@icode_count);
if (@icode_count < 2) THEN
update Manuscript set status = 3 where idManuscript in ( select Manuscript_idManuscript from Manuscript_feedback where Reviewer_idReviewer = reviewer_id );
ELSE
update Manuscript set status = 1 where idManuscript in ( select Manuscript_idManuscript from Manuscript_feedback where Reviewer_idReviewer = reviewer_id );
END IF;
END &&
DELIMITER ;


DROP TRIGGER IF EXISTS manuscript_status_update_reviewer_interest;
DELIMITER &&
CREATE TRIGGER manuscript_status_update_reviewer_interest BEFORE UPDATE
ON Reviewer_interest for each row
BEGIN
CALL status_updation(old.Icode_idIcode, old.Reviewer_idReviewer);
END &&
DELIMITER ;

-- Trigger 2 Test
update Reviewer_interest set Icode_idIcode = 4 where idReviewer_interest = 1;


-- Trigger 3
DELIMITER &&
CREATE TRIGGER update_manuscript_status BEFORE UPDATE
ON Manuscript for each row
BEGIN
IF (new.status = 4) THEN
SET new.status = 5;
END IF;
END &&
DELIMITER ;

-- Trigger 3 Test
update Manuscript set status = 4 where idManuscript = 1;
