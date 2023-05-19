-- DML sccript that lists all cities of California found
-- in the hbtn_0d_usa database
--SELECT * FROM states WHERE 'name' = 'California' ASC AND 'id' = SELECT city_id FROM city where 'name' = 'California'
SELECT cities.name
FROM cities, states
WHERE cities.state_id = states.id
  AND states.name = 'California'
ORDER BY cities.id ASC;
