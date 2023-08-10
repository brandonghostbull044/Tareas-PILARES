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
