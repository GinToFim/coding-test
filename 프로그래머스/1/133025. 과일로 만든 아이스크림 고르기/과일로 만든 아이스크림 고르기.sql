-- 코드를 입력하세요
SELECT flavor
  FROM icecream_info
 WHERE flavor in (
     SELECT flavor
       FROM first_half
      WHERE total_order > 3000)
   AND ingredient_type = 'fruit_based'
 ORDER BY 1;

