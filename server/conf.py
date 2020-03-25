local_ip = "127.0.0.1"

local_port = 20001

buffersize = 1024

code = {"log_in":"1","send":"2","create_count":"3"}
code_server = {"1":"log_in","2":"send","3":"create_count"}
reply_code = {"log_bad":"201","log_fine":"200","send_bad":"101",
		"send_no_man":"301","send_fine":"300"}

mysql_usr = "yanjianyu"
mysql_password = "666666"
mysql_database = "IM"
mysql_table = "user"

redis_host = "127.0.0.1"
redis_port = 6379
key_outtime = 360
