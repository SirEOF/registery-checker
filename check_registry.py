
from _winreg import *
import _winreg

keytosearch="AppEvents"

i=0
while(True):
    try:
        tmp= _winreg.EnumKey(HKEY_CLASSES_ROOT,i)
        if(tmp== keytosearch):
            print "found in root",tmp
        i+=1
    except:
        break
i=0
while(True):
    try:
        tmp= _winreg.EnumKey(HKEY_CURRENT_USER,i)
        if(tmp== keytosearch):
            print "found in current user",tmp
        i+=1
    except:
        break
i=0
while(True):
    try:
        tmp= _winreg.EnumKey(HKEY_LOCAL_MACHINE,i)
        if(tmp== keytosearch):
            print "found in local",tmp
        i+=1
    except:
        break
i=0
while(True):
    try:
        tmp= _winreg.EnumKey(HKEY_USERS,i)
        if(tmp== keytosearch):
            print "found in users",tmp
        i+=1
    except:
        break
i=0
while(True):
    try:
        tmp= _winreg.EnumKey(HKEY_CURRENT_CONFIG,i)
        if(tmp== keytosearch):
            print "found in config",tmp
        i+=1
    except:
        break
