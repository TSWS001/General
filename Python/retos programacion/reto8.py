#RETO8 EL GENERADOR DE PSEUDOALEATORIO
import time

def random(final):
    return time.time_ns() %101
      
for i in range(0,101):
  print(random(100))
