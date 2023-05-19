-- DML sccript that lists all cities of California found
-- in the hbtn_0d_usa database
--SELECT * FROM states WHERE 'name' = 'California' ASC AND 'id' = SELECT city_id FROM city where 'name' = 'California'
SELECT cities.id, state.state_id, cities.name 
FROM cities, states 
WHERE state.state_id = 
	(SELECT state.state_id
	FROM state WHERE state.name = 'California') 
ORDER BY cities.id ASC;
