# Udacity: Intro to Relational Databases
### Tournament project
Database that keeps track of players and matches in a game tournament using the Swiss system for pairing up players in each round. There is no elimination. Each players is matched with another player with a similar win record as them. This project is a Python module that uses PostgreSQL.

### Files
* tournament.sql - Creates database tables using implemented definitions
* tournament.py -- Implementation
* tournament_test.py -- Basic test cases

### Usage
It requires PostgreSQL, Virtualbox, Python and Vagrant. It can be launched with [Vagrant](https://www.vagrantup.com/) by using the command `vagrant up` then `vagrant ssh`.

Run PostgreSQL with `psql`. Make sure you run this in the same directory as the tournament files
Then import the tournament sql file with `\i tournament.sql;`
