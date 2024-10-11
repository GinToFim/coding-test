-- 코드를 입력하세요
SELECT
    info.rest_id,
    info.rest_name,
    info.food_type,
    info.favorites,
    info.address,
    ROUND(AVG(review.review_score), 2) AS score
  FROM rest_info AS info, rest_review AS review
 WHERE info.rest_id = review.rest_id
   AND address LIKE '서울%'
 GROUP BY 1
 ORDER BY 6 DESC, 4 DESC;

  