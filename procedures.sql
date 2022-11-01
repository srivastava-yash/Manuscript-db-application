use F006JPH_db;

DROP FUNCTION IF EXISTS ResultFunction;
DELIMITER &&
CREATE FUNCTION ResultFunction(Appropriateness INT,Clarity INT,Methodology INT,Experimental_results INT)
returns VARCHAR(10)
DETERMINISTIC
BEGIN
	DECLARE Manuscript_total_score INT;
    DECLARE FeedbackResult VARCHAR(10);
    Set Manuscript_total_score = Appropriateness + Clarity + Methodology + Experimental_results;
    IF Manuscript_total_score > 39 THEN
		SET FeedbackResult = "ACCEPTED";
	ELSE
		SET FeedbackResult = "REJECTED";
	END IF;
		Return (FeedbackResult);
END &&
DELIMITER ;

SELECT Manuscript_idManuscript, ResultFunction(AVG(Appropriateness),AVG(Clarity),AVG(Methodology),AVG(Experimental_results))
FROM Manuscript_feedback where Manuscript_idManuscript = '1';