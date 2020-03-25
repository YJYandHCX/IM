import redis
from conf import *
class con_redis:
    def __init__(self):
        self.con = redis.Redis(host = redis_host,port = redis_port)
        
    def check_id(self,id):
        if (self.con.exists(id) == 0):
            return False
        else:
            return True
    def get_address(self,id):
        
        t = self.con.get(id)
        if (t == None):
            return None
        else:
            return t.decode()
    def set_key(self,id,address):
        self.con.set(id,address)
        self.con.expire(id,key_outtime)
        return True
