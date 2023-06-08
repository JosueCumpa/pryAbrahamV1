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
    'sha256$JZlcJysAqPkmkFFk$a2a3ec1b1b7a348e91f5ef853c04bae1264b37879d746739a1152c0b36dc683c',
    'admin123@gmail.com',
    'A'
);


CREATE OR REPLACE FUNCTION fn_login
(p_usuario VARCHAR(20)
)
RETURNS TABLE(
	id integer, 
    idrol integer, 
    nombre VARCHAR(100), 
    usuario VARCHAR(100),
	clave text, 
    correo VARCHAR(100), 
    estado CHAR(1), 
    rol VARCHAR(50))
LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
	RETURN QUERY
		SELECT 
			u.*, r.nombre as rol
		FROM usuario u
			INNER JOIN rol r on r.id=u.idrol
		WHERE u.usuario=p_usuario;
END
$BODY$;