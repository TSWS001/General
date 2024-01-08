#RETO6 PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK

list = [("🗿","✂️"), ("✂️","🗿"), ("🦎","✂️"), ("✂️","📄"),]
logica = {
    "🗿" : ["🦎","✂️"],
    "🖖" : ["✂️","🗿"],
    "📄" : ["🗿","🖖"],
    "🦎" : ["🖖","📄"],
    "✂️" : ["📄","🦎"],
    }


def juego(jugadas):
  jugador1=0
  jugador2=0
  for jugada in jugadas:
    if( esMayor(jugada[0],jugada[1]) == 0):
      jugador1+=1
      print("Player 1 ")
    elif( esMayor(jugada[0],jugada[1]) == 1):
      jugador2+=1
      print("Player 2 ")
    elif( esMayor(jugada[0],jugada[1]) == 2):
      print(" TIE")
  print("and",end=" ")
  if(jugador1 > jugador2):
    print("Player 1 WIN")
  elif(jugador1 < jugador2):
    print("Player 2 WIN")
  elif(jugador1 == jugador2):
    print(" TIE ! ! ! ")

#retorna un 0 si el obj1 es mayor que obj2, 
#un 1 en caso contrario y un 2 si es empate
def esMayor(obj1, obj2):
  if( obj1==obj2 ):
    return 2
  elif( obj2==logica[obj1][0] or obj2==logica[obj1][1] ):
    return 0
  return 1


juego(list)
