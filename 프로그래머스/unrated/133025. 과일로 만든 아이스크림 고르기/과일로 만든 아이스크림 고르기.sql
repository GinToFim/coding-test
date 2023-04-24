-- 코드를 입력하세요
SELECT fh.flavor
  FROM first_half AS fh
 INNER JOIN icecream_info AS ice
    ON fh.flavor = ice.flavor
WHERE fh.total_order > 3000 
      AND ice.ingredient_type = 'fruit_based';