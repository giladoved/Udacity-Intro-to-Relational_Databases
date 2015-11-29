-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table Players (
    id serial primary key,
    name text
);

create table Matches (
    id serial primary key,
    player integer not null,
    opponent integer not null,
    result integer not null,
    unique (player, opponent)
);

create view Wins as
    select Players.id, count(Matches.opponent) as w from Players left join (select * from Matches where result > 0) as Matches on Players.id = Matches.player group by players.id order by w desc;

create view Totals as
    select Players.id, count(Matches.opponent) as t from Players left join Matches on Players.id = Matches.player group by Players.id order by t desc;

create view Standings as
    select Players.id as i, Players.name as n, Wins.w as w, Totals.t as t from Players, Totals, Wins where Players.id = Wins.id and Wins.id = Totals.id order by w, t desc;
