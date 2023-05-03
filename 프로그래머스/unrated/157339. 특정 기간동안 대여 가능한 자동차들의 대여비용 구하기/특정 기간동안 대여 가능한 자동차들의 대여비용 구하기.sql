/*
'세단' OR 'SUV'이고
2022년 11월 1일 ~ 2022년 11월 30일까지 대여 가능 
AND
30일간의 대여 금액이 50만원 이상 200만원 미만이 자동차

*/
SELECT cr.car_id, cr.car_type,
       ROUND(cr.daily_fee * 30 * (100 - pn.discount_rate) / 100, 0) AS FEE
  FROM car_rental_company_car AS cr
 INNER JOIN car_rental_company_discount_plan AS pn
    ON cr.car_type = pn.car_type
 WHERE cr.car_id NOT IN (
     SELECT car_id
       FROM car_rental_company_rental_history
      WHERE start_date <= '2022-11-30' AND end_date >= '2022-11-01')
       AND cr.car_type IN ('세단', 'SUV')
       AND pn.duration_type = '30일 이상'
 GROUP BY cr.car_id
HAVING 500000 <= FEE AND FEE < 2000000
 ORDER BY fee DESC, car_type ASC, car_id DESC;