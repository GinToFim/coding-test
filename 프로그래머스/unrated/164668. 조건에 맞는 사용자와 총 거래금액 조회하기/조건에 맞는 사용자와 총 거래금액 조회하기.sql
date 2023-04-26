-- 코드를 입력하세요
SELECT usr.user_id, usr.nickname,
       SUM(brd.price) AS total_sales
  FROM used_goods_board AS brd
 INNER JOIN used_goods_user AS usr
    ON brd.writer_id = usr.user_id
 WHERE brd.status = 'DONE'
 GROUP BY 1
 HAVING total_sales >= 700000
 ORDER BY total_sales ASC;