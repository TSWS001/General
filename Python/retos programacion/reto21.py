#RETO21 NUMERO PRIMOS GEMELOS 

def primo(num):
  for j in range(2,num):
    if num%j==0:
      return False
  return True

max =int( input('valor max: '))
anterior=3
for i in range(1,max):
  
  if primo(i)==True:
    if i-anterior==2:
      if anterior!=3:
        print(', ',end='')
      print(f'({anterior}, {i})',end='')
    anterior=i
    
    

    
      
            
     