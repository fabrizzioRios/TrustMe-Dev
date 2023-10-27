-- VISTAS
-- --------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------
-- VER INFORMACIÓN PÁGINA DETALLADA
CREATE VIEW Vw_InformacionPagina AS
SELECT
	 P.Id_Pagina AS IdPagina,
    P.registrant_name AS NombreRegistrado,
    P.registrant_city AS Ciudad,
    P.registrant_state AS Estado,
    P.registrant_country AS Pais,
    P.domain_name AS Dominio,
    P.creation_date AS FechaCreacionPagina,
    P.Estatus AS EstatusPagina,
    V.estatus AS EstatusValidacion,
    R.estatus AS EstatusRFC
FROM
    Pagina AS P
    INNER JOIN Validacion AS V ON P.Id_Pagina = V.Id_Pagina
    INNER JOIN RFC AS R ON P.Id_Usuario = R.Id_Usuario;

-- --------------------------------------------------------------------------------------
-- VER LISTA DE PAGINAS
CREATE VIEW Vw_ListaPaginas AS
SELECT
	P.URL AS URL,
	V.Estatus AS Estatus
FROM
	Pagina AS P
	INNER JOIN Validacion AS V ON P.Id_Pagina = V.Id_Pagina;

-- --------------------------------------------------------------------------------------
-- VER COMENTARIOS
CREATE VIEW Vw_Comentarios AS
SELECT
	U.Nombre AS Nombre,
	O.Comentario AS Comentario
FROM
	Usuarios AS U
	INNER JOIN Opinion AS O ON U.Id_Usuario = O.Id_Usuario;

-- --------------------------------------------------------------------------------------
-- SACAR RFC
CREATE VIEW Vw_RFC AS
SELECT
	r.RFC
FROM RFC AS r
WHERE r.Estatus = 'Pendiente'