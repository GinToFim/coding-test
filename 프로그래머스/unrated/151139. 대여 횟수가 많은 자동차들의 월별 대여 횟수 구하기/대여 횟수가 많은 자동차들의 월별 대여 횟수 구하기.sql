-- 코드를 입력하세요
SELECT MONTH(start_date) AS month, car_id, 
       COUNT(car_id) AS records
  FROM car_rental_company_rental_history
 WHERE car_id IN (
     SELECT car_id
       FROM car_rental_company_rental_history
      WHERE DATE_FORMAT(start_date, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
      GROUP BY 1
     HAVING COUNT(car_id) >= 5
       ) AND
       DATE_FORMAT(start_date, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
 GROUP BY 1, 2
 ORDER BY 1 ASC, 2 DESC;