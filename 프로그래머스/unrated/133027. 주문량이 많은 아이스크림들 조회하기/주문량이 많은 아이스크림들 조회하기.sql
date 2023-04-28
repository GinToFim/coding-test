SELECT flavor
  FROM (
      SELECT flavor, SUM(total_order)
        FROM (
            SELECT *
              FROM FIRST_HALF
             UNION
            SELECT *
              FROM JULY) AS union_table
       GROUP BY flavor
       ORDER BY SUM(total_order) DESC
       LIMIT 3
       ) AS super_table;


