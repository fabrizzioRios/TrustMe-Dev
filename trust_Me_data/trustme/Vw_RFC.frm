TYPE=VIEW
query=select `r`.`RFC` AS `RFC` from `trustme`.`RFC` `r` where `r`.`Estatus` = \'Pendiente\'
md5=256ed294a969b321fc7a7dcd91c0beb7
updatable=1
algorithm=0
definer_user=root
definer_host=%
suid=2
with_check_option=0
timestamp=0001698394645231720
create-version=2
source=SELECT\n	r.RFC\nFROM RFC AS r\nWHERE r.Estatus = \'Pendiente\'
client_cs_name=utf8mb4
connection_cl_name=utf8mb4_general_ci
view_body_utf8=select `r`.`RFC` AS `RFC` from `trustme`.`RFC` `r` where `r`.`Estatus` = \'Pendiente\'
mariadb-version=110102
