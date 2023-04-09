-- 코드를 입력하세요
SELECT COUNT(user_id) AS users
  FROM user_info
 WHERE age >= 20 AND age <= 29
       AND joined LIKE '2021%';