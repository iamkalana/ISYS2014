-- Create t20worldcup2016_20783462 database and use it.
DROP DATABASE IF EXISTS t20worldcup2016_20783462;
CREATE DATABASE t20worldcup2016_20783462;
USE t20worldcup2016_20783462;


-- Create Team table
DROP TABLE IF EXISTS Team;
CREATE TABLE Team(
    teamID CHAR(4),
    teamName VARCHAR(40),
    captain CHAR(4),
    viceCaptain CHAR(4),
    coachName VARCHAR(40),
    PRIMARY KEY(teamID)
);


-- Create Player table
DROP TABLE IF EXISTS Player;
CREATE TABLE Player(
    playerID CHAR(4),
    playerName VARCHAR(40),
    playerNo INT,
    teamID CHAR(4),
    DOB DATE,
    batting VARCHAR(40),
    bowling VARCHAR(40),
    PRIMARY KEY(playerID),
    FOREIGN KEY(teamID) REFERENCES Team(teamID)
);


-- Create Stadium table
DROP TABLE IF EXISTS Stadium;
CREATE TABLE Stadium(
    stadiumID CHAR(4),
    stadiumName VARCHAR(100),
    location VARCHAR(100),
    capacity INT,
    PRIMARY KEY(stadiumID)
);

-- Create Match table
DROP TABLE IF EXISTS MatchInfo;
CREATE TABLE MatchInfo(
    date DATE,
    category VARCHAR(40),
    team1 CHAR(4),
    team2 CHAR(4),
    stadium CHAR(4),
    winningTeamScore VARCHAR(40),
    losingTeamScore VARCHAR(40),
    winnerTeam CHAR(4),
    POM CHAR(4),
    PRIMARY KEY(date,team1,team2),
    FOREIGN KEY(team1) REFERENCES Team(teamID),
    FOREIGN KEY(team2) REFERENCES Team(teamID),
    FOREIGN KEY(stadium) REFERENCES Stadium(stadiumID),
    FOREIGN KEY(winnerTeam) REFERENCES Team(teamID),
    FOREIGN KEY(POM) REFERENCES Player(playerID)
);

-- Create Plays table
DROP TABLE IF EXISTS Plays;
CREATE TABLE Plays(
    date DATE,
    team1 CHAR(4),
    team2 CHAR(4),
    result VARCHAR(40),
    PRIMARY KEY(date,team1,team2),
    FOREIGN KEY(date) REFERENCES MatchInfo(date),
    FOREIGN KEY(team1) REFERENCES MatchInfo(team1),
    FOREIGN KEY(team2) REFERENCES MatchInfo(team2)
);