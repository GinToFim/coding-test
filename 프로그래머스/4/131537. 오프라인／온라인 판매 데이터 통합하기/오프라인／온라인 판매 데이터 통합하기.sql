-- 코드를 입력하세요
(SELECT DATE_FORMAT(sales_date, "%Y-%m-%d"), 
        product_id, user_id, sales_amount
   FROM online_sale
  WHERE YEAR(sales_date) = 2022 AND MONTH(sales_date) = 3)
  
  UNION
  
(SELECT DATE_FORMAT(sales_date, "%Y-%m-%d"), 
        product_id, NULL AS user_id, sales_amount
   FROM offline_sale
  WHERE YEAR(sales_date) = 2022 AND MONTH(sales_date) = 3)
  
 ORDER BY 1, 2, 3;