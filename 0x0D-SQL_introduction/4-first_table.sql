-- creat first table
SET @database_name = 'mysql';
CREATE TABLE IF NOT EXISTS `first_table` (
    `id` INT,
    `name` VARCHAR(256)
) ENGINE=InnoDB;
