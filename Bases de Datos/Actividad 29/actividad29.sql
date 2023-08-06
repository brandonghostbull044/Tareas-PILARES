CREATE TABLE IF NOT EXISTS t_sucursal(
  	id_sucursal INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  	nombre VARCHAR(25) NOT NULL,
  	direccion VARCHAR(50)
  );
  
CREATE TABLE IF NOT EXISTS t_proveedores(
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
  	FOREIGN KEY (id_proveedor) REFERENCES t_proveedores(id_proveedor) ON DELETE CASCADE ON UPDATE CASCADE
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
  	id_venta INT UNSIGNED NOT NULL,
  	id_producto INT UNSIGNED NOT NULL,
  	FOREIGN KEY (id_venta) REFERENCES t_ventas(id_venta) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (id_producto) REFERENCES t_productos(id_producto) ON DELETE CASCADE ON UPDATE CASCADE
  );
  
  INSERT INTO t_clientes (id_cliente, nombre, apellido, edad, sexo) VALUES
    (58390, 'Octavio', 'Ruiz', 27, 'M'),
    (58391, 'Diego', 'Fernandez', 32, 'M'),
    (58392, 'Omar', 'Garcia', 24, 'M'),
    (58393, 'Maria', 'Luna', 26, 'F'),
    (58394, 'Silvia', 'Zuñiga', 35, 'F'),
    (58395, 'Pedro', 'Perez', 22, 'M'),
    (58396, 'Sonia', 'Cardona', 29, 'F'),
    (58397, 'Hugo', 'Mendez', 30, 'M'),
    (58398, 'Sofia', 'Parriego', 26, 'F'),
    (58399, 'Sandra', 'Rivas', 31, 'F');

INSERT INTO t_proveedores (id_proveedor, nombre, apellido, direccion) VALUES
    (45630, 'Manuel', 'Hernández', 'calle coneja #432'),
    (45631, 'Jesus', 'Martinez', 'calle flores #543'),
    (45632, 'Fernando', 'Lopez', 'calle trejo #654'),
    (45633, 'Ivan', 'Sanchez', 'calle nuvo #765'),
    (45634, 'Rosa', 'Rodriguez', 'calle trolo #876'),
    (45635, 'Merida', 'Rito', 'calle falco #987'),
    (45636, 'Leslie', 'Duran', 'calle mediterraneo #102'),
    (45637, 'Ulises', 'Mendoza', 'calle mar #234'),
    (45638, 'Andrea', 'Guzman', 'calle yate #345'),
    (45639, 'Luz', 'Velazquez', 'calle siempre viva #678'),
	(45640, 'Rey', 'Treviño', 'calle golondrinas #111');
    
INSERT INTO t_productos (id_producto, modelo, marca, precio, id_proveedor) VALUES
    (12340, 'Camara', 'Sani', 5350, 45638),
    (12341, 'Pantalla', 'Samsoni', 7820, 45632),
    (12342, 'Audifonos', 'Tronic', 1456, 45633),
    (12343, 'DVD', 'Yashi', 1000, 45631),
    (12344, 'Bluray', 'Moshi', 2000, 45636),
    (12345, 'Celular', 'Moma', 5670, 45639),
    (12346, 'Mouse', 'Razor', 560, 45630),
    (12347, 'Laptop', 'vopoi', 17500, 45635),
    (12348, 'Teclado', 'Razor', 1020, 45634),
    (12349, 'Videogame', 'Sanor', 4567, 45637),
    (12350, 'GT 720', 'Razor', 1000, 45630),
    (12351, 'Laptop G3', 'Dell', 13000, 45638),
    (12352, 'DDR4 4GB', 'Kingston', 300, 45638);

INSERT INTO t_sucursal (id_sucursal, nombre, direccion) VALUES
    (23560, 'Salmons tropia', 'calle tropia #234'),
    (23561, 'Salmons naranjo', 'calle naranjo #345'),
    (23562, 'Salmons artemisa', 'calle artemisa #456'),
    (23563, 'Salmons pichacho', 'calle picacho #567'),
    (23564, 'Salmons fisica', 'calle fisica #678');

INSERT INTO t_vendedor (id_vendedor, nombre, apellido, id_sucursal, telefono) VALUES
    (67840, 'Alberto', 'Ascencio', 23562, 84592730),
    (67841, 'Paulina', 'Rivera', 23562, 89452356),
    (67842, 'Jose', 'Bueno', 23564, 98653265),
    (67843, 'Eduardo', 'Telones', 23564, 98342761),
    (67844, 'Martha', 'Mota', 23561, 14568723),
    (67845, 'Alonso', 'Garcia', 23561, 14789534),
    (67846, 'Diego', 'Trenes', 23563, 34679512),
    (67847, 'Monica', 'Diaz', 23563, 34785612),
    (67848, 'Maricela', 'Hernandez', 23560, 78341267),
    (67849, 'Diana', 'Rico', 23560, 78563453),
    (67850, 'Joel', 'Perez', 23560, 78563453);

INSERT INTO t_ventas (id_venta, id_cliente, id_vendedor, fecha) VALUES
    (1    ,    58391    ,    67840    ,    '2015-02-06')    ,
    (2    ,    58397    ,    67845    ,    '2015-02-06')    ,
    (3    ,    58393    ,    67846    ,    '2015-02-06')    ,
    (4    ,    58390    ,    67843    ,    '2015-02-06')    ,
    (5    ,    58392    ,    67849    ,    '2015-02-06')    ,
    (6    ,    58395    ,    67842    ,    '2015-02-06')    ,
    (7    ,    58399    ,    67848    ,    '2015-02-06')    ,
    (8    ,    58394    ,    67844    ,    '2015-02-06')    ,
