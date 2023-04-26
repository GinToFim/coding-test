-- 코드를 입력하세요
SELECT bk.category, SUM(bs.sales)
# SELECT *
  FROM book AS bk
 INNER JOIN book_sales AS bs
    ON bk.book_id = bs.book_id
 WHERE bs.sales_date LIKE '2022-01%'
 GROUP BY 1
 ORDER BY 1;
 