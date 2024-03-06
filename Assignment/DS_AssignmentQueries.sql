-- -------- SQL Queries -------- --

-- Show 2016 T20 World Cup all teams
SELECT t.teamName AS Team, p1.playerName AS 'Captain', p2.playerName AS 'Vice Captain', t.coachName AS Coach
FROM Team t 
INNER JOIN Player p1 ON t.captain = p1.playerID
INNER JOIN Player p2 ON t.viceCaptain = p2.playerID;

-- Show 2016 T20 World Cup all players
SELECT p.playerName AS 'Player', p.playerNo AS 'No', t.teamName AS 'Team', p.DOB AS 'Date of Birth', p.batting AS 'Batting', p.bowling AS 'Bowling'
FROM Player p INNER JOIN Team t
ON p.teamID = t.teamID;

-- Show specific team members(players)
SELECT p.playerName AS 'Player', p.playerNo AS 'No', t.teamName AS 'Team', p.DOB AS 'Date of Birth', p.batting AS 'Batting', p.bowling AS 'Bowling'
FROM Player p INNER JOIN Team t
ON p.teamID = t.teamID
WHERE t.teamName = 'Sri lanka';

-- Show tournament summary
SELECT p.date AS 'Date', t1.teamName AS 'Team 1', t2.teamName AS 'Team 2', p.result AS 'Result'
FROM Plays p
INNER JOIN Team t1 ON p.team1 = t1.teamID
INNER JOIN Team t2 ON p.team2 = t2.teamID;

-- Show detailed tournament information
SELECT m.date AS 'Date', m.category AS 'Category', CONCAT(t1.teamName, ' vs ', t2.teamName) AS 'Between', s.stadiumName AS 'Stadium', 
m.winningTeamScore AS 'Winning Team Score', m.losingTeamScore AS 'Losing Team Score', t3.teamName AS 'Won', p.playerName AS 'Player of the Match'
FROM MatchInfo m 
INNER JOIN Team t1 ON m.team1 = t1.teamID
INNER JOIN Team t2 ON m.team2 = t2.teamID
INNER JOIN Team t3 ON m.winnerTeam = t3.teamID
INNER JOIN Stadium s ON m.stadium = s.stadiumID
INNER JOIN Player p ON m.POM = p.playerID
ORDER BY m.date;

-- Show specific match category
SELECT m.date AS 'Date', m.category AS 'Category', CONCAT(t1.teamName, ' vs ', t2.teamName) AS 'Between', s.stadiumName AS 'Stadium', 
m.winningTeamScore AS 'Winning Team Score', m.losingTeamScore AS 'Losing Team Score', t3.teamName AS 'Won', p.playerName AS 'Player of the Match'
FROM MatchInfo m 
INNER JOIN Team t1 ON m.team1 = t1.teamID
INNER JOIN Team t2 ON m.team2 = t2.teamID
INNER JOIN Team t3 ON m.winnerTeam = t3.teamID
INNER JOIN Stadium s ON m.stadium = s.stadiumID
INNER JOIN Player p ON m.POM = p.playerID
WHERE m.category = 'Final';

-- Show stadium details
SELECT stadiumName AS 'Stadium', location AS 'Location', capacity AS 'Maximum Capacity'  
FROM Stadium;

-- Show specific team played matches
SELECT m.date AS 'Date', CONCAT(t1.teamName, ' vs ', t2.teamName) AS 'Between', t3.teamName AS 'Won'
FROM MatchInfo m
INNER JOIN Team t1 ON m.team1 = t1.teamID
INNER JOIN Team t2 ON m.team2 = t2.teamID
INNER JOIN Team t3 ON m.winnerTeam = t3.teamID
WHERE t1.teamName = 'Sri lanka' OR t2.teamName = 'Sri lanka';

-- Show teams win match count
SELECT t.teamName, COUNT(*) AS Won
FROM MatchInfo m
INNER JOIN Team t ON m.winnerTeam = t.teamID
GROUP BY t.teamName;

-- Show the team which has most wins
SELECT *
FROM (SELECT t1.teamName AS TeamName, COUNT(*) AS Won
      FROM MatchInfo m1
      INNER JOIN Team t1 ON m1.winnerTeam = t1.teamID
      GROUP BY m1.winnerTeam) r1
