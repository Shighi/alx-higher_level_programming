-- Creates the temperatures table
CREATE TABLE temperatures (
    city VARCHAR(64) NOT NULL,
    country VARCHAR(64) NOT NULL,
    season VARCHAR(32) NOT NULL,
    average_temperature FLOAT
);
