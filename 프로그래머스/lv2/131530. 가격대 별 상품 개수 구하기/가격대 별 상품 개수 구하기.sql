# 80000

SELECT CASE 
            WHEN price >= 0 AND price < 10000 THEN '0'
            WHEN price >= 10000 AND price < 20000 THEN '10000'
            WHEN price >= 20000 AND price < 30000 THEN '20000'
            WHEN price >= 30000 AND price < 40000 THEN '30000'
            WHEN price >= 40000 AND price < 50000 THEN '40000'
            WHEN price >= 50000 AND price < 60000 THEN '50000'
            WHEN price >= 60000 AND price < 70000 THEN '60000'
            WHEN price >= 70000 AND price < 80000 THEN '70000'
            WHEN price >= 80000 AND price < 90000 THEN '80000'
       END AS price_group,
       COUNT(*) AS products
  FROM product
 GROUP BY 1
 ORDER BY 1;