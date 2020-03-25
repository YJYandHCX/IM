#!/usr/bin/env python
# coding: utf-8

# In[1]:


from conf import *
import socket
import time


# In[9]:


import threading


# In[2]:


This_socket = socket.socket(family = socket.AF_INET,type = socket.SOCK_DGRAM)


# In[3]:


This_socket.settimeout(2)


# In[4]:


own_id = ""


# In[5]:


while True:
    print("Log in or Create a count")
    m = input()
    if (m == 'Log in'):
        break
    if (m == 'Create a count'):
        This_socket.sendto(str.encode(code["create_count"]),server_Address)
        try:
            print("I am OK")
            t = This_socket.recvfrom(buffersize)
            #print("I am fine")
            #print(t)
            id_and_password = t[0]
            id_and_password = id_and_password.decode()
            #t = t.decode()
            
            #print(t)
            s = id_and_password.split(" ")
            print("your id is ",s[0])
            print("your password is ",s[1])
            continue
        except:
            print("Timeout,try again !")
            continue


# In[6]:


while True:
    #print("Please Log in:")
    print("Plaase Enter Your ID:")
    s = input()
    own_id = s
    print("Please Enter Your Password")
    p = input()
    
    id_and_password = str.encode("1 "+s+" "+p)
    print(id_and_password)
    This_socket.sendto(id_and_password,server_Address)
    try:
        t = This_socket.recvfrom(buffersize)
        print(t)
        if t[0] == b'200':
            
            print("Successfully log in !")
            break
        else:
            print("Your password is wrong ! Try again !")
    except:
        print("Timeout! Try again")
        s = ""
        p = ""
        continue
print("OKKKKKK")


# In[11]:


def recv_ack():
    print("I am recving!")
    while(True):
        try:
            reply = This_socket.recvfrom(buffersize)
            reply = reply[0].decode()
            #if reply[0] != b'300':
            print(reply)
            continue
        except:
            #print("Send Fail")
            continue


# In[14]:


t1 = threading.Thread(target = recv_ack,args = ())
t1.start()

# In[ ]:


while True:
    print("Please put target user's id:")
    target = input()
    
    print("Please input your message:")
    m = input()
    
    whole_m = code["send"] + " " + target + " "+ m + " " + own_id
    whole_m = str.encode(whole_m)
    print(whole_m)
    This_socket.sendto(whole_m,server_Address)
    #print(whole_m)
    try:
        t = This_socket.recvfrom(buffersize)
        
        if t[0] != b'300':
            print("target user is not online")
            continue
        else:
            continue
    except:
        print("Send Fail!")
        continue
    #    s = ""
    #    p = ""
    #    #continue
    #break


# In[ ]:




