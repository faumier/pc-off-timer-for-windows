import os
import datetime, time

def apagar_sistema(minutos):

    them = datetime.datetime.now()+ datetime.timedelta(minutes=minutos)

    while them > datetime.datetime.now():
        print ("que")
        time.sleep(1)
    else:
        
      os.system("shutdown /s /t 1")


