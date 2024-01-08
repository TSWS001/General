#RETO2 EL PARTIDO DE TENIS
sequencia =  ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']
puntuacion = ['Love', 15, 30, 40]
P1=0
P2=0
for i in sequencia:
  if i=='P1':
    P1+=1
  else:
    P2+=1

  if P1<=3 and P2<=3:
    if P1==3 and P2==3:
      print('Deuce')
    elif P1==3 and P1-P2==2:
      print('Ha ganado el P1')
    elif P2==3 and P2-P1==2:
      print('Ha ganado el P2')
    else:
      print(f'{puntuacion[P1]} - {puntuacion[P2]}')

  else:
    if P1==P2:
      print('Deuce')
    elif P1-P2==1:
      print('Ventaja P1')
    elif P2-P1==1:
      print('Ventaja P2')

    if P1-P2==2:
      print('Ha ganado el P1')
    elif P2-P1==2:
      print('Ha ganado el P2')


