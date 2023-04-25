SELECT HOUR(datetime) AS hour, COUNT(HOUR(datetime)) AS count
  FROM animal_outs
 WHERE HOUR(datetime) >= 9 AND HOUR(datetime) < 20
 GROUP BY 1
 ORDER BY 1;
  