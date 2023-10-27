TYPE=VIEW
query=select `U`.`Nombre` AS `Nombre`,`O`.`Comentario` AS `Comentario` from (`trustme`.`Usuarios` `U` join `trustme`.`Opinion` `O` on(`U`.`Id_Usuario` = `O`.`Id_Usuario`))
md5=f363e588ad645abb7dfc3d5ff52a1764
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=0001698394645118229
create-version=2
source=SELECT\n	U.Nombre AS Nombre,\n	O.Comentario AS Comentario\nFROM\n	Usuarios AS U\n	INNER JOIN Opinion AS O ON U.Id_Usuario = O.Id_Usuario
client_cs_name=utf8mb4
connection_cl_name=utf8mb4_general_ci
view_body_utf8=select `U`.`Nombre` AS `Nombre`,`O`.`Comentario` AS `Comentario` from (`trustme`.`Usuarios` `U` join `trustme`.`Opinion` `O` on(`U`.`Id_Usuario` = `O`.`Id_Usuario`))
mariadb-version=110102
