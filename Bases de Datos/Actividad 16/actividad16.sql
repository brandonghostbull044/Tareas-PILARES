CREATE DATABASE IF NOT EXISTS clinica CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS paciente(
	codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    poblacion VARCHAR(50) NOT NULL DEFAULT "CdMx",
    telefono VARCHAR(20),
    nombre VARCHAR(50) NOT NULL,
    a_paterno VARCHAR(50) NOT NULL,
    a_materno VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE
  );

CREATE TABLE IF NOT EXISTS medico(
	codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  	especialidad VARCHAR(50) DEFAULT "Médico General" NOT NULL, 
  	nombre VARCHAR(50) NOT NULL,
  	a_paterno VARCHAR(50) NOT NULL,
  	a_materno VARCHAR(50) NOT NULL,
  	telefono VARCHAR(20)
  );
  
CREATE TABLE IF NOT EXISTS ingreso(
  	codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  	id_paciente INT UNSIGNED,
  	id_medico INT UNSIGNED,
  	fecha_ingreso DATETIME,
  	num_habitacion INT UNSIGNED,
  	num_cama INT UNSIGNED,
  	FOREIGN KEY (id_paciente) REFERENCES paciente(codigo) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (id_medico) REFERENCES medico(codigo) ON DELETE RESTRICT ON UPDATE RESTRICT
  );
  
INSERT INTO paciente(codigo, poblacion, telefono, nombre, a_paterno, a_materno, fecha_nacimiento) VALUES (1, "cdmx", " ", "juan", "lopez", "perez", "1988-01-02"), (2, "cdmx", "+525578", "sacnite", "perez", "lopez", "1996-12-05");
INSERT INTO medico(especialidad, nombre, a_paterno, a_materno, telefono) VALUES ("endocrinologo", "viviana", "lopez", "lopez", "+525545678921"), ("radiologo", "roberto", "lopez", "perez", "+52456441345");
INSERT INTO ingreso(id_paciente, id_medico, fecha_ingreso, num_habitacion, num_cama) VALUES (1, 1, "2023-06-08 23:58:20", 2, 1);