WHERE r1.Won = (SELECT MAX(Won)
                FROM (SELECT t2.teamName AS TeamName, COUNT(*) AS Won
                      FROM MatchInfo m2
                      INNER JOIN Team t2 ON m2.winnerTeam = t2.teamID
                      GROUP BY m2.winnerTeam )r2);

-- OR --                      
SELECT t.teamName, COUNT(*) AS Won
FROM MatchInfo m
INNER JOIN Team t ON m.winnerTeam = t.teamID
GROUP BY t.teamName ORDER BY COUNT(t.teamName) DESC LIMIT 1;

-- Show player awards
SELECT p.playerName AS 'Player Name', COUNT(*) AS 'Awarded (times)'
FROM MatchInfo m
INNER JOIN Player p ON m.POM = p.playerID
GROUP BY m.POM;


-- -------- Advanced Concepts -------- --

-- Views
-- Show players
create view TeamMembers as
SELECT p.playerName AS 'Player', p.playerNo AS 'No', t.teamName AS 'Team', p.DOB AS 'Date of Birth', p.batting AS 'Batting', p.bowling AS 'Bowling'
FROM Player p INNER JOIN Team t
ON p.teamID = t.teamID;

-- Test views
-- SELECT * FROM TeamMembers WHERE Team = 'South Africa';


-- Stored Procedures
-- Insert data to Team table
DELIMITER $$
CREATE PROCEDURE insertTeam(
    id CHAR(4),
    tName VARCHAR(40),
    cap CHAR(4),
    vice CHAR(4),
    coach VARCHAR(40)
)
COMMENT 'Insert data to Team table'
BEGIN 
INSERT INTO Team 
VALUES(id,tName,cap,vice,coach);
END
$$
DELIMITER ;

-- Insert data to Player table
DELIMITER $$
CREATE PROCEDURE insertPlayer(
    id CHAR(4),
    pName VARCHAR(40),
    pNo INT,
    tID CHAR(4),
    DOB DATE,
    bat VARCHAR(40),
    ball VARCHAR(40)
)
COMMENT 'Insert data to Player table'
BEGIN 
INSERT INTO Player 
VALUES(id,pName,pNo,tID,DOB,bat,ball);
END
$$
DELIMITER ;

-- Insert data to Stadium table
DELIMITER $$
CREATE PROCEDURE insertStadium(
    id CHAR(4),
    name VARCHAR(100),
    loc VARCHAR(100),
    capacity INT
)
COMMENT 'Insert data to Stadium table'
BEGIN 
INSERT INTO Stadium 
VALUES(id,name,loc,capacity);
END
$$
DELIMITER ;

-- Insert data to MatchInfo table
DELIMITER $$
CREATE PROCEDURE insertMatch(
    date DATE,
    category VARCHAR(40),
    team1 CHAR(4),
    team2 CHAR(4),
    stadium CHAR(4),
    winningTeamScore VARCHAR(40),
    losingTeamScore VARCHAR(40),
    won CHAR(4),
    pom CHAR(4)
)
COMMENT 'Insert data to MatchInfo table'
BEGIN 
INSERT INTO MatchInfo 
VALUES(date,category,team1,team2,stadium,winningTeamScore,losingTeamScore,won,pom);
END
$$
DELIMITER ;

-- Test stored procedures
-- CALL insertTeam('tt01','test team','p003','p004','test coach');
-- CALL insertPlayer('pp01','test player',23,'tt01','1981-07-07','test bat','test ball');
-- CALL insertStadium('ss01','test stadium','test location',0000);
-- CALL insertMatch('2016-05-05','test category','tt01','tt01','ss01','test w score','test l score','tt01','pp01');


-- Triggers
-- Update Plays table after inserting data to MatchInfo table
DROP TRIGGER IF EXISTS after_insert_matchInfo;
DELIMITER $$
CREATE TRIGGER after_insert_matchInfo 
AFTER INSERT ON MatchInfo
FOR EACH ROW
BEGIN
INSERT INTO Plays 
VALUES(NEW.date,NEW.team1,NEW.team2,CONCAT((SELECT teamName
                                            FROM Team 
                                            WHERE teamID = NEW.winnerTeam), ' won by ', NEW.winningTeamScore));
END 
$$
DELIMITER ;

-- Test triggers
-- INSERT INTO MatchInfo VALUES('2017-04-12','Testing trigger','t007','t005','s002','124/6(15 overs)','118/9(20 overs)','t007','p094');
-- SELECT * FROM Plays;