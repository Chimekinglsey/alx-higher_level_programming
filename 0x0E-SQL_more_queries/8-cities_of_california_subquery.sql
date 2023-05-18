-- DML sccript that lists all cities of California found
-- in the hbtn_0d_usa database
USE hbtn_0d_usa;
SELECT * FROM states WHERE 'name' = 'California' ASC AND 'id' = SELECT city_id FROM city where 'name' = 'California'
