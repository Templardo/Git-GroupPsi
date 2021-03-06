# 2d Crear un script para crear un Room con el nombre “Devnet-GroupPsi”,
# en este Room deben estar incluidos todos los integrantes del grupo. 
# En caso ya exista el Room, el script debe mostrar el Room-ID y todos los
# correos de todos los integrantes. 
# Luego debe enviar un mensaje al Room con la ruta del contenedor en el Docker Hub.
import requests
import json
import sys

access_token = 'Y2M5YmEyZTMtOWI4NS00MGVlLWEwN2QtNmNhOWFiMWE5MDJiZTA5M2JjMWItYWE1_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
   'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
salas=res.json()

#CREAMOS UNA FUNCIÓN QUE VERIFIQUE SI ES QUE EXISTE LA SALA
def existeSala(salasResponse,salaBuscada):
      print('Buscando',salaBuscada)       
      for sala in salasResponse['items']:            
            if str(sala['title']) == salaBuscada:
                  print("\n\n",sala,"\n\n")                    
                  return sala['id']
      return False

nombreSala='Devnet-GroupPsi'
ExisteSala = existeSala(salas,nombreSala)

if(ExisteSala!=False):
   print('Existe con id:',ExisteSala)  

   room_id = ExisteSala

   urlmiembros = 'https://webexapis.com/v1/memberships'
   headers = {
      'Authorization': 'Bearer {}'.format(access_token),
       'Content-Type': 'application/json'
   }
   params = {'roomId': room_id}
   resMiembros = requests.get(urlmiembros, headers=headers, params=params)
   personas = resMiembros.json()
   
   print("PARTICIPANTES:")
   for miembro in personas['items']:
          print(miembro['personEmail'])

   #ENVIA EL MENSAJE DEL DOCKER
   message = 'https://hub.docker.com/r/ferurena72/dockergrouppsi'
   url = 'https://webexapis.com/v1/messages'
   headers = {
      'Authorization': 'Bearer {}'.format(access_token), 
      'Content-Type': 'application/json'
   }
   params = {'roomId': room_id, 'markdown': message}
   res = requests.post(url, headers=headers, json=params) 
   print(res.json())

else:
   print('No existe, creando sala...')          
   
   params={'title': nombreSala}
   res = requests.post(url, headers=headers, json=params)
   print(res.json())
   
   params={'max': '100'}
   res = requests.get(url, headers=headers, params=params)
   salas=res.json()

   room_id = existeSala(salas,nombreSala)
   print(room_id)
   #room_id='Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMDY5N2Q2ZDAtNWZlMC0xMWVjLWI1MWMtODcwNTJiY2YxODcx'
   url = 'https://webexapis.com/v1/memberships'

   print('Añadiendo David Carrillo')
   person_email = 'davidcarrilloyepez@hotmail.com'
   params = {'roomId': room_id, 'personEmail': person_email}
   res = requests.post(url, headers=headers, json=params)
   print(res.json())

   print('Añadiendo Gregorio Urena')
   person_email = 'fernando.urena@sistemas.edu.bo'
   params = {'roomId': room_id, 'personEmail': person_email}
   res = requests.post(url, headers=headers, json=params)
   print(res.json())

   print('Añadiendo Miguel Reynolds')
   person_email = 'miguel.reynolds@gmail.com'
   params = {'roomId': room_id, 'personEmail': person_email}
   res = requests.post(url, headers=headers, json=params)
   print(res.json())

   print('Añadiendo Erika Viña')
   person_email = 'lexierika@gmail.com'
   params = {'roomId': room_id, 'personEmail': person_email}
   res = requests.post(url, headers=headers, json=params)
   print(res.json())
