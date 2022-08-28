DROP DATABASE IF EXISTS top250_db;

CREATE DATABASE top250_db;

CREATE TABLE top250_db.football_transfers (
Name VARCHAR(60) PRIMARY KEY,
Position VARCHAR(100),
Age INT,
Team_from VARCHAR(100),
League_from VARCHAR(100),
Team_to VARCHAR(100),
League_to VARCHAR(100),
Season VARCHAR(20),
Market_value VARCHAR(60),
Transfer_fee DECIMAL(20,2));