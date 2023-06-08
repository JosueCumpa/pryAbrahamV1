CREATE TABLE IF NOT EXISTS ROL(
    id SERIAL PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    estado CHAR(1) NOT NULL
);

INSERT INTO ROL(nombre, estado) VALUES ('Administrador', 'A');
INSERT INTO ROL(nombre, estado) VALUES ('Ventas', 'A');
INSERT INTO ROL(nombre, estado) VALUES ('Logistica', 'A');

CREATE TABLE IF NOT EXISTS USUARIO(
    id SERIAL PRIMARY KEY,
    idrol int DEFAULT NULL,
    foreign key(idrol) references rol(id),
    nombre varchar(100) DEFAULT NULL,
    usuario VARCHAR(100),
    clave text NOT NULL,
    correo varchar(100) DEFAULT NULL,
    estado CHAR(1) NOT NULL
);

INSERT INTO USUARIO(idrol, nombre, usuario, clave, correo, estado) VALUES(
    1,
    'Usuario de prueba',
    'Admin123',
    'pbkdf2:sha256:600000$M09Hs8m0HnOgjHEN$9e09f13c3f67a284b1457535ec98155af7591427150c9cc069ef1e25bd728398',
    'admin123@gmail.com',
    'A'
);