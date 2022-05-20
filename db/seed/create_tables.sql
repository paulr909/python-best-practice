CREATE TABLE `employees`
(
    `emp_no`     INT            NOT NULL AUTO_INCREMENT,
    `birth_date` DATE           NOT NULL,
    `first_name` VARCHAR(14)    NOT NULL,
    `last_name`  VARCHAR(16)    NOT NULL,
    `gender`     ENUM ('M','F') NOT NULL,
    `hire_date`  DATE           NOT NULL,
    PRIMARY KEY (`emp_no`)
) ENGINE = InnoDB;

CREATE TABLE `departments`
(
    `dept_no`   CHAR(4)     NOT NULL,
    `dept_name` VARCHAR(40) NOT NULL,
    PRIMARY KEY (`dept_no`),
    UNIQUE KEY `dept_name` (`dept_name`)
) ENGINE = InnoDB;

CREATE TABLE `salaries`
(
    `emp_no`    INT  NOT NULL,
    `salary`    INT  NOT NULL,
    `from_date` DATE NOT NULL,
    `to_date`   DATE NOT NULL,
    PRIMARY KEY (`emp_no`, `from_date`),
    KEY `emp_no` (`emp_no`),
    CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`)
        REFERENCES `employees` (`emp_no`) ON DELETE CASCADE
) ENGINE = InnoDB;

CREATE TABLE `dept_emp`
(
    `emp_no`    INT     NOT NULL,
    `dept_no`   CHAR(4) NOT NULL,
    `from_date` DATE    NOT NULL,
    `to_date`   DATE    NOT NULL,
    PRIMARY KEY (`emp_no`, `dept_no`),
    KEY `emp_no` (`emp_no`),
    KEY `dept_no` (`dept_no`),
    CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`)
        REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,
    CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`)
        REFERENCES `departments` (`dept_no`) ON DELETE CASCADE
) ENGINE = InnoDB;

CREATE TABLE `dept_manager`
(
    `emp_no`    INT     NOT NULL,
    `dept_no`   CHAR(4) NOT NULL,
    `from_date` DATE    NOT NULL,
    `to_date`   DATE    NOT NULL,
    PRIMARY KEY (`emp_no`, `dept_no`),
    KEY `emp_no` (`emp_no`),
    KEY `dept_no` (`dept_no`),
    CONSTRAINT `dept_manager_ibfk_1` FOREIGN KEY (`emp_no`)
        REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,
    CONSTRAINT `dept_manager_ibfk_2` FOREIGN KEY (`dept_no`)
        REFERENCES `departments` (`dept_no`) ON DELETE CASCADE
) ENGINE = InnoDB;

CREATE TABLE `titles`
(
    `emp_no`    INT         NOT NULL,
    `title`     VARCHAR(50) NOT NULL,
    `from_date` DATE        NOT NULL,
    `to_date`   DATE DEFAULT NULL,
    PRIMARY KEY (`emp_no`, `title`, `from_date`),
    KEY `emp_no` (`emp_no`),
    CONSTRAINT `titles_ibfk_1` FOREIGN KEY (`emp_no`)
        REFERENCES `employees` (`emp_no`) ON DELETE CASCADE
) ENGINE = InnoDB;


