use timetablemanager;

INSERT INTO admin (username, password, role) VALUES
('admin123', '123', 'admin'),
('admin1', 'admin1', 'admin'),
('admin2', 'admin2', 'admin'),
('Teacher1', 'Teacher1', 'teacher'),
('Teacher2', 'Teacher3', 'teacher'),
('HOD1', 'HOD1', 'HOD');


INSERT INTO Subject (subjectcode, subjectname, semester) VALUES
('UE21CS341A', 'Software Engineering',5),
('UE21CS351A', 'DBMS',5),
('UE21CS352A', 'Machine Intelligence',5),
('UE21CS342A', 'Data Analytics',5),
('UE21CS343A', 'Graph theory',5);



INSERT INTO TEACHER values
('INSTRUCTOR1', 'INSTRUCTOR1', 'CS', 'INSTRUCTOR1@gmail.com'),
('INSTRUCTOR2', 'INSTRUCTOR2', 'CS', 'INSTRUCTOR2@gmail.com'),
('INSTRUCTOR3', 'INSTRUCTOR3', 'CS', 'INSTRUCTOR3@gmail.com'),
('INSTRUCTOR4', 'INSTRUCTOR4', 'CS', 'INSTRUCTOR4@gmail.com'),
('INSTRUCTOR5', 'INSTRUCTOR5', 'CS', 'INSTRUCTOR5@gmail.com'),
('INSTRUCTOR6', 'INSTRUCTOR6', 'CS', 'INSTRUCTOR6@gmail.com'),
('INSTRUCTOR7', 'INSTRUCTOR7', 'CS', 'INSTRUCTOR7@gmail.com');



INSERT INTO Batch values
("5A"),
("5B"),
("5C"),
("5D"),
("5E"),
("5F");


INSERT INTO Teaches (teacherid, subjectcode, batchid) VALUES
('INSTRUCTOR1', 'UE21CS351A', '5A'),
('INSTRUCTOR1', 'UE21CS351A', '5B'),
('INSTRUCTOR2', 'UE21CS351A', '5C'),
('INSTRUCTOR3', 'UE21CS351A', '5D'),
('INSTRUCTOR4', 'UE21CS351A', '5E');


INSERT INTO Teaches (teacherid, subjectcode, batchid) VALUES
('INSTRUCTOR5', 'UE21CS342A', '5A'),
('INSTRUCTOR4', 'UE21CS342A', '5B'),
('INSTRUCTOR3', 'UE21CS342A', '5C'),
('INSTRUCTOR6', 'UE21CS342A', '5D'),
('INSTRUCTOR2', 'UE21CS342A', '5E');

INSERT INTO Teaches (teacherid, subjectcode, batchid) VALUES
('INSTRUCTOR2', 'UE21CS343A', '5A'),
('INSTRUCTOR1', 'UE21CS343A', '5B'),
('INSTRUCTOR5', 'UE21CS343A', '5C'),
('INSTRUCTOR3', 'UE21CS343A', '5D'),
('INSTRUCTOR2', 'UE21CS343A', '5E');


INSERT INTO Teaches (teacherid, subjectcode, batchid) VALUES
('INSTRUCTOR4', 'UE21CS352A', '5A'),
('INSTRUCTOR3', 'UE21CS352A', '5B'),
('INSTRUCTOR2', 'UE21CS352A', '5C'),
('INSTRUCTOR6', 'UE21CS352A', '5D'),
('INSTRUCTOR1', 'UE21CS352A', '5E');


INSERT INTO Teaches (teacherid, subjectcode, batchid) VALUES
('INSTRUCTOR2', 'UE21CS341A', '5A'),
('INSTRUCTOR1', 'UE21CS341A', '5B'),
('INSTRUCTOR3', 'UE21CS341A', '5C'),
('INSTRUCTOR5', 'UE21CS341A', '5D'),
('INSTRUCTOR4', 'UE21CS341A', '5E');


INSERT INTO Classroom (room_id, capacity) VALUES
('G01', 45),
('G02', 45),
('G03', 45),
('G04', 45),
('G05', 45);


