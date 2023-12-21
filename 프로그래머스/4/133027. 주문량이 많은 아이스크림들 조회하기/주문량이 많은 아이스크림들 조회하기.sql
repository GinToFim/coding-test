-- 코드를 입력하세요
SELECT first_half.flavor
  FROM first_half, july
 WHERE first_half.flavor = july.flavor
 GROUP BY first_half.flavor
 ORDER BY SUM(first_half.total_order + july.total_order) DESC
 LIMIT 3;