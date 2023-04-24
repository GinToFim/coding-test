SELECT user_id, product_id
  FROM online_sale
 GROUP BY 1, 2
HAVING COUNT(product_id) > 1
 ORDER BY user_id ASC, product_id DESC;