-- 코드를 입력하세요
SELECT ins.animal_id, ins.animal_type, ins.name
# SELECT *
  FROM animal_ins AS ins
 INNER JOIN animal_outs AS outs
    ON ins.animal_id = outs.animal_id
 WHERE ins.sex_upon_intake LIKE 'Intact%' 
       AND (outs.sex_upon_outcome LIKE 'Spayed%'
       OR outs.sex_upon_outcome LIKE 'Neutered%')
 ORDER BY 1;