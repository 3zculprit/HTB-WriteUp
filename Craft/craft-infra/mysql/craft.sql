CREATE DATABASE `craft`; 

/* create the craft.brew schema */
CREATE TABLE `craft`.`brew` (
`id` INT NOT NULL AUTO_INCREMENT,
`brewer` VARCHAR(45) NULL,
`name` VARCHAR(45) NULL,
`style` VARCHAR(45) NULL,
`abv` DECIMAL(3,3) NULL,
PRIMARY KEY (`id`));

/* create the craft.user schema */
CREATE TABLE `craft`.`user` (
`id` INT NOT NULL AUTO_INCREMENT,
`username` VARCHAR(45) NULL,
`password` VARCHAR(100) NULL,
PRIMARY KEY (`id`));