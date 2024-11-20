-- JOIN students and batches to get student names and their batch names
SELECT students.name AS student_name, batches.name AS batch_name
FROM students
JOIN batches ON students.batch_id = batches.id;
