TYPE=VIEW
query=select `P`.`Id_Pagina` AS `IdPagina`,`P`.`registrant_name` AS `NombreRegistrado`,`P`.`registrant_city` AS `Ciudad`,`P`.`registrant_state` AS `Estado`,`P`.`registrant_country` AS `Pais`,`P`.`domain_name` AS `Dominio`,`P`.`creation_date` AS `FechaCreacionPagina`,`P`.`estatus` AS `EstatusPagina`,`V`.`Estatus` AS `EstatusValidacion`,`R`.`Estatus` AS `EstatusRFC` from ((`trustme`.`Pagina` `P` join `trustme`.`Validacion` `V` on(`P`.`Id_Pagina` = `V`.`Id_Pagina`)) join `trustme`.`RFC` `R` on(`P`.`Id_Usuario` = `R`.`Id_Usuario`))
md5=eee0daf82726451885e1effea43a6d4f
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=0001698394642763426
create-version=2
source=SELECT\n	 P.Id_Pagina AS IdPagina,\n    P.registrant_name AS NombreRegistrado,\n    P.registrant_city AS Ciudad,\n    P.registrant_state AS Estado,\n    P.registrant_country AS Pais,\n    P.domain_name AS Dominio,\n    P.creation_date AS FechaCreacionPagina,\n    P.Estatus AS EstatusPagina,\n    V.estatus AS EstatusValidacion,\n    R.estatus AS EstatusRFC\nFROM\n    Pagina AS P\n    INNER JOIN Validacion AS V ON P.Id_Pagina = V.Id_Pagina\n    INNER JOIN RFC AS R ON P.Id_Usuario = R.Id_Usuario
client_cs_name=utf8mb4
connection_cl_name=utf8mb4_general_ci
view_body_utf8=select `P`.`Id_Pagina` AS `IdPagina`,`P`.`registrant_name` AS `NombreRegistrado`,`P`.`registrant_city` AS `Ciudad`,`P`.`registrant_state` AS `Estado`,`P`.`registrant_country` AS `Pais`,`P`.`domain_name` AS `Dominio`,`P`.`creation_date` AS `FechaCreacionPagina`,`P`.`estatus` AS `EstatusPagina`,`V`.`Estatus` AS `EstatusValidacion`,`R`.`Estatus` AS `EstatusRFC` from ((`trustme`.`Pagina` `P` join `trustme`.`Validacion` `V` on(`P`.`Id_Pagina` = `V`.`Id_Pagina`)) join `trustme`.`RFC` `R` on(`P`.`Id_Usuario` = `R`.`Id_Usuario`))
mariadb-version=110102
