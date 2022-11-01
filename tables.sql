SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

use F006JPH_db;

-- -----------------------------------------------------
-- Table `F006JPH_db`.`Affiliation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Affiliation` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Affiliation` (
  `idAffiliation` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`idAffiliation`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Person`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Person` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Person` (
  `idPerson` INT NOT NULL AUTO_INCREMENT,
  `fname` VARCHAR(45) NULL,
  `lname` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`idPerson`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Author`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Author` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Author` (
  `idAuthor` INT NOT NULL AUTO_INCREMENT,
  `Affiliation_idAffiliation` INT NOT NULL,
  `Person_idPerson` INT NOT NULL,
  PRIMARY KEY (`idAuthor`, `Affiliation_idAffiliation`, `Person_idPerson`),
  INDEX `fk_Author_Affiliation1_idx` (`Affiliation_idAffiliation` ASC) VISIBLE,
  INDEX `fk_Author_Person1_idx` (`Person_idPerson` ASC) VISIBLE,
  CONSTRAINT `fk_Author_Affiliation1`
    FOREIGN KEY (`Affiliation_idAffiliation`)
    REFERENCES `F006JPH_db`.`Affiliation` (`idAffiliation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Author_Person1`
    FOREIGN KEY (`Person_idPerson`)
    REFERENCES `F006JPH_db`.`Person` (`idPerson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`manuscript_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`manuscript_status` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`manuscript_status` (
  `idmanuscript_status` INT NOT NULL AUTO_INCREMENT,
  `status` VARCHAR(45) NULL,
  PRIMARY KEY (`idmanuscript_status`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Icode`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Icode` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Icode` (
  `idIcode` INT NOT NULL AUTO_INCREMENT,
  `description` VARCHAR(45) NULL,
  PRIMARY KEY (`idIcode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Publication_Issue`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Publication_Issue` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Publication_Issue` (
  `idPublication` INT NOT NULL AUTO_INCREMENT,
  `year` INT NULL,
  `period` INT NULL,
  `publication_status` VARCHAR(25) NULL,
  PRIMARY KEY (`idPublication`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Editor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Editor` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Editor` (
  `idEditor` INT NOT NULL AUTO_INCREMENT,
  `Person_idPerson` INT NOT NULL,
  PRIMARY KEY (`idEditor`, `Person_idPerson`),
  INDEX `fk_Editor_Person1_idx` (`Person_idPerson` ASC) VISIBLE,
  CONSTRAINT `fk_Editor_Person1`
    FOREIGN KEY (`Person_idPerson`)
    REFERENCES `F006JPH_db`.`Person` (`idPerson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `F006JPH_db`.`Manuscript`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Manuscript` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Manuscript` (
  `idManuscript` INT NOT NULL AUTO_INCREMENT,
  `status` INT NOT NULL,
  `Icode_idIcode` INT NOT NULL,
  `date_received` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `title` VARCHAR(45) NULL,
  `primary_author` INT NOT NULL,
  `issue` INT NOT NULL,
  `Editor_idEditor` INT NOT NULL,
  `begining_page_number` INT NULL,
  `ending_page_number` INT NULL,
  `issue_order` INT NULL,
  `modified_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`idManuscript`),
  INDEX `fk_Manuscript_manuscript_status1_idx` (`status` ASC) VISIBLE,
  INDEX `fk_Manuscript_Icode1_idx` (`Icode_idIcode` ASC) VISIBLE,
  INDEX `fk_Manuscript_Author1_idx` (`primary_author` ASC) VISIBLE,
  INDEX `fk_Manuscript_Publication1_idx` (`issue` ASC) VISIBLE,
  INDEX `fk_Manuscript_Editor1_idx` (`Editor_idEditor` ASC) VISIBLE,
  CONSTRAINT `fk_Manuscript_manuscript_status1`
    FOREIGN KEY (`status`)
    REFERENCES `F006JPH_db`.`manuscript_status` (`idmanuscript_status`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manuscript_Icode1`
    FOREIGN KEY (`Icode_idIcode`)
    REFERENCES `F006JPH_db`.`Icode` (`idIcode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manuscript_Author1`
    FOREIGN KEY (`primary_author`)
    REFERENCES `F006JPH_db`.`Author` (`idAuthor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manuscript_Publication1`
    FOREIGN KEY (`issue`)
    REFERENCES `F006JPH_db`.`Publication_Issue` (`idPublication`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manuscript_Editor1`
    FOREIGN KEY (`Editor_idEditor`)
    REFERENCES `F006JPH_db`.`Editor` (`idEditor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`logs` (
`idlogs` INT NOT NULL AUTO_INCREMENT,
`count` INT,
PRIMARY KEY (`idlogs`)
)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `F006JPH_db`.`Author_order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Author_order` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Author_order` (
  `idAuthor_order` INT NOT NULL AUTO_INCREMENT,
  `Manuscript_idManuscript` INT NOT NULL,
  `Author_idAuthor` INT NOT NULL,
  `order` INT NULL,
  PRIMARY KEY (`idAuthor_order`, `Manuscript_idManuscript`, `Author_idAuthor`),
  INDEX `fk_Author_order_Manuscript1_idx` (`Manuscript_idManuscript` ASC) VISIBLE,
  INDEX `fk_Author_order_Author1_idx` (`Author_idAuthor` ASC) VISIBLE,
  CONSTRAINT `fk_Author_order_Manuscript1`
    FOREIGN KEY (`Manuscript_idManuscript`)
    REFERENCES `F006JPH_db`.`Manuscript` (`idManuscript`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Author_order_Author1`
    FOREIGN KEY (`Author_idAuthor`)
    REFERENCES `F006JPH_db`.`Author` (`idAuthor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Reviewer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Reviewer` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Reviewer` (
  `idReviewer` INT NOT NULL AUTO_INCREMENT,
  `Affiliation_idAffiliation` INT NOT NULL,
  `Person_idPerson` INT NOT NULL,
  PRIMARY KEY (`idReviewer`, `Affiliation_idAffiliation`, `Person_idPerson`),
  INDEX `fk_Reviewer_Affiliation1_idx` (`Affiliation_idAffiliation` ASC) VISIBLE,
  INDEX `fk_Reviewer_Person1_idx` (`Person_idPerson` ASC) VISIBLE,
  CONSTRAINT `fk_Reviewer_Affiliation1`
    FOREIGN KEY (`Affiliation_idAffiliation`)
    REFERENCES `F006JPH_db`.`Affiliation` (`idAffiliation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reviewer_Person1`
    FOREIGN KEY (`Person_idPerson`)
    REFERENCES `F006JPH_db`.`Person` (`idPerson`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Reviewer_interest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Reviewer_interest` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Reviewer_interest` (
  `idReviewer_interest` INT NOT NULL AUTO_INCREMENT,
  `Reviewer_idReviewer` INT NOT NULL,
  `Icode_idIcode` INT NOT NULL,
  PRIMARY KEY (`idReviewer_interest`),
  INDEX `fk_Reviewer_interest_Reviewer1_idx` (`Reviewer_idReviewer` ASC) VISIBLE,
  INDEX `fk_Reviewer_interest_Icode1_idx` (`Icode_idIcode` ASC) VISIBLE,
  CONSTRAINT `fk_Reviewer_interest_Reviewer1`
    FOREIGN KEY (`Reviewer_idReviewer`)
    REFERENCES `F006JPH_db`.`Reviewer` (`idReviewer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reviewer_interest_Icode1`
    FOREIGN KEY (`Icode_idIcode`)
    REFERENCES `F006JPH_db`.`Icode` (`idIcode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `F006JPH_db`.`Manuscript_feedback`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `F006JPH_db`.`Manuscript_feedback` ;

CREATE TABLE IF NOT EXISTS `F006JPH_db`.`Manuscript_feedback` (
  `idManuscript_feedback` INT NOT NULL AUTO_INCREMENT,
  `Manuscript_idManuscript` INT NOT NULL,
  `Reviewer_idReviewer` INT NOT NULL,
  `Appropriateness` INT NULL,
  `Clarity` INT NULL,
  `Methodology` INT NULL,
  `Experimental_results` INT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`idManuscript_feedback`),
  INDEX `fk_Manuscript_feedback_Manuscript1_idx` (`Manuscript_idManuscript` ASC) VISIBLE,
  INDEX `fk_Manuscript_feedback_Reviewer1_idx` (`Reviewer_idReviewer` ASC) VISIBLE,
  CONSTRAINT `fk_Manuscript_feedback_Manuscript1`
    FOREIGN KEY (`Manuscript_idManuscript`)
    REFERENCES `F006JPH_db`.`Manuscript` (`idManuscript`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Manuscript_feedback_Reviewer1`
    FOREIGN KEY (`Reviewer_idReviewer`)
    REFERENCES `F006JPH_db`.`Reviewer` (`idReviewer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
