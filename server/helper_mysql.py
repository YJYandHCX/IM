import pymysql
from conf import *
class con_mysql:
    def __init__(self):
        self.con = pymysql.connect(user = mysql_usr,password=mysql_password,
                                   database = mysql_database)
        self.cur = self.con.cursor()
    def read(self,name_id):
        check_sql = "SELECT * FROM " + mysql_table + " WHERE id = " + name_id
        t = self.cur.execute(check_sql)
        res = self.cur.fetchall()
        return res
        
    def write(self,name_id,name_password):
        write_sql = "INSERT INTO "+ mysql_table + " SET " + "id = " + name_id +","+ "passwor = " + name_password
        try:
            self.cur.execute(write_sql)
            t = self.cur.fetchall()
            return True
        except:
            return False

