#RETO9 HETEROGRAMA, ISOGRAMA Y PANGRAMA

def heterograma(palabra):
  for i in range(len(palabra)):
      for j in range(0,i):
        if(palabra[j] == palabra[i]):
          return False
  return True

def pangrama(palabra):
  if len(palabra)<=25:
    return False
  abc = "abcdefghijklmnopqrstuvwxyz"
  palabra = palabra.lower()
  palabra = palabra.replace(' ','')
  
  for i in palabra:
    abc = abc.replace(i,'')
  if abc == '':
    return True
  else:
    return False

def isograma(palabra):
  ArrCantidad = []
  for i in range(len(palabra)):
    ArrCantidad.append(buscarCantidad(palabra, palabra[i]))

  for k in range(len(ArrCantidad)-1):
    if ArrCantidad[k] != ArrCantidad[k+1]:
      return False
  return True

def buscarCantidad(lista, item):
  num=0
  for it in lista:
    if (it == item):
      num+=1

  return num

def func(palabra):
  print(f'{palabra} es:')
  print(f'heterograma: {heterograma(palabra)}')
  print(f'isograma: {isograma(palabra)}')
  print(f'pangrama: {pangrama(palabra)}\n')

func('yuxtaponer')
func('bilabial')
func('Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú')