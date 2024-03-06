import mysql.connector
from tabulate import tabulate


def runPrograme():
    global conn
    conn = makeConnection()
    mainMenu()


def mainMenu():
    menuUI = """
    *** ICC T20 World Cup 2016 - DATABASE ***

    1 > Retrive Data
    2 > Insert Data
    0 > Exit
    """

    print(menuUI)
    option = input("Enter your option: ")
    while option != "0":

        if option == "1":
            retrieveData()
        elif option == "2":
            insertData()
        else:
            print("Invalid input!")

        print(menuUI)
        option = input("Enter your option: ")

    print("Good Bye...")


def retrieveData():
    menuUI = """
    -- Retrive Data --

    1 > Show 2016 T20 World Cup all teams
    2 > Show 2016 T20 World Cup all players
    3 > Show specific team members(players)
    4 > Show tournament summary
    5 > Show detailed tournament information
    6 > Show specific match category
    7 > Show stadium details
    8 > Show specific team played matches
    9 > Show the team which has most wins
    10 > Show player awards
    0 > Go Back
    """

    print(menuUI)
    option = input("Enter your option: ")
    while option != "0":

        if option == "1":
            print("\n--- 2016 T20 World Cup all teams ---\n")
            showAllTeams()
        elif option == "2":
            print("\n--- 2016 T20 World Cup all players ---\n")
            showAllPlayers()
        elif option == "3":
            print("\n--- Show specific team members(players) ---\n")
            showATeam()
        elif option == "4":
            print("\n--- Show tournament summary ---\n")
            showMatchSummery()
        elif option == "5":
            print("\n--- Show detailed tournament information ---\n")
            showMatchDetails()
        elif option == "6":
            print("\n--- Show specific match category ---\n")
            showMatchCategory()
        elif option == "7":
            print("\n--- Show stadium details ---\n")
            showStadiums()
        elif option == "8":
            print("\n--- Show specific team played matches ---\n")
            showTeamMatches()
        elif option == "9":
            print("\n--- Show the team which has most wins ---\n")
            showMostWins()
        elif option == "10":
            print("\n--- Show player awards ---\n")
            showAwards()
        else:
            print("Invalid input!")

        print(menuUI)
        option = input("Enter your option: ")


def insertData():
    menuUI = """
    -- Insert Data --

    1 > Insert Data to Team table
    2 > Insert Data to Player table
    3 > Insert Data to Stadium table
    4 > Insert Data to MatchInfo table
    0 > Go Back
    """

    print(menuUI)
    option = input("Enter your option: ")
    while option != "0":

        if option == "1":
            print("Inserting Data to Team table")
            insertTeam()
        elif option == "2":
            print("Inserting Data to Player table")
            insertPlayer()
        elif option == "3":
            print("Inserting Data to Stadium table")
            insertStadium()
        elif option == "4":
            print("Inserting Data to MatchInfo table")
            insertMatch()
        else:
            print("Invalid input!")

        print(menuUI)
        option = input("Enter your option: ")

    print("Good Bye...")


def makeConnection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="blackops",
            database="t20worldcup2016_20783462"
        )
        if (conn):
            print("Connection Successful")
            return conn

    except:
        print("Error occured!")


def display(connection, query):
    mycursor = connection.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    fields = [i[0] for i in mycursor.description]
    print(tabulate(myresult, headers=fields, tablefmt='psql'))


def insert(connection, query, data):
    mycursor = connection.cursor()
    mycursor.execute(query, data)


# Show 2016 T20 World Cup all teams
def showAllTeams():
    query = """SELECT t.teamName AS Team, p1.playerName AS 'Captain', p2.playerName AS 'Vice Captain', t.coachName AS Coach
            FROM Team t 
            INNER JOIN Player p1 ON t.captain = p1.playerID
            INNER JOIN Player p2 ON t.viceCaptain = p2.playerID;"""
    display(conn, query)


# Show 2016 T20 World Cup all players
def showAllPlayers():
    query = """SELECT p.playerName AS 'Player', p.playerNo AS 'No', t.teamName AS 'Team', p.DOB AS 'Date of Birth', p.batting AS 'Batting', p.bowling AS 'Bowling'
            FROM Player p INNER JOIN Team t
            ON p.teamID = t.teamID"""
    display(conn, query)


# Show specific team members(players)
def showATeam():
    team = input("Enter the Team Name: ")
    query = """SELECT p.playerName AS 'Player', p.playerNo AS 'No', t.teamName AS 'Team', p.DOB AS 'Date of Birth', p.batting AS 'Batting', p.bowling AS 'Bowling'
            FROM Player p INNER JOIN Team t
            ON p.teamID = t.teamID
            WHERE t.teamName = '""" + team + """'"""
    display(conn, query)


# Show tournament summary
def showMatchSummery():
    query = """SELECT p.date AS 'Date', t1.teamName AS 'Team 1', t2.teamName AS 'Team 2', p.result AS 'Result'
            FROM Plays p
            INNER JOIN Team t1 ON p.team1 = t1.teamID
            INNER JOIN Team t2 ON p.team2 = t2.teamID"""
    display(conn, query)