(9    ,    58398    ,    67847    ,    '2015-02-06')    ,
(10    ,    58396    ,    67841    ,    '2015-02-06')    ,
(11    ,    58391    ,    67840    ,    '2015-03-06')    ,
(12    ,    58397    ,    67845    ,    '2015-03-06')    ,
(13    ,    58393    ,    67846    ,    '2015-03-06')    ,
(14    ,    58390    ,    67843    ,    '2015-03-06')    ,
(15    ,    58392    ,    67849    ,    '2015-03-06')    ,
(16    ,    58395    ,    67842    ,    '2015-03-06')    ,
(17    ,    58399    ,    67848    ,    '2015-03-06')    ,
(18    ,    58394    ,    67844    ,    '2015-03-06')    ,
(19    ,    58398    ,    67847    ,    '2015-03-06')    ,
(20    ,    58396    ,    67841    ,    '2015-03-06')    ,
(21    ,    58391    ,    67840    ,    '2015-04-06')    ,
(22    ,    58397    ,    67845    ,    '2015-04-06')    ,
(23    ,    58393    ,    67846    ,    '2015-04-06')    ,
(24    ,    58390    ,    67843    ,    '2015-04-06')    ,
(25    ,    58392    ,    67849    ,    '2015-04-06')    ,
(26    ,    58395    ,    67842    ,    '2015-04-06')    ,
(27    ,    58399    ,    67848    ,    '2015-04-06')    ,
(28    ,    58394    ,    67844    ,    '2015-04-06')    ,
(29    ,    58398    ,    67847    ,    '2015-04-06')    ,
(30    ,    58396    ,    67841    ,    '2015-04-06')    ,
(31    ,    58391    ,    67840    ,    '2015-05-06')    ,
(32    ,    58397    ,    67845    ,    '2015-05-06')    ,
(33    ,    58393    ,    67846    ,    '2015-05-06')    ,
(34    ,    58390    ,    67843    ,    '2015-05-06')    ,
(35    ,    58392    ,    67849    ,    '2015-05-06')    ,
(36    ,    58395    ,    67842    ,    '2015-05-06')    ,
(37    ,    58399    ,    67848    ,    '2015-05-06')    ,
(38    ,    58394    ,    67844    ,    '2015-05-06')    ,
(39    ,    58398    ,    67847    ,    '2015-05-06')    ,
(40    ,    58396    ,    67841    ,    '2015-05-06')    ,
(41    ,    58391    ,    67840    ,    '2015-07-06')    ,
(42    ,    58397    ,    67845    ,    '2015-07-06')    ,
(43    ,    58393    ,    67846    ,    '2015-07-06')    ,
(44    ,    58390    ,    67843    ,    '2015-07-06')    ,
(45    ,    58392    ,    67849    ,    '2015-07-06')    ,
(46    ,    58395    ,    67842    ,    '2015-07-06')    ,
(47    ,    58399    ,    67848    ,    '2015-07-06')    ,
(48    ,    58394    ,    67844    ,    '2015-07-06')    ,
(49    ,    58398    ,    67847    ,    '2015-07-06')    ,
(50    ,    58396    ,    67841    ,    '2015-07-06')    
;

INSERT INTO registro_venta (id_venta, id_producto) VALUES
(1    ,    12342    ),
(2    ,    12344    ),
(3    ,    12340    ),
(4    ,    12345    ),
(5    ,    12343    ),
(6    ,    12347    ),
(7    ,    12346    ),
(8    ,    12341    ),
(9    ,    12348    ),
(10    ,    12349    ),
(11    ,    12344    ),
(12    ,    12340    ),
(13    ,    12345    ),
(14    ,    12343    ),
(15    ,    12347    ),
(16    ,    12346    ),
(17    ,    12341    ),
(18    ,    12348    ),
(19    ,    12349    ),
(20    ,    12342    ),
(21    ,    12340    ),
(22    ,    12345    ),
(23    ,    12343    ),
(24    ,    12347    ),
(25    ,    12346    ),
(26    ,    12341    ),
(27    ,    12348    ),
(28    ,    12349    ),
(29    ,    12342    ),
(30    ,    12344    ),
(31    ,    12345    ),
(32    ,    12343    ),
(33    ,    12347    ),
(34    ,    12346    ),
(35    ,    12341    ),
(36    ,    12348    ),
(37    ,    12349    ),
(38    ,    12342    ),
(39    ,    12344    ),
(40    ,    12340    ),
(41    ,    12345    ),
(42    ,    12343    ),
(43    ,    12347    ),
(44    ,    12341    ),
(45    ,    12348    ),
(46    ,    12349    ),
(47    ,    12342    ),
(48    ,    12344    ),
(49    ,    12340    ),
(50    ,    12345    );

SELECT * FROM t_clientes;
SELECT nombre, apellido FROM t_proveedores;
SELECT modelo, marca, precio FROM t_productos;
SELECT nombre FROM t_sucursal;
SELECT apellido, telefono, id_sucursal FROM t_sucursal;
SELECT id_venta, fecha FROM t_ventas;
SELECT count(*) FROM t_clientes;
SELECT max(precio) FROM t_productos;
SELECT min(precio) FROM t_productos;
SELECT avg(edad) FROM t_clientes;
SELECT sum(precio) FROM *;
SELECT count(*), avg(precio), sum(precio), min(precio), max(precio), FROM t_proveedores;