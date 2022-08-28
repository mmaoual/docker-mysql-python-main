-- LOAD DATA LOCAL INFILE "database/top250-00-19.csv"
-- INTO TABLE top250_db.football_transfers FIELDS TERMINATED BY "," LINES TERMINATED BY "\r" (Name,Position,Age,Team_from,League_from,Team_to,League_to,Season,Market_value,Transfer_fee);

INSERT INTO top250_db.football_transfers (Name,Position,Age,Team_from,League_from,Team_to,League_to,Season,Market_value,Transfer_fee) 
VALUES ('Luís Figo','Right Winger',27,'FC Barcelona','LaLiga','Real Madrid','LaLiga','2000-2001','NA',60000000);

SELECT * FROM top250_db.football_transfers;