#RETO1 EL LENGUAJE HACKER
alfabet = ['4','l3','[',')','3','|=','&','#','1',',_|','>|','1','/\\/\\'
,'^/','0','|*','(_,)','I2','5','7','(_)','\\/','\\/\\/','><','j','2']
palabra=input('Introduce la palabra: \n')
for letra in palabra:
  if letra.isalpha()==True:
    print(alfabet[ord(letra)-ord('a')],end='')
  else:
    print(letra,end='')