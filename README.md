# Udacity: Intro to Relational Databases
### Tournament project
Database that keeps track of players and matches in a game tournament using the Swiss system for pairing up players in each round. There is no elimination. Each players is matched with another player with a similar win record as them. This project is a Python module that uses PostgreSQL.

### Features
* Prevents rematches between players. 
* Support games where a draw (tied game) is possible. 

### Files
* tournament.sql - Creates database tables using implemented definitions
* tournament.py -- Implementation
* tournament_test.py -- Basic test cases

### Usage
It requires PostgreSQL, Virtualbox, Python and Vagrant. It can be launched with [Vagrant](https://www.vagrantup.com/) by using the command `vagrant up` then `vagrant ssh`.

Run PostgreSQL with `psql`. Make sure you run this in the same directory as the tournament files.
Then import the tournament sql file with `\i tournament.sql;`.
To run the test cases exit psql with by typing `\q`, then run the python file of test cases with `python tournament_test.py`.

### Methods
##### Register a player
The database assigns a unique id to every player that registers. To register a player with a name call `registerPlayer(name)`. There can be duplicate names.

##### Count players
The call `countPlayers()` returns the number of players currently registered.

##### Get player standings 
Calling `playerStandings()` will return a list of the players and their win records, sorted by wins. This means that the first entry will be the player in first place and so on. The function returns a list of tuples that contains (id, name, # wins, # matches). 

##### Report match
To report the winner and loser of a single match between two players call `reportMatch(winner, loser, draw)` where winner is the id of the player that won the match and loser is the id of the player that lost. If the match was tied, set the draw parameter to 1, otherwise set it to 0.
    
##### Swiss pairings
To get a list of pairs of players that are playing each other in the next round, call `swissPairings()`. This returns a list of tuples which contain (id1, name1, id2, name2)
