#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect() 
    c = db.cursor()
    c.execute("delete from Matches;")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("delete from Players;")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(*) from Players;")
    results = c.fetchall()
    db.close() 
    return results[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("insert into Players (name) values (%s);", (name, ))
    db.commit()
    db.close()

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
    db = connect()
    c = db.cursor()
    c.execute("select * from Standings;")
    rows = c.fetchall()
    db.close()
    results = []
    for row in rows:
        results.append((row[0], row[1], row[2], row[3])) 
    return results   

def reportMatch(winner, loser, draw):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    if draw:
        c.execute("insert into Matches (player, opponent, result) values (%s, %s, 0);", (winner, loser))
        c.execute("insert into Matches (player, opponent, result) values (%s, %s, 0);", (loser, winner))
    else:
        c.execute("insert into Matches (player, opponent, result) values (%s, %s, 1);", (winner, loser))
        c.execute("insert into Matches (player, opponent, result) values (%s, %s, 0);", (loser, winner))
    db.commit()
    db.close() 
 
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
    db = connect()
    c = db.cursor()
    c.execute("select i, n, w from Standings")
    rows = c.fetchall()
    results = []
    index = 0
    pair = ()
    for row in rows:
        if index == 0:
            pair = (row[0], row[1], None, None)
            index = 1
        else:
            pair = (pair[0], pair[1], row[0], row[1])
            results.append(pair)
            pair = ()
            index = 0
    db.commit()
    db.close()
    return results

