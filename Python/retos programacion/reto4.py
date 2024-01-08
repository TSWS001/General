#RETO4 PRIMO, FIBONACCI Y PAR

def function(num):
  print(f"{num} ",end="")
  if primo(num)==True:
    print("es primo,",end="")
  else:
    print("no es primo,",end="")
  
  if fibonacci(num)==True:
    print("fibonacci y es ",end="")
  else:
    print("no es fibonacci y es ",end="")  
  
  if par(num)==True:
    print("par")
  else:
    print("impar") 

def par(num):
  if num%2==0:
    return True
  return False

def primo(num):
  for i in range(2,num):
    if num%i==0:
      return False
  return True

def fibonacci(num):
  primero=0
  segundo=1
  for i in range(0,num):
    aux=primero+segundo
    if(num==aux):
      return True
    primero=segundo
    segundo=aux
  return False

function(7)