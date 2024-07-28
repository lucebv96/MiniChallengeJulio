CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

INSERT INTO Usuarios (nombre) VALUES ('Juan Perez');
INSERT INTO Usuarios (nombre) VALUES ('Lucero Barreto');
INSERT INTO Usuarios (nombre) VALUES ('Ricardo Salinas');

UPDATE Usuarios
SET nombre = 'Satoru Gojo'
WHERE id = 3;

SELECT * FROM Usuarios; --Para ver el cambio

DELETE FROM Usuarios
WHERE id = 6;

SELECT * FROM Usuarios; --Para ver el cambio