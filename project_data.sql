CREATE TABLE GAME_T (
    GameID SERIAL,
    GameDate DATE,
    OffenseTeam char(3),
    DefenseTeam char(3),
    Down int,
    ToGo int,
    Yards int,Recorded time	Event	Process ID	Payload
No data found
ERROR:  could not open file "C:\Users\rcarm\OneDrive\Desktop\Analysis Projects\Group Project\dataset.csv" for reading: Permission denied
HINT:  COPY FROM inst
    YardsDelta int,
    Successful varchar(10),
    Formation varchar(20),
    PlayType varchar(20)

    
);


COPY GAME_T(GameDate, OffenseTeam, DefenseTeam, Down, ToGo, Yards, 
YardsDelta, Successful, Formation, PlayType)
FROM 'C:\Users\rcarm\OneDrive\Desktop\Analysis Projects\Group Project\dataset.csv'
DELIMITER ','
CSV HEADER;
