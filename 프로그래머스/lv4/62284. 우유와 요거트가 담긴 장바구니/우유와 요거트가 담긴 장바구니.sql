-- 코드를 입력하세요
SELECT cart_id
  FROM cart_products
 WHERE cart_id IN (
     SELECT cart_id
       FROM cart_products
      WHERE name = 'Milk'
 ) AND cart_id IN (
      SELECT cart_id
       FROM cart_products
      WHERE name = 'Yogurt'
 )
 GROUP BY 1
 ORDER BY ID;
