-- 코드를 입력하세요
SELECT cr.car_id, cr.car_type,
       ROUND(cr.daily_fee * 30 * (100 - pn.discount_rate) / 100, 0) AS FEE
  FROM car_rental_company_car AS cr
 INNER JOIN car_rental_company_rental_history AS hy
    ON cr.car_id = hy.car_id
 INNER JOIN car_rental_company_discount_plan AS pn
    ON cr.car_type = pn.car_type
 WHERE cr.car_id NOT IN (
     SELECT car_id
       FROM car_rental_company_rental_history
      WHERE start_date <= '2022-11-30' AND end_date >= '2022-11-01')
       AND cr.car_type IN ('세단', 'SUV')
       AND pn.duration_type = '30일 이상'
 GROUP BY cr.car_id
HAVING fee BETWEEN 500000 AND 1999999
 ORDER BY fee DESC, car_type ASC, car_id DESC;
       

