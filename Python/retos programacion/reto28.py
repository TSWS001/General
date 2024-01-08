#RETO28 EXPRESION MATEMATICA

def expresionMatematica(expresion):
   expresionArr = []
   count=0
   spacecheck=False
   for digit in expresion:
      expresionArr.append(digit)
   
      if(not(esNumero(digit) or digit==" " or digit=="+" or digit=="-" or digit=="*" or digit=="/" or digit=="%")):
         return False
      
      if(digit==" " and esNumero(expresionArr[count-1]) and expresionArr[count-2]==' ' and count!=2):
         spacecheck=True
      count+=1
   return spacecheck
      


#Comprobar si el string pasasdo es un numero o no
def esNumero(expresion):
   try:
      int(expresion)#si es integer
   except:
      return False
   
   try:
      float(expresion)#si es decimal
   except:
      return False
   return True

#print(expresionMatematica("5 + 6 / 7 - 4"))  
print(expresionMatematica("5 + 4"))  

