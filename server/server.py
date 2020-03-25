#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket
from helper_mysql import con_mysql
from conf import *
import random
from helper_redis import con_redis


# In[2]:


This_socket = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)
This_socket.bind((local_ip,local_port))
This_mysql = con_mysql()
This_redis = con_redis()


# In[3]:


def create_count(sock,sql,address):
    while True:
        new_id = random.randint(1,100000)
        new_pass = random.randint(1,1000)
        
        if sql.write(str(new_id),str(new_pass)):
            sock.sendto(str.encode(str(new_id) + " " + str(new_pass)),address)
            return True


# In[4]:


def log_in(sock,sql,red,id_and_password,address):
    name_id,password = id_and_password[0],id_and_password[1]
    
    p = sql.read(name_id)
    print(p)
    if (len(p)==0):
        sock.sendto(str.encode(reply_code["log_bad"]),address)
        return False
    print(p[0][1])
    print(type(p[0][1]))
    if (password == str(p[0][1])):
        sock.sendto(str.encode(reply_code["log_fine"]),address)
        #return True
        str_address = str(address[0]) + " " + str(address[1])
        red.set_key(name_id,str_address)
        #print(red.get_address(name_id))
        return True
    else:
        sock.sendto(str.encode(reply_code["log_bad"]),address)
    
    #print(name_id,password)
    return False


# In[32]:


def recive_message(sock,red,whole_m,address):
    target,m,sender = whole_m[0],whole_m[1],whole_m[2]
    
    print(target)
    print(m)
    print(sender)
    
    if (red.check_id(target) == False):
        sock.sendto(str.encode(reply_code["send_no_man"]),address)
        return 
    t_ad = red.get_address(target)
    print(t_ad)
    #t_ad = t_ad.decode()
    ip,port = t_ad.split(" ")
    print(ip,port)
    target_ad = (ip,int(port))
    
    s = sender + "tell you :    " + m
    
    sock.sendto(str.encode(s),target_ad)
    return 
    #sock.send_to(str.encode())


# In[33]:


while(True):
    Message_Pair = This_socket.recvfrom(buffersize)
    Message = Message_Pair[0]
    address = Message_Pair[1]
    
    #print(type(address[0]))
    #print(type(address[1]))
    
    Message = Message.decode()
    al = Message.split(" ")
    #print(Message)
    if al[0] == code["create_count"]:
        print("OK")
        create_count(This_socket,This_mysql,address)
    if al[0] == code["log_in"]:
        log_in(This_socket,This_mysql,This_redis,al[1:],address)
    if al[0] == code["send"]:
        recive_message(This_socket,This_redis,al[1:],address)
        break


# In[ ]:




