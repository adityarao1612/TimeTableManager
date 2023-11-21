drop database timetablemanager;
create database IF NOT EXISTS timetablemanager;
use timetablemanager;


-- Admin table
CREATE TABLE IF NOT EXISTS admin (
        username varchar(50) PRIMARY KEY,
        password varchar(50),
        role varchar(20));


-- Student table
CREATE TABLE IF NOT EXISTS Student (
    studentid varchar(13) PRIMARY KEY,
    name VARCHAR(255),
    semester INT,
    section char,
    batchid varchar(2)
);

-- Teacher table
CREATE TABLE IF NOT EXISTS Teacher (
    teacherid varchar(13) PRIMARY KEY,
    name VARCHAR(255),
    dept VARCHAR(50),
    email VARCHAR(100)
);

-- Subject table
CREATE TABLE IF NOT EXISTS Subject (
    subjectcode VARchar(25) PRIMARY KEY,
    subjectname VARCHAR(255),
    semester int
);

-- Teaches table
CREATE TABLE IF NOT EXISTS Teaches (
    teacherid varchar(13),
    subjectcode varchar(25),
    batchid varchar(2)
);

-- Classroom table
CREATE TABLE IF NOT EXISTS Classroom (
    room_id VARCHAR(10) PRIMARY KEY,
    capacity INT
);

-- Timetable table

-- CREATE TABLE Timetable (
--     timetable_id INT PRIMARY KEY,
--     batch_id INT
-- );
CREATE TABLE IF NOT EXISTS Batch (
    batchid VARchar(2) PRIMARY KEY
);

-- Timeslot table
CREATE TABLE IF NOT EXISTS Timeslot (
    slot_id INT,
    room_id VARCHAR(10),
    batch_id VARCHAR(2),
    subjectcode VARCHAR(25),
    day VARCHAR(10),
    starttime TIME,
    endtime TIME,
    PRIMARY KEY (slot_id, room_id)
);

-- Add foreign key constraint to Teaches table
ALTER TABLE Teaches
ADD CONSTRAINT fk_teaches_teacher FOREIGN KEY (teacherid) REFERENCES Teacher(teacherid),
ADD CONSTRAINT fk_teaches_subject FOREIGN KEY (subjectcode) REFERENCES Subject(subjectcode),
ADD CONSTRAINT fk_teaches_batch FOREIGN KEY (batchid) REFERENCES batch(batchid);

-- Add foreign key constraint to Timeslot table
ALTER TABLE Timeslot
ADD CONSTRAINT fk_timeslot_room FOREIGN KEY (room_id) REFERENCES Classroom(room_id),
ADD CONSTRAINT fk_timeslot_batch FOREIGN KEY (batch_id) REFERENCES batch(batchid),
ADD CONSTRAINT fk_timeslot_subject FOREIGN KEY (subjectcode) REFERENCES Subject(subjectcode);

-- Add foreign key constraint to Batch table
-- ALTER TABLE Batch
-- ADD CONSTRAINT fk_batch_timetable FOREIGN KEY (timetable_id) REFERENCES Timetable(timetable_id);

-- Add foreign key constraint to Student table
ALTER TABLE Student
ADD CONSTRAINT fk_student_batch FOREIGN KEY (batchid) REFERENCES Batch(batchid);

-- Add foreign key constraint to Timetable table
-- ALTER TABLE Timetable
-- ADD CONSTRAINT fk_timetable_batch FOREIGN KEY (batch_id) REFERENCES Batch(batch_id);

CREATE TABLE IF NOT EXISTS UpdatedTables (
    slot_id INT,
    room_id VARCHAR(10),
    batch_id varchar(2),
    subjectcode VARchar(25),
    day VARCHAR(10),
    starttime TIME,
    endtime TIME,
	PRIMARY KEY (slot_id, room_id)

);


CREATE TABLE LeaveTable (
    leave_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_id VARCHAR(255) NOT NULL,
    leave_day VARCHAR(255) NOT NULL,
    CONSTRAINT unique_leave UNIQUE (teacher_id, leave_day)
);

DELIMITER //
CREATE TRIGGER after_leave_insert
AFTER INSERT ON LeaveTable
FOR EACH ROW
BEGIN
    DELETE FROM UpdatedTables
    WHERE (batch_id,subjectcode) IN (
        SELECT batchid,subjectcode FROM Teaches WHERE teacherid = NEW.teacher_id   
          ) AND day = NEW.leave_day;
END;
//
DELIMITER ;


DELIMITER //
CREATE TRIGGER after_leave_delete
AFTER DELETE ON LeaveTable
FOR EACH ROW
BEGIN
    INSERT INTO UpdatedTables (slot_id, room_id, batch_id, subjectcode, day, starttime, endtime)
    SELECT ts.slot_id, ts.room_id, ts.batch_id, ts.subjectcode, ts.day, ts.starttime, ts.endtime
    FROM Timeslot ts
    WHERE (ts.batch_id, ts.subjectcode) IN (
        SELECT batchid, subjectcode FROM Teaches WHERE teacherid = OLD.teacher_id
    ) AND day = OLD.leave_day;
END;
//
DELIMITER ;
