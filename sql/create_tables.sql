-- ===========================================================
-- Project: Restaurant Operations Intelligence Platform
-- Author: Rahmath Mozumder
-- Description: Creates all database tables
-- Database: PostgreSQL
-- ===========================================================


CREATE TABLE branches (
    branch_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    address VARCHAR(200) NOT NULL,
    opening_date DATE NOT NULL,
    seating_capacity INTEGER,
    opening_time TIME,
    closing_time TIME,
    manager_name VARCHAR(100),
    phone_number VARCHAR(20),
    status VARCHAR(20) NOT NULL
);