-- 코드를 입력하세요
SELECT half.flavor
  FROM first_half AS half
 INNER JOIN icecream_info AS info
    ON half.flavor = info.flavor
 WHERE half.total_order > 3000
   AND info.ingredient_type = 'fruit_based';