#RETO3 GENERADOR DE CONTRASEÑAS

import random

def generarContrasena(longitud, mayuscula, numero, simbolo):
  res=''
  for i in range(longitud):
    op=random.randrange(3)
    if op==0 and mayuscula==True:
      res=res+chr(random.randint(ord('A'),ord('Z')))
    elif op==1 and numero==True:
      res=res+str(random.randint(1,9))
    elif op==2 and simbolo==True:
      res=res+chr(random.randint(ord(' '),ord('\\')))
    else:
      res=res+chr(random.randint(ord('a'),ord('z')))
  return res
contrasena=generarContrasena(16,True,True,True)
print(contrasena)