# Show detailed tournament information
def showMatchDetails():
    query = """SELECT m.date AS 'Date', m.category AS 'Category', CONCAT(t1.teamName, ' vs ', t2.teamName) AS 'Between', s.stadiumName AS 'Stadium', 
            m.winningTeamScore AS 'Winning Team Score', m.losingTeamScore AS 'Losing Team Score', t3.teamName AS 'Won', p.playerName AS 'Player of the Match'
            FROM MatchInfo m 
            INNER JOIN Team t1 ON m.team1 = t1.teamID
            INNER JOIN Team t2 ON m.team2 = t2.teamID
            INNER JOIN Team t3 ON m.winnerTeam = t3.teamID
            INNER JOIN Stadium s ON m.stadium = s.stadiumID
            INNER JOIN Player p ON m.POM = p.playerID
            ORDER BY m.date"""
    display(conn, query)


# Show specific match category
def showMatchCategory():
    category = input("Enter the Match Category: ")
    query = """SELECT m.date AS 'Date', m.category AS 'Category', CONCAT(t1.teamName, ' vs ', t2.teamName) AS 'Between', s.stadiumName AS 'Stadium', 
            m.winningTeamScore AS 'Winning Team Score', m.losingTeamScore AS 'Losing Team Score', t3.teamName AS 'Won', p.playerName AS 'Player of the Match'
            FROM MatchInfo m 
            INNER JOIN Team t1 ON m.team1 = t1.teamID
            INNER JOIN Team t2 ON m.team2 = t2.teamID
            INNER JOIN Team t3 ON m.winnerTeam = t3.teamID
            INNER JOIN Stadium s ON m.stadium = s.stadiumID
            INNER JOIN Player p ON m.POM = p.playerID
            WHERE m.category = '""" + category + """'"""
    display(conn, query)


# Show stadium details
def showStadiums():
    query = """SELECT stadiumName AS 'Stadium', location AS 'Location', capacity AS 'Maximum Capacity'  
            FROM Stadium"""
    display(conn, query)


# Show specific team played matches
def showTeamMatches():
    team = input("Enter the Team Name: ")
    query = """SELECT m.date AS 'Date', CONCAT(t1.teamName, ' vs ', t2.teamName) AS 'Between', t3.teamName AS 'Won'
            FROM MatchInfo m
            INNER JOIN Team t1 ON m.team1 = t1.teamID
            INNER JOIN Team t2 ON m.team2 = t2.teamID
            INNER JOIN Team t3 ON m.winnerTeam = t3.teamID
            WHERE t1.teamName = '""" + team + """' OR t2.teamName = '""" + team + """'"""
    display(conn, query)


# Show the team which has most wins
def showMostWins():
    query = """SELECT *
            FROM (SELECT t1.teamName AS TeamName, COUNT(*) AS Won
                  FROM MatchInfo m1
                  INNER JOIN Team t1 ON m1.winnerTeam = t1.teamID
                  GROUP BY m1.winnerTeam) r1
            WHERE r1.Won = (SELECT MAX(Won)
                            FROM (SELECT t2.teamName AS TeamName, COUNT(*) AS Won
                            FROM MatchInfo m2
                            INNER JOIN Team t2 ON m2.winnerTeam = t2.teamID
                            GROUP BY m2.winnerTeam )r2)"""
    display(conn, query)


# Show player awards
def showAwards():
    query = """SELECT p.playerName AS 'Player Name', COUNT(*) AS 'Awarded (times)'
            FROM MatchInfo m
            INNER JOIN Player p ON m.POM = p.playerID
            GROUP BY m.POM"""
    display(conn, query)


# Insert Data to Team table
def insertTeam():
    id = input("Enter the Team ID: ")
    name = input("Enter the Team Name: ")
    captain = input("Enter the Captain Player ID: ")
    vice = input("Enter the Vice Captain Player ID: ")
    coach = input("Enter the Coach Name: ")

    statement = "CALL insertTeam(%s,%s,%s,%s,%s);"
    data = (id, name, captain, vice, coach)

    try:
        insert(conn, statement, data)
        print("Data added successfully.")
    except:
        print("Error while inserting!")


# Insert Data to Player table
def insertPlayer():
    id = input("Enter the Player ID: ")
    name = input("Enter the Player Name: ")
    no = input("Enter the Player No: ")
    team = input("Enter the Player team ID: ")
    birth = input("Enter the Player Birthday: ")
    bat = input("Enter the Player Batting style: ")
    ball = input("Enter the Player Bowling style: ")

    statement = "CALL insertPlayer(%s,%s,%s,%s,%s,%s,%s);"
    data = (id, name, no, team, birth, bat, ball)

    try:
        insert(conn, statement, data)
        print("Data added successfully.")
    except:
        print("Error while inserting!")


# Insert Data to Stadium table
def insertStadium():
    id = input("Enter the Stadium ID: ")
    name = input("Enter the Stadium Name: ")
    loc = input("Enter the Stadium Location: ")
    capacity = input("Enter the Stadium Capacity: ")

    statement = "CALL insertStadium(%s,%s,%s,%s);"
    data = (id, name, loc, capacity)

    try:
        insert(conn, statement, data)
        print("Data added successfully.")
    except:
        print("Error while inserting!")


# Insert Data to MatchInfo table
def insertMatch():
    mDate = input("Enter the Match date: ")
    category = input("Enter the Match category: ")
    team1 = input("Enter the team 1 ID: ")
    team2 = input("Enter the team 2 ID: ")
    stadium = input("Enter the stadium ID: ")
    wScore = input("Enter the winning team score: ")
    lScore = input("Enter the losing team score: ")
    won = input("Enter the winning team ID: ")
    pom = input("Enter the Player of the match player ID: ")

    statement = "CALL insertMatch(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    data = (mDate, category, team1, team2, stadium, wScore, lScore, won, pom)

    try:
        insert(conn, statement, data)
        print("Data added successfully.")
    except:
        print("Error while inserting!")


runPrograme()
