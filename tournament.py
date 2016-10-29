#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
# All Functions created by ApTr13 for obtaining the results of a Swiss Tournamnet 

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("DELETE FROM Matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("DELETE FROM Players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("SELECT count(*) as num FROM Players")
    for row in a.fetchall():
        a = row
    DB.close()
    return a[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("INSERT INTO Players (Name) VALUES (%s)",(name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    """
        THIS QUERY WORKS ON VIEWS. TWO VIEWS *Wins* & *Loses*
        COMBINED TO GET RESULTS IN THE VIEW *Standings* 
    """
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("SELECT * FROM Standings")
    b = a.fetchall()
    for row in b:
        a = row
    DB.close()
    return b


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("INSERT INTO Matches (WinID, LoseID) VALUES (%s,%s)",(winner, loser,))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    """ 
        FIRST A TEMPORARY VIEW *Swiss* IS CREATED, FROM WHICH
        THE GIVEN SELECT QUERY FILTERS THE PAIRINGS

        The Temporary view is created so that Serial number (Sr) can be used
        for the conditions in WHERE clause to create tuples with two ids &
        two names of players at nearly-equally position in table.
    """
    DB = psycopg2.connect("dbname=tournament")
    a = DB.cursor()
    a.execute("SELECT a.Id, a.Name, b.Id, b.Name FROM Swiss as a, Swiss as b WHERE b.Sr = a.Sr + 1 AND a.Sr%2 = 1 ")
    b = a.fetchall()
    for row in b:
        a = row
    DB.close()
    return b