INSERT INTO Timeslot (slot_id, room_id, batch_id, subjectcode, day, starttime, endtime) VALUES
(1, 'G01', '5A', 'UE21CS341A', 'Monday', '08:00:00', '09:30:00'),
(2, 'G01', '5A', 'UE21CS343A', 'Monday', '10:00:00', '11:30:00'),
(3, 'G01', '5A', 'UE21CS351A', 'Monday', '12:30:00', '14:00:00'),
(4, 'G01', '5A', 'UE21CS352A', 'Monday', '14:30:00', '16:00:00'),
(5, 'G01', '5A', 'UE21CS343A', 'Tuesday', '08:00:00', '09:30:00'),
(6, 'G01', '5A', 'UE21CS351A', 'Tuesday', '10:00:00', '11:30:00'),
(7, 'G01', '5A', 'UE21CS341A', 'Tuesday', '12:30:00', '14:00:00'),
(8, 'G01', '5A', 'UE21CS352A', 'Tuesday', '14:30:00', '16:00:00'),
(9, 'G01', '5A', 'UE21CS343A', 'Wednesday', '08:00:00', '09:30:00'),
(10, 'G01', '5A', 'UE21CS351A', 'Wednesday', '10:00:00', '11:30:00');

INSERT INTO Timeslot (slot_id, room_id, batch_id, subjectcode, day, starttime, endtime) VALUES
(11, 'G01', '5A', 'UE21CS352A', 'Wednesday', '12:30:00', '14:00:00'),
(12, 'G01', '5A', 'UE21CS342A', 'Wednesday', '14:30:00', '16:00:00'),
(13, 'G01', '5A', 'UE21CS341A', 'Thursday', '08:00:00', '09:30:00'),
(14, 'G01', '5A', 'UE21CS351A', 'Thursday', '10:00:00', '11:30:00'),
(15, 'G01', '5A', 'UE21CS342A', 'Thursday', '12:30:00', '14:00:00'),
(16, 'G01', '5A', 'UE21CS352A', 'Thursday', '14:30:00', '16:00:00'),
(17, 'G01', '5A', 'UE21CS351A', 'Friday', '08:00:00', '09:30:00'),
(18, 'G01', '5A', 'UE21CS341A', 'Friday', '10:00:00', '11:30:00'),
(19, 'G01', '5A', 'UE21CS352A', 'Friday', '12:30:00', '14:00:00'),
(20, 'G01', '5A', 'UE21CS342A', 'Friday', '14:30:00', '16:00:00');








