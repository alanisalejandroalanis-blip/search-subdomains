import requests
import sys

#aqui estamos declarando las variables donde vamos a guardar los datos que capture sys que guapo estoy muak

url = sys.argv[1]

diccionario = sys.argv[2]

 # el with sirve para cerrarlo despues de ñlerrlo y luego le decimos abre diccionario en modo lectura y saca uno que eso de sacar uno lo hace por predeterminado python el pone ese valor y luego le dices guardalo como alias 
with open(diccionario, "r") as alias:
 #despues se guarda en una variable llamado lineao porq alias es temporal y se va borrar el for le dice que haga eso cada que pase por ahi y que se repita 
  for  linea in alias: 
 
 #aqui etamos limpiando la variable linea y asignando esa palabra limpia a la variable

   palabra_limpia = linea

   palabra_limpia = linea.strip() 

   url_limpia = url + "/" + palabra_limpia 

   respuesta = requests.get(url_limpia) 
   if respuesta.status_code == 200:
     print("esta si jala -->", url_limpia)
