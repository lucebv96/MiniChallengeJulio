CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

INSERT INTO Usuarios (nombre) VALUES ('Juan Perez');
INSERT INTO Usuarios (nombre) VALUES ('Lucero Barreto');
INSERT INTO Usuarios (nombre) VALUES ('Ricardo Salinas');

SELECT * FROM Usuarios;
