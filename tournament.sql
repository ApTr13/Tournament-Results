-- Table definitions for the tournament project.
-- MADE BY - ApTr13
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- Delete all previous Data in the Database
DROP DATABASE tournament;

-- Creating a new database for storing Tournament data
CREATE DATABASE tournament;

-- Connecting to the Database
\c tournament

-- Creating a table for adding New Players
CREATE TABLE Players
(
    ID SERIAL PRIMARY KEY,
    Name text
);

-- Creating a table for reporting new matches
CREATE TABLE Matches
(
    Match SERIAL PRIMARY KEY,
    WinID SMALLINT references Players(ID),
    LoseID SMALLINT references Players(ID)
);

-- A temporary VIEW for obtaining count of Wins for every Player
CREATE VIEW Wins AS
SELECT Players.ID as ID, Players.Name as N,count(WinID) as W
FROM Players LEFT JOIN Matches
ON Players.ID = Matches.WinID
GROUP BY Players.ID
;

-- A temporary VIEW for obtaining count of Loses for every Player
CREATE VIEW Loses AS
SELECT Players.ID as ID, Players.Name as N,count(LoseID) as L
FROM Players LEFT JOIN Matches
ON Players.ID = Matches.LoseID
GROUP BY Players.ID
;

-- VIEW of Player-Standings combining the counts of Wins & Loses
-- from the Temporary views *WIns* & *Loses* to get
-- the total number of matches played by every Player
CREATE VIEW Standings AS
SELECT Wins.ID as Id, Wins.N as Name, Wins.W as Victory,
 Wins.W + Loses.L as Match
FROM Wins LEFT JOIN Loses
ON Wins.ID=Loses.ID 
GROUP BY Wins.ID, Wins.N,Wins.W,Loses.L
ORDER BY Wins.W
;

-- A temporary VIEW Swiss for adding a column of Serial Number to Standings
CREATE VIEW Swiss AS
SELECT ROW_NUMBER() OVER(ORDER BY Standings.VIctory) AS Sr,
 Standings.Id as Id, Standings.Name as Name,
 Standings.Victory as Win, Standings.Match as Match
FROM Standings
ORDER BY Win 
;


