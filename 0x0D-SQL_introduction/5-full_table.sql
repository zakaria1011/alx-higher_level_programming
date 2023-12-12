-- Check if the database name is provided
SET @database_name = 'hbtn_0c_0'; 
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = @database_name
    AND TABLE_NAME = 'first_table';