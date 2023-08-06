SELECT nombre, direccion FROM t_sucursal WHERE id_sucursal=23562;
SELECT id_vendedor, telefono, id_sucursal FROM t_vendedor WHERE nombre="Martha" AND apellido="Mota";
SELECT * FROM t_productos WHERE precio<10000;
SELECT * FROM t_productos WHERE precio>=1000 AND precio<=5000;
SELECT * FROM t_ventas WHERE fecha between "2015-02-01" AND "2015-03-31";
SELECT id_vendedor, id_cliente, fecha FROM t_ventas WHERE id_vendedor=67841 OR id_vendedor=67847;
SELECT * FROM t_sucursal WHERE NOT id_sucursal+23562;
SELECT count(id_vendedor) AS "Numero de vendedores", id_sucursal AS "ID de sucursal" FROM t_vendedor group by id_sucursal order by desc;
SELECT id_proveedor, count(id_producto), sum(precio), avg(precio), min(precio), max(precio) FROM t_productos group by id_proveedor having min(precio) >=0 AND min(precio) <=1500;