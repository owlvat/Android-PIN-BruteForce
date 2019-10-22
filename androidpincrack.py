import os
import hashlib
import sqlite3
import struct
import binascii

#I am reading from a file called settings.db and the salt for the password is stored in this database.
sqlite_file = "settings.db"
table_name = "secure"
id_column = "_id"
name = "name"
value = "value"
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute("SELECT `value` FROM `secure` WHERE `name`='lockscreen.password_salt'")     
name_exists = c.fetchone()
if name_exists:
    salt=(int(name_exists[0]))
    hexsalt=binascii.hexlify((struct.pack('>q',(int(salt))))) 
else:
    print("does not exist")
conn.close()

#In password.key the md5 and sha1 hashes of the password are stored in one long string
file = open("password.key", "rb")
sha1=(file.read(40))
md5=(file.read(32))

passwordhash = md5.decode().lower()
print("MD5 hash read in from password.key: " + passwordhash)
print("Lockscreen Salt read from settings.db: " + str(salt))

#In device_policies.xml it shows the length of the password so the program will only try that length of password
xml_file = open("device_policies.xml", "r")
xml_file = (xml_file.read())
codelength = int(xml_file.split('length="')[1].split('"')[0])

#This means that it will only try password of that length and no others
for i in range(10**(codelength)):
       if len(str(i)) < (codelength):
           #This fills the start of the code with zeros 
           code = (str(i).zfill(codelength))
       else:
            code = str(i)
       passwordguess = (hashlib.md5(code.encode() + hexsalt).hexdigest())
       #print(passwordguess)
       if passwordguess == passwordhash:
           print("code found: " + code)
           #It will continue to try passwords until it gets to one where the hash matches
       else:
            continue
           
