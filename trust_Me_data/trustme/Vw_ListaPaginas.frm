TYPE=VIEW
query=select `P`.`URL` AS `URL`,`V`.`Estatus` AS `Estatus` from (`trustme`.`Pagina` `P` join `trustme`.`Validacion` `V` on(`P`.`Id_Pagina` = `V`.`Id_Pagina`))
md5=90f4134430ab5883baa88255c313f363
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=0001698394642847260
create-version=2
source=SELECT\n	P.URL AS URL,\n	V.Estatus AS Estatus\nFROM\n	Pagina AS P\n	INNER JOIN Validacion AS V ON P.Id_Pagina = V.Id_Pagina
client_cs_name=utf8mb4
connection_cl_name=utf8mb4_general_ci
view_body_utf8=select `P`.`URL` AS `URL`,`V`.`Estatus` AS `Estatus` from (`trustme`.`Pagina` `P` join `trustme`.`Validacion` `V` on(`P`.`Id_Pagina` = `V`.`Id_Pagina`))
mariadb-version=110102
