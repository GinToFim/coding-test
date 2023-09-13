-- 코드를 입력하세요
SELECT user_id, product_id
  FROM online_sale
 GROUP BY 1, 2
HAVING COUNT(user_id) > 1
 ORDER BY 1 ASC, 2 DESC;