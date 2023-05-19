-- DML sccript that lists all cities of California found
-- in the hbtn_0d_usa database
--SELECT * FROM states WHERE 'name' = 'California' ASC AND 'id' = SELECT city_id FROM city where 'name' = 'California'
SELECT id, name 
FROM cities 
WHERE state_id = 
	(SELECT id
	FROM state WHERE name = 'California') 
ORDER BY cities.id ASC;
