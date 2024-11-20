-- COUNT students in each batch
SELECT batch_id, COUNT(*) AS total_students
FROM students
GROUP BY batch_id;
