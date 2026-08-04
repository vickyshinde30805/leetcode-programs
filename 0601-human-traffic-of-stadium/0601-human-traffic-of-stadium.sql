# Write your MySQL query statement below

SELECT DISTINCT a.*
FROM Stadium a
JOIN Stadium b
JOIN Stadium c
WHERE a.people >= 100
  AND b.people >= 100
  AND c.people >= 100
  AND (
       (a.id = b.id - 1 AND a.id = c.id - 2)
    OR (a.id = b.id + 1 AND a.id = c.id - 1)
    OR (a.id = b.id + 2 AND a.id = c.id + 1)
  )
ORDER BY visit_date;