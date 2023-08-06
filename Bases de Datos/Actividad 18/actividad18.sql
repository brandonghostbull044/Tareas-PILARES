CREATE TABLE IF NOT EXISTS t_sucursal(
  	id_sucursal INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	nombre VARCHAR(25) NOT NULL,
  	direccion VARCHAR(50)
  );
  
CREATE TABLE IF NOT EXISTS t_proveedor(
  	id_proveedor INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	nombre VARCHAR(25) NOT NULL,
  	apellido VARCHAR(25) NOT NULL,
  	direccion VARCHAR(50)
  );

CREATE TABLE IF NOT EXISTS t_clientes(
  	id_cliente INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	nombre VARCHAR(25) NOT NULL,
  	apellido VARCHAR(25) NOT NULL,
  	edad INT UNSIGNED,
  	sexo ENUM('F', 'M')
  );

CREATE TABLE IF NOT EXISTS t_vendedor(
  	id_vendedor INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	id_sucursal INT UNSIGNED NOT NULL,
  	nombre VARCHAR(25) NOT NULL,
  	apellido VARCHAR(25) NOT NULL,
  	telefono VARCHAR(25) NOT NULL,
  	FOREIGN KEY (id_sucursal) REFERENCES t_sucursal(id_sucursal) ON DELETE CASCADE ON UPDATE CASCADE
  );
 
CREATE TABLE IF NOT EXISTS t_productos(
  	id_producto INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	id_proveedor INT UNSIGNED NOT NULL,
  	modelo VARCHAR(30) NOT NULL,
  	marca VARCHAR(25) NOT NULL,
  	precio INT UNSIGNED NOT NULL,
  	FOREIGN KEY (id_proveedor) REFERENCES t_proveedor(id_proveedor) ON DELETE CASCADE ON UPDATE CASCADE
  );
  
CREATE TABLE IF NOT EXISTS t_ventas(
  	id_venta INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	id_cliente INT UNSIGNED NOT NULL,
  	id_producto INT UNSIGNED NOT NULL,
  	id_vendedor INT UNSIGNED NOT NULL,
  	fecha DATETIME DEFAULT current_timestamp,
  	FOREIGN KEY (id_cliente) REFERENCES t_clientes(id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (id_producto) REFERENCES t_productos(id_producto) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (id_vendedor) REFERENCES t_vendedor(id_vendedor) ON DELETE CASCADE ON UPDATE CASCADE
  );
  
CREATE TABLE IF NOT EXISTS registro_venta(
  	id_registro INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
  	id_venta INT UNSIGNED NOT NULL,
  	id_producto INT UNSIGNED NOT NULL,
  	FOREIGN KEY (id_venta) REFERENCES t_ventas(id_venta) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (id_producto) REFERENCES t_productos(id_producto) ON DELETE CASCADE ON UPDATE CASCADE
  );
