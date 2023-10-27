CREATE DATABASE trustme;

USE trustme;

CREATE TABLE Usuarios (
  Id_Usuario INT AUTO_INCREMENT PRIMARY KEY,
  Nombre VARCHAR(150),
  Correo VARCHAR(50),
  Contraseña VARCHAR(30)
);

CREATE TABLE Pagina (
  Id_Pagina INT AUTO_INCREMENT PRIMARY KEY,
  Id_Usuario INT,
  URL VARCHAR(100),
  name_servers VARCHAR(100),
  registrar VARCHAR(100),
  registrant_name VARCHAR(100),
  registrant_city VARCHAR(80),
  registrant_state VARCHAR(80),
  registrant_country VARCHAR(80),
  admin VARCHAR(100),
  admin_city VARCHAR(80),
  admin_country VARCHAR(80),
  admin_state VARCHAR(80),
  tech_name VARCHAR(80),
  tech_city VARCHAR(80),
  tech_state VARCHAR(80),
  tech_country VARCHAR(80),
  biling_name VARCHAR(80),
  biling_city VARCHAR(80),
  biling_state VARCHAR(80),
  domain_name VARCHAR(100),
  creation_date DATE,
  update_date DATE,
  expiration_date DATE,
  estatus VARCHAR(20),
  FOREIGN KEY (Id_Usuario) REFERENCES Usuarios(Id_Usuario)
);

CREATE TABLE Validacion (
  Id_Pagina INT PRIMARY KEY,
  Estatus VARCHAR(100),
  FOREIGN KEY (Id_Pagina) REFERENCES Pagina(Id_Pagina)
);

CREATE TABLE Opinion (
  Id_Usuario INT PRIMARY KEY,
  Id_Pagina INT,
  Comentario VARCHAR(300),
  FOREIGN KEY (Id_Usuario) REFERENCES Usuarios(Id_Usuario),
  FOREIGN KEY (Id_Pagina) REFERENCES Pagina(Id_Pagina)
);

CREATE TABLE RFC (
  Id_Usuario INT PRIMARY KEY,
  RFC VARCHAR(50),
  Estatus VARCHAR(100),
  FOREIGN KEY (Id_Usuario) REFERENCES Usuarios(Id_Usuario)
);