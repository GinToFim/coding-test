-- 코드를 작성해주세요
WITH RECURSIVE ecoli_generation
AS (
    SELECT 
        id,
        parent_id,
        1 AS generation
      FROM ecoli_data
     WHERE parent_id IS NULL
    
    UNION ALL
    
    SELECT 
        e.id,
        e.parent_id,
        eg.generation + 1
      FROM ecoli_data AS e, ecoli_generation AS eg
     WHERE e.parent_id = eg.id
)
SELECT 
    id
  FROM ecoli_generation
 WHERE generation = 3
 ORDER BY 1;
