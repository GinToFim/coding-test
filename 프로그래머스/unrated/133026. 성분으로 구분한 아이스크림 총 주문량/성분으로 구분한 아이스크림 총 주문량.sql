-- 코드를 입력하세요
SELECT ice.ingredient_type, SUM(fh.total_order) AS total_order
  FROM first_half AS fh
  LEFT JOIN icecream_info AS ice
        ON fh.flavor = ice.flavor
 GROUP BY 1;