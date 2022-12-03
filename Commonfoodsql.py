import mysql.connector
con = mysql.connector.connect(   #connector object
        host = "localhost",
        user = "root",
        password = "tiger",
        database = "schoolnutritionist")
cur = con.cursor()              #creating cursor

       
query1='''
create table common_food
(
Food varchar(20) primary key,
Iron float,
Calcium float,
Proteins float,
VitaminD float,
VitaminC float
);
'''

query2='''
insert into common_food values
("Apple",0.2,7.5,0.5,0,9.2),
("Orange",0.9,55,1,0,83),
("Spinach",0.8,29.7,0.9,0,28),
("Legumes",2,23,7.6,0,0),
("Peas",2,40,4,0,58),
("Milk",0.5,200,8,98,0.1),
("Yogurt",0.2,296,8.5,120,1.96),
("Eggs",1.9,25,6,37,0),
("Fish",0.3,170,40,250,0),
("Chicken",0.8,75,24,7,0);
'''

query3='''
create table patient_intake
(
UserID varchar(25) primary key,
Apple float,
Orange float,
Spinach float,
Legumes float,
Peas float,
Milk float,
Yogurt float,
Eggs float,
Fish float,
Chicken float
);
'''

query4='''
create table patient_nutrilvl
(
UserID varchar(25) primary key,
Iron float,
Calcium float,
Proteins float,
VitaminD float,
VitaminC float
);
'''

query5='''
create table age_group
(
AgeGrp varchar(20) primary key,
Iron float,
Calcium float,
Proteins float,
VitaminD float,
VitaminC float
);
'''

query6='''
insert into age_group values
("Primary",10,1100,19,3000,30),
("Secondary",11,1300,45,4000,50),
("Teacher",10,1000,1,600,80);
'''

cur.execute(query1)              #executing sql cmds
cur.execute(query2)              #executing sql cmds
cur.execute(query3)              #executing sql cmds
cur.execute(query4)              #executing sql cmds
cur.execute(query5)              #executing sql cmds
cur.execute(query6)              #executing sql cmds
cur.execute("commit")
