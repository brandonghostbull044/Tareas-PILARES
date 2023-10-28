CREATE DATABASE IF NOT EXISTS proveedores CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS proveedor(
  codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(25) NOT NULL,
  direccion VARCHAR(50) NOT NULL,
  ciudad VARCHAR(25) NOT NULL,
  provincia VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS categoria(
codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
nombre VARCHAR(25)
);

CREATE TABLE IF NOT EXISTS pieza(
  codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  codigo_categoria INT UNSIGNED NOT NULL,
  nombre VARCHAR(25) NOT NULL,
  color VARCHAR(15),
  precio INT NOT NULL,
  categoria VARCHAR(20) NOT NULL,
  FOREIGN KEY (codigo_categoria) REFERENCES categoria(codigo) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS registro(
  codigo_proveedor INT UNSIGNED NOT NULL,
  codigo_pieza INT UNSIGNED NOT NULL,
  cantidad INT NOT NULL,
  fecha DATETIME,
  FOREIGN KEY (codigo_proveedor) REFERENCES proveedor(codigo) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (codigo_pieza) REFERENCES pieza(codigo) ON DELETE CASCADE ON UPDATE CASCADE
);