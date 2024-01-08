#RETO24 CIFRADO CESAR

def EsMayuscula(letra):
  if ord(letra)>=ord('A') and ord(letra)<=ord('Z'):
    return True
  else:
    return False


# devuelve la letra movida 'num' espacios segun el cifrado de cesar
# num puede ser negativo

def CifradoCesarLetra(letra,num):
  if letra.isalpha()==False:
    return letra
  
  num_ascii=ord(letra)+num

  if EsMayuscula(letra):  #caso si es mayuscula
    num_ascii=ord('A')+(num_ascii-ord('A'))%26
  else:                   #caso si NO es mayuscula
    num_ascii=ord('a')+(num_ascii-ord('a'))%26
  
  return chr(num_ascii)

txt2=''
txt = input("El texto a cifrar: ")
for letra in txt:
  letracifrado=CifradoCesarLetra(letra,3)
  print(letracifrado, end='')
  txt2=txt2+letracifrado

print("\nTexto descifrada: ")

for letra in txt2:
  print(CifradoCesarLetra(letra,-3), end='')
