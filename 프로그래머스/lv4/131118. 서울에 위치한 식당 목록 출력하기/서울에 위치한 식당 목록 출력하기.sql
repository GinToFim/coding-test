-- 코드를 입력하세요
SELECT info.rest_id, info.rest_name, info.food_type, 
       info.favorites, info.address,
       ROUND(AVG(rv.review_score), 2) AS score
  FROM rest_info AS info
 INNER JOIN rest_review AS rv
    ON info.rest_id = rv.rest_id
 WHERE info.address LIKE "서울%"
 GROUP BY 1
 ORDER BY score DESC, favorites DESC;