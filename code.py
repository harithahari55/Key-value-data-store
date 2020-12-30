import threading 
from threading import*
import time
d={} 
def create(key,value,timeout=0):
    if key in d:
        print("Error: This key already exists")
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("Error: Memory limit exceeded!! ")
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
def read(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key")
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                print(stri)
            else:
                print("Error: time-to-live of",key,"has expired")
        else:
            stri=str(key)+":"+str(b[0])
            print(stri)
def delete(key):
    if key not in d:
        print("Error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")
def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("Error: given key does not exist in database. Please enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("Error: time-to-live of",key,"has expired") 
    else:
        if key not in d:
            print("Error: given key does not exist in database. Please enter a valid key") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l

t1=threading.Thread(target=create,args=("a",20,300))
t2=threading.Thread(target=create,args=("b",12,100))
t3=threading.Thread(target=modify,args=("b",5))
t4=threading.Thread(target=read,args=("b"))
t5=threading.Thread(target=delete,args=("b"))
t6=threading.Thread(target=read,args=("b"))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

            























