#RETO27 CUENTA ATRÁS

def CuentaAtras(ini,paso):
    if(esEnteroPositivo(ini) and esEnteroPositivo(paso)):
       i=ini
       while i>=0:
          print(i)
          i-=paso
    else:
       print("Not Integer Positive number\n")

def esEnteroPositivo(num):
    if(num>=0 or isinstance(num,int)):
      return True
    else:
       return False

   
CuentaAtras(50,10)