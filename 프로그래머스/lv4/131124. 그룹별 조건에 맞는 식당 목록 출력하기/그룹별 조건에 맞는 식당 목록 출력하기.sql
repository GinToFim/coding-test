-- 코드를 입력하세요
SELECT member_name, review_text,
       DATE_FORMAT(review_date, '%Y-%m-%d') AS review_date
  FROM member_profile AS pf
 INNER JOIN rest_review AS rv
    ON pf.member_id = rv.member_id
 WHERE pf.member_id = (
     SELECT member_id
       FROM rest_review
      GROUP BY member_id
      ORDER BY COUNT(*) DESC
      LIMIT 1)
 ORDER BY 3 ASC, 2 ASC;

