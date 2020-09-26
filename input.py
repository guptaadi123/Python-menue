#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()

myx = mydata.getvalue("x")
if myx=="1":
    a=subprocess.getoutput("date")
    print(a)
elif myx=="2":
    b=subprocess.getoutput("cal")
    print(b)
elif myx=="3":
    c=subprocess.getoutput("firefox")
else:
    print("invalid option please try again from the give menue")
#o = subprocess.getoutput("sudo {0}".format( myx))
print(o)
