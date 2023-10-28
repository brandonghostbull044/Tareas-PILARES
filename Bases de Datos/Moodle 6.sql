-- Bases de datos Fin de semana
-- Practica 6
-- Brandon Leon Gonzalez
-- Folio: 337NRA92
-- 14-08-23

CREATE DATABASE IF NOT EXISTS ventas CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS producto(
	  codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	nombre VARCHAR(50) NOT NULL,
  	precio DOUBLE,
  	codigo_fabricante INT
  );

CREATE TABLE IF NOT EXISTS fabricante(
  	codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	nombre VARCHAR(50)
  );

INSERT INTO fabricante(codigo, nombre) VALUES (1, 'Asus'), (2, 'Lenovo'), (3, 'Hewlett-Packard'), (4, 'Samsung'), (5, 'Seagate'), (6, 'Crucial'), (7, 'Gigabyte'), (8, 'Huawei'), (9, 'Xioami');
INSERT INTO  producto(codigo, nombre, precio, codigo_fabricante) VALUES (1, 'Disco duro SATA3 1TB', 86.99, 5), (2, 'Memoria RAM DDR4 8GB', 120, 6), (3, 'Disco SSD 1TB', 15.99, 4), (4, 'GeForce GTX 1050 Ti', 185, 7), (5, 'GeForce GTX 1080 Xtreme', 755, 6), (6, 'Monitor 24 LED Full HD', 202, 1), (7, 'Monitor 27 LED Full HD', 245.99, 1), (8, 'Portátil Yoga 520', 559, 2), (9, 'Portátil Ideapad 320', 444, 2), (10, 'Impresora HP Deskjet 3720', 59.99, 3), (11, 'Impresora HP Laserjet Pro M26nw', 180, 3);

SELECT * FROM producto;
SELECT nombre, precio FROM producto WHERE precio <= 2000;
SELECT * FROM producto WHERE precio != 86.99;
SELECT precio, codigo_fabricante FROM producto WHERE precio > 250;
SELECT nombre, precio, codigo_fabricante FROM producto WHERE precio BETWEEN 300 AND 750;
SELECT nombre FROM producto WHERE codigo_fabricante = 6;
SELECT nombre, precio, codigo_fabricante FROM producto WHERE codigo_fabricante = 1 OR codigo_fabricante = 2;
SELECT nombre, precio, codigo_fabricante FROM producto WHERE codigo_fabricante = 1 AND precio < 210;
SELECT nombre AS 'El más caro' FROM producto WHERE precio = (SELECT MAX(precio) FROM producto);
SELECT nombre AS 'El más barato' FROM producto WHERE precio = (SELECT MIN(precio) FROM producto);
SELECT COUNT(*) FROM producto;
SELECT SUM(precio) AS 'Suma de precios' FROM producto WHERE codigo_fabricante = 3;
SELECT AVG(precio) AS 'Promedio de precios del fabricante Lenovo' FROM producto WHERE codigo_fabricante = 2;
SELECT COUNT(*) FROM producto GROUP BY codigo_fabricante;
SELECT nombre, precio FROM producto ORDER BY precio DESC;
SELECT nombre, precio FROM producto ORDER BY precio ASC;
