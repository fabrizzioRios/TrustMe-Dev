DELIMITER //

-- INSERTAR UN NUEVO USUARIO
CREATE PROCEDURE InsertarUsuario(IN p_Nombre VARCHAR(150), IN p_Correo VARCHAR(50), IN p_Contraseña VARCHAR(30))
BEGIN
    INSERT INTO Usuarios (Nombre, Correo, Contraseña)
    VALUES (p_Nombre, p_Correo, p_Contraseña);
END //

-- INSERTAR COMENTARIO
CREATE PROCEDURE InsertarOpinion(IN p_Id_usuario INT, IN p_Id_Pagina INT, IN p_Comentario VARCHAR(300))
BEGIN
    INSERT INTO Opinion (Id_Usuario, Id_Pagina, Comentario)
    VALUES (p_Id_usuario, p_Id_Pagina, p_Comentario);
END //

-- INSERTAR RFC
CREATE PROCEDURE InsertarRFC(IN p_Id_usuario INT, IN p_RFC VARCHAR(50))
BEGIN
    INSERT INTO RFC (Id_Usuario, RFC, Estatus)
    VALUES (p_Id_usuario, p_RFC, 'Pendiente');
END //

-- INSERTAR PAGINA
CREATE PROCEDURE InsertarPagina(
    IN p_Id_Usuario INT, IN p_URL VARCHAR(100), IN p_name_servers VARCHAR(100), IN p_registrar VARCHAR(100), IN p_registrant_name VARCHAR(100),
    IN p_registrant_city VARCHAR(80), IN p_registrant_state VARCHAR(80), IN p_registrant_country VARCHAR(80), IN p_admin VARCHAR(100), IN p_admin_city VARCHAR(80),
    IN p_admin_country VARCHAR(80), IN p_admin_state VARCHAR(80), IN p_tech_name VARCHAR(80), IN p_tech_city VARCHAR(80), IN p_tech_state VARCHAR(80),
    IN p_tech_country VARCHAR(80), IN p_biling_name VARCHAR(80), IN p_biling_city VARCHAR(80), IN p_biling_state VARCHAR(80), IN p_domain_name VARCHAR(100),
    IN p_creation_date DATE, IN p_update_date DATE, IN p_expiration_date DATE
)
BEGIN
    INSERT INTO Pagina (
        Id_Usuario, URL, name_servers, registrar, registrant_name,
        registrant_city, registrant_state, registrant_country, admin, admin_city,
        admin_country, admin_state, tech_name, tech_city, tech_state,
        tech_country, biling_name, biling_city, biling_state, domain_name,
        creation_date, update_date, expiration_date
    )
    VALUES (
        p_Id_Usuario, p_URL, p_name_servers, p_registrar, p_registrant_name,
        p_registrant_city, p_registrant_state, p_registrant_country, p_admin, p_admin_city,
        p_admin_country, p_admin_state, p_tech_name, p_tech_city, p_tech_state,
        p_tech_country, p_biling_name, p_biling_city, p_biling_state, p_domain_name,
        p_creation_date, p_update_date, p_expiration_date
    );
END //

-- INSERTAR VALIDACIÓN
CREATE PROCEDURE InsertarValidacion(IN p_Id_Pagina INT, IN p_Estatus VARCHAR(100))
BEGIN
    INSERT INTO Validacion (Id_Pagina, Estatus)
    VALUES (p_Id_Pagina, p_Estatus);
END //

-- ACTUALIZAR ESTATUS RFC
CREATE PROCEDURE ActualizarEstatusRFC(IN p_Id_Pagina INT, IN p_Estatus VARCHAR(100))
BEGIN
    UPDATE RFC
    SET Estatus = p_Estatus
    WHERE Id_Usuario = p_Id_Pagina;
END //

-- ACTUALIZAR ESTATUS VALIDACIÓN
CREATE PROCEDURE ActualizarEstatusValidacion(IN p_Id_Usuario INT, IN p_Estatus VARCHAR(100))
BEGIN
    UPDATE Validacion
    SET Estatus = p_Estatus
    WHERE Id_Pagina = p_Id_Usuario;
END //

-- VER PÁGINA DETALLADA CON UN ID DE PÁGINA
CREATE PROCEDURE VerInfoPagina(IN p_Id_Pagina INT)
BEGIN
    SELECT * FROM Vw_InformacionPagina
    WHERE IdPagina = p_Id_Pagina;
END //
DELIMITER ;