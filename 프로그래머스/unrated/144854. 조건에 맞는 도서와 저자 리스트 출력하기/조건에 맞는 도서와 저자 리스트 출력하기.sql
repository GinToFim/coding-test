-- 코드를 입력하세요
SELECT bk.book_id, ar.author_name, DATE_FORMAT(bk.published_date, '%Y-%m-%d')
  FROM book AS bk
 INNER JOIN author AS ar
    ON bk.author_id = ar.author_id
 WHERE bk.category = '경제'
 ORDER BY 3 ASC;