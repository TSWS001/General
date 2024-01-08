#RETO23 LA BASE DE DATOS

import pymysql

try:
  conection = pymysql.connect(host='mysql-5707.dinaserver.com',
                              user='mouredev_read',
                              password='mouredev_pass',
                              db='moure_test')
  
  #Lets read something at the DDBB
  try:
    with conection.cursor() as cursor:
      cursor.execute('SELECT * FROM `challenges`;')

      peliculas = cursor.fetchall()

      for pelicula in peliculas:
        print(pelicula)
  finally:
    cursor.close()
    conection.close()

except(pymysql.err.OperationalError, pymysql.err.InternalError) as e:
  print("Something went wrong: ",e)



    
      
            
