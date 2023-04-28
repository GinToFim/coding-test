-- 코드를 입력하세요
SELECT prd.product_id, prd.product_name,
       SUM(prd.price * ord.amount) AS total_sales
  FROM food_product AS prd
 INNER JOIN food_order AS ord
    ON prd.product_id = ord.product_id
  WHERE DATE_FORMAT(ord.produce_date, '%Y-%m') = '2022-05'
  GROUP BY prd.product_id
  ORDER BY total_sales DESC, product_id ASC;