INSERT INTO Student values
("PES1UG21CS001","AMARA SAI PRASAD",5,'A',"5A"),
("PES1UG21CS002","A SAKTHE BALAN",5,'A',"5A"),
("PES1UG21CS003","A VISHAL SETTY",5,'A',"5A"),
("PES1UG21CS004","A.NITHIN",5,'A',"5A"),
("PES1UG21CS005","AADITHYA H RAO",5,'A',"5A"),
("PES1UG21CS006","AADITYA NARAYAN",5,'A',"5A"),
("PES1UG21CS007","AAKASH V",5,'A',"5A"),
("PES1UG21CS008","ANANTH KASHYAP",5,'A',"5A"),
("PES1UG21CS009","AARYAN HEMANT BADYAL",5,'A',"5A"),
("PES1UG21CS010","AARYAN SHETTY",5,'A',"5A"),
("PES1UG21CS011","AASHISH SHARMA ",5,'A',"5A"),
("PES1UG21CS012","AAVISH GILBERT J",5,'A',"5A"),
("PES1UG21CS013","AAYUSH MISHRA",5,'A',"5A"),
("PES1UG21CS014","AAYUSH NAGAR",5,'A',"5A"),
("PES1UG21CS015","AAYUSH SENAPATI",5,'A',"5A"),
("PES1UG21CS016","ABHAY NARASINHA JOSHI",5,'A',"5A"),
("PES1UG21CS017","ABHAY RANGA HAMPAPUR",5,'A',"5A"),
("PES1UG21CS018","ABHIGNYA KOTHA",5,'A',"5A"),
("PES1UG21CS019","ABHIJEET M BALOJI",5,'A',"5A"),
("PES1UG21CS020","ABHINAV R BHARADWAJ",5,'A',"5A"),
("PES1UG21CS021","ABHINAVA RAM N",5,'A',"5A"),
("PES1UG21CS022","ABHIRAJ",5,'A',"5A"),
("PES1UG21CS023","ABHIRAM PRASANNA",5,'A',"5A"),
("PES1UG21CS024","ABHIRAM.H.A",5,'A',"5A"),
("PES1UG21CS025","ABHISHEK",5,'A',"5A"),
("PES1UG21CS026","ABHISHEK SHRINIVAS VADAVADAGI",5,'A',"5A"),
("PES1UG21CS027","ACHALA NAYAK",5,'A',"5A"),
("PES1UG21CS028","ACHINTYA KRISHNA",5,'A',"5A"),
("PES1UG21CS029","ADHESH DHEERAJ ",5,'A',"5A"),
("PES1UG21CS030","ADITHI S MURTHY",5,'A',"5A"),
("PES1UG21CS031","ADITHYA GANESH",5,'A',"5A"),
("PES1UG21CS032","ADITHYA MAHESH",5,'A',"5A"),
("PES1UG21CS033","ADITHYA S KOLAVI",5,'A',"5A"),
("PES1UG21CS034","ADITHYA SHARMA C A",5,'A',"5A"),
("PES1UG21CS035","ADITHYA TG",5,'A',"5A"),
("PES1UG21CS036","ADITHYA.B",5,'A',"5A"),
("PES1UG21CS037","ADITI GOYAL",5,'A',"5A"),
("PES1UG21CS038","ADITI MALLYA",5,'A',"5A"),
("PES1UG21CS039","ADITI PRABHU A",5,'A',"5A"),
("PES1UG21CS040","ADITYA ANANT MANGALGI",5,'A',"5A"),
("PES1UG21CS041","ADITYA ARAKERE",5,'B',"5B"),
("PES1UG21CS042","ADITYA CHAUBEY",5,'B',"5B"),
("PES1UG21CS043","ADITYA D VENKATESH PRASANNA",5,'B',"5B"),
("PES1UG21CS044","ADITYA KAMSHETTY ",5,'B',"5B"),
("PES1UG21CS045","ADITYA RAO",5,'B',"5B"),
("PES1UG21CS046","ADITYA VIKRAM SINGH",5,'B',"5B"),
("PES1UG21CS047","ADRIJA BANERJEE",5,'B',"5B"),
("PES1UG21CS048","ADVAY AGRAWAL",5,'B',"5B"),
("PES1UG21CS049","ADVIKA VARSHA NAIK",5,'B',"5B"),
("PES1UG21CS050","AGNEL ELIZABETH",5,'B',"5B"),
("PES1UG21CS051","AISHWARYA L PATIL",5,'B',"5B"),
("PES1UG21CS052","AJEY BHAT",5,'B',"5B"),
("PES1UG21CS053","AKANKSHA PRABHANNA MULGUND",5,'B',"5B"),
("PES1UG21CS054","AKANKSHA SENDHIL",5,'B',"5B"),
("PES1UG21CS055","AKASH KAMALESH",5,'B',"5B"),
("PES1UG21CS056","AKASH SHIDDANAGOUDAR",5,'B',"5B"),
("PES1UG21CS057","AKASH VIJAYAKUMAR ANGADI",5,'B',"5B"),
("PES1UG21CS058","AKHILESH M K",5,'B',"5B"),
("PES1UG21CS059","AKSHAR S",5,'B',"5B"),
("PES1UG21CS060","AKSHATA LAXMAN PAWAR",5,'B',"5B"),
("PES1UG21CS061","AKSHATHA M K",5,'B',"5B"),
("PES1UG21CS062","AKSHATHA P",5,'B',"5B"),
("PES1UG21CS063","AKSHAY ANAND",5,'B',"5B"),
("PES1UG21CS064","AKSHAY PRASAD HONNAVALLI",5,'B',"5B"),
("PES1UG21CS065","AMBATI REVANTH SREERAM",5,'B',"5B"),
("PES1UG21CS066","GANYA U ",5,'B',"5B"),
("PES1UG21CS067","A GEETHIKA CHOWDARY",5,'B',"5B"),
("PES1UG21CS068","A B SAGAR YADAV ",5,'B',"5B"),
("PES1UG21CS069","Nistha Singh",5,'B',"5B"),
("PES1UG21CS070","ADITYA KORISHETTY",5,'B',"5B"),
("PES1UG21CS071","RACHAPPA",5,'B',"5B"),
("PES1UG21CS072","ALAPATI NAGA VENKATA CHARAN",5,'B',"5B"),
("PES1UG21CS073","ALSTON RICHARD ARANHA",5,'B',"5B"),
("PES1UG21CS074","AMAAN FEROZ",5,'B',"5B"),
("PES1UG21CS075","AMARA SAI ANITEJ",5,'B',"5B"),
("PES1UG21CS076","AMISH GUPTA",5,'B',"5B"),
("PES1UG21CS077","AMOGH BHARNE",5,'B',"5B"),
("PES1UG21CS078","AMRITHA G K",5,'B',"5B"),
("PES1UG21CS079","AMULYA MARALI",5,'B',"5B"),
("PES1UG21CS080","ANAGHA SIDDHESHWAR",5,'B',"5B"),
("PES1UG21CS081","ANANYA J",5,'C',"5C"),
("PES1UG21CS082","ANANYA JHA",5,'C',"5C"),
("PES1UG21CS083","ANANYA MAHISHI",5,'C',"5C"),
("PES1UG21CS084","ANANYA PRASAD B",5,'C',"5C"),
("PES1UG21CS085","ANEESH K B",5,'C',"5C"),
("PES1UG21CS086","ANIKETH MADHUGIRI",5,'C',"5C"),
("PES1UG21CS087","ANIKETHANA A M",5,'C',"5C"),
("PES1UG21CS088","ANIMAN KUMAR",5,'C',"5C"),
("PES1UG21CS089","ANIMESH BHAIJI",5,'C',"5C"),
("PES1UG21CS090","ANIRUDH G JOSHI",5,'C',"5C"),
("PES1UG21CS091","ANIRUDH LAKHOTIA",5,'C',"5C"),
("PES1UG21CS092","ANIRUDH REVANUR",5,'C',"5C"),
("PES1UG21CS093","ANJAN R PRASAD",5,'C',"5C"),
("PES1UG21CS094","ANKIREDDY SAI SANDEEP REDDY",5,'C',"5C"),
("PES1UG21CS095","ANKITHA. A",5,'C',"5C"),
("PES1UG21CS096","ANKUSH H V",5,'C',"5C"),
("PES1UG21CS097","ANOOSH DAMODAR",5,'C',"5C"),
("PES1UG21CS098","ANOUSHKA VEMIREDDY",5,'C',"5C"),
("PES1UG21CS099","ANSHUL DASYAM",5,'C',"5C"),
("PES1UG21CS100","ANSHUL RAMDAS BALIGA",5,'C',"5C"),
("PES1UG21CS101","ANSHUL RANJAN",5,'C',"5C"),
("PES1UG21CS102","ANUP PRAKASH BACCHE",5,'C',"5C"),
("PES1UG21CS103","AMULYA N",5,'C',"5C"),
("PES1UG21CS104","ANKITHA A C",5,'C',"5C"),
("PES1UG21CS105","AYSHA RAHBAR",5,'C',"5C"),
("PES1UG21CS106","ANUPAMA KAMATH",5,'C',"5C"),
("PES1UG21CS107","ANURAG BASAVARAJ BHUSARE",5,'C',"5C"),
("PES1UG21CS108","ANURAG N KOPPAL",5,'C',"5C"),
("PES1UG21CS109","ANUSHA M V",5,'C',"5C"),
("PES1UG21CS110","ANUSHKA GHEI",5,'C',"5C"),
("PES1UG21CS111","ANVESHA NAYAK",5,'C',"5C"),
("PES1UG21CS112","APOORVA RAJ",5,'C',"5C"),
("PES1UG21CS113","ARADHANA MAHATI",5,'C',"5C"),
("PES1UG21CS114","ARCHISHMAN VB",5,'C',"5C"),
("PES1UG21CS115","ARNAB KARMAKAR",5,'C',"5C"),
("PES1UG21CS116","ARNAV SRINIVAS ATREY",5,'C',"5C"),
("PES1UG21CS117","ARPIT AGARWAL",5,'C',"5C"),
("PES1UG21CS118","ARSHYA KHURANA",5,'C',"5C"),
("PES1UG21CS119","ARUN AMAR KURALI",5,'C',"5C"),
("PES1UG21CS120","ARVIN ARUN NOOLI",5,'C',"5C"),
("PES1UG21CS121","ARYA VINAYAK R",5,'D',"5D"),
("PES1UG21CS122","ARYAMAN S JAIN",5,'D',"5D"),
("PES1UG21CS123","ARYAN GUPTA",5,'D',"5D"),
("PES1UG21CS124","ARYAN SHARMA",5,'D',"5D"),
("PES1UG21CS125","ARYANSH KHICHAR ",5,'D',"5D"),
("PES1UG21CS126","ASHAY NAIK",5,'D',"5D"),
("PES1UG21CS127","ASHLIN FURTADO",5,'D',"5D"),
("PES1UG21CS128","ASHRIT BHARADWAJ",5,'D',"5D"),
("PES1UG21CS129","ASHVIN BHAT",5,'D',"5D"),
("PES1UG21CS130","ASHVIN SHARMA",5,'D',"5D"),
("PES1UG21CS131","ASHWIN RAGUPATHY",5,'D',"5D"),
("PES1UG21CS132","ASHWINI VENKATARAMAN HEGDE",5,'D',"5D"),
("PES1UG21CS133","ARYAN KUMAR",5,'D',"5D"),
("PES1UG21CS134","Ruchitha V S",5,'D',"5D"),
("PES1UG21CS135","AMRITHA S",5,'D',"5D"),
("PES1UG21CS136","ANUSHREE M SULIBHAVI",5,'D',"5D"),
("PES1UG21CS137","ALETI SAHITH REDDY",5,'D',"5D"),
("PES1UG21CS138","AYUSH SHANDILYA",5,'D',"5D"),
("PES1UG21CS139","CHANDU NAIK",5,'D',"5D"),
("PES1UG21CS140","DARSHAN KRISHNA HEGDE",5,'D',"5D"),
("PES1UG21CS141","ATHUL RAIMON",5,'D',"5D"),
("PES1UG21CS142","ATLA SRIVATSAV",5,'D',"5D"),
("PES1UG21CS143","AVANISH SHENOY",5,'D',"5D"),
("PES1UG21CS144","AYUSH SINHA",5,'D',"5D"),
("PES1UG21CS145","B MONISH MOGER",5,'D',"5D"),
("PES1UG21CS146","B S PRANAV SRIKAR",5,'D',"5D"),
("PES1UG21CS147","BALAKRISHNA DICHITHA",5,'D',"5D"),
("PES1UG21CS148","BASAVARAJ NARAYANAPPA HARAVI",5,'D',"5D"),
("PES1UG21CS149","BAVIGADDA JAGAN SAI",5,'D',"5D"),
("PES1UG21CS150","BENNY SHRIYA E M",5,'D',"5D"),
("PES1UG21CS151","BHARAT",5,'D',"5D"),
("PES1UG21CS152","BHARATH RAJA PK",5,'D',"5D"),
("PES1UG21CS153","BHAVANA BHIMASHANKAR HUGAR",5,'D',"5D"),
("PES1UG21CS154","BHOOMI BHAT",5,'D',"5D"),
("PES1UG21CS155","BHOOMIKA B K",5,'D',"5D"),
("PES1UG21CS156","BHUVAN VIJAY KUMAR",5,'D',"5D"),
("PES1UG21CS157","BOMMISETTY BALA LAKSHMI DEEPTHI ",5,'D',"5D"),
("PES1UG21CS158","BONTHA SREENIVASA REDDY ",5,'D',"5D"),
("PES1UG21CS159","BRUNDA L",5,'D',"5D"),
("PES1UG21CS160","C V NAMRATA",5,'D',"5D"),
("PES1UG21CS161","CHAITRA PAIDIKONDALA",5,'E',"5E"),
("PES1UG21CS162","CHANDA NIKHIL",5,'E',"5E"),
("PES1UG21CS163","CHANDAN K H",5,'E',"5E"),
("PES1UG21CS164","CHANDANA",5,'E',"5E"),
("PES1UG21CS165","CHANDANA S M",5,'E',"5E"),
("PES1UG21CS166","CHANDRACHUD SARATH",5,'E',"5E"),
("PES1UG21CS167","CHARITHA K REDDY",5,'E',"5E"),
("PES1UG21CS168","CHARUTHA RAJEESH",5,'E',"5E"),
("PES1UG21CS169","CHETAN G MUNDASAD",5,'E',"5E"),
("PES1UG21CS170","CHETAN S",5,'E',"5E"),
("PES1UG21CS171","CHETANA MITAL",5,'E',"5E"),
("PES1UG21CS172","CHETHAN R",5,'E',"5E"),
("PES1UG21CS173","CHIRAG H",5,'E',"5E"),
("PES1UG21CS174","DHRUV MOHAN BHAT",5,'E',"5E"),
("PES1UG21CS175","GOURVI KALA",5,'E',"5E"),
("PES1UG21CS176","CHIRAG HEGDE",5,'E',"5E"),
("PES1UG21CS177","CHIRANTH TS",5,'E',"5E"),
("PES1UG21CS178","CHITTESH KUMAR KANIPAKAM",5,'E',"5E"),
("PES1UG21CS179","CHOUGULE NEHA RAJKUMAR",5,'E',"5E"),
("PES1UG21CS180","CHUNCHU RITHWIK SAI SURYA ",5,'E',"5E"),
("PES1UG21CS181","CM ABHAY",5,'E',"5E"),
("PES1UG21CS182","D L RAMESHWAR",5,'E',"5E"),
("PES1UG21CS183","DANISH AHMED",5,'E',"5E"),
("PES1UG21CS184","DARSH AGARWAL",5,'E',"5E"),
("PES1UG21CS185","DARSHAN BABU T R ",5,'E',"5E"),
("PES1UG21CS186","DARSHAN V",5,'E',"5E"),
("PES1UG21CS187","DEEKSHA KRISHNAPPA",5,'E',"5E"),
("PES1UG21CS188","DEEPAK PARMAR",5,'E',"5E"),
("PES1UG21CS189","DEVIKA MENON",5,'E',"5E"),
("PES1UG21CS190","DHANUSH KUMAR B",5,'E',"5E"),
("PES1UG21CS191","DHARAN SHETTY",5,'E',"5E"),
("PES1UG21CS192","DHEERAJ MRUTYUNJAY HAVALE",5,'E',"5E"),
("PES1UG21CS193","DHRITI RAJESH KRISHNAN",5,'E',"5E"),
("PES1UG21CS194","DHRUV BALWANT SURTI",5,'E',"5E"),
("PES1UG21CS195","DHRUV PODUVAL",5,'E',"5E"),
("PES1UG21CS196","DHRUV PRASHANT NILKUND",5,'E',"5E"),
("PES1UG21CS197","DHRUV S MOMAYA",5,'E',"5E"),
("PES1UG21CS198","DHRUVA S NAYAK",5,'E',"5E"),
("PES1UG21CS199","DIGVIJAY SUNIL",5,'E',"5E"),
("PES1UG21CS200","DILIP H",5,'E',"5E");

