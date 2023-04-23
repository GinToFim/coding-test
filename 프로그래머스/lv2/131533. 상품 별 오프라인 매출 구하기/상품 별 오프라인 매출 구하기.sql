SELECT pd.product_code, 
       SUM(off.sales_amount) * pd.price AS sales
  FROM offline_sale AS off
 INNER JOIN product AS pd
    ON off.product_id = pd.product_id
 GROUP BY 1
 ORDER BY 2 DESC, 1 ASC;