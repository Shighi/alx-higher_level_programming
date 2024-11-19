-- Convert the database hbtn_0c_0 to UTF-8 encoding (utf8mb4, collate utf8mb4_unicode_ci)
-- Convert the table first_table and the field name in first_table to UTF-8 as well
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
