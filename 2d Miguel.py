# 2d Crear un script para crear un Room con el nombre “Devnet-GroupPsi”,
# en este Room deben estar incluidos todos los integrantes del grupo. 
# En caso ya exista el Room, el script debe mostrar el Room-ID y todos los
# correos de todos los integrantes. 
# Luego debe enviar un mensaje al Room con la ruta del contenedor en el Docker Hub.
import requests
import json
import sys

import requests

access_token = 'ZjBkYWJhZjYtNmRhNS00NDgyLWEyYWYtNmYyZmE5MTRhMDczMDIwYmEwYzgtZmRm_P0A1_5d96674f-de50-43d7-ae6b-8071b71cb457'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
   'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json()['items'][0]['title'])

#sala = (json.dumps(res.json()["title"]))
# 1=existe; 0 = no existe
sala = 0
print(sala)
if sala == 1:
   print("Existe")
   print(res.json())
else: 
    print("no existe")
    headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
    params={'title': 'Devnet-GroupPsi_b'}
    res = requests.post(url, headers=headers, json=params)
    #print(res.json())
    #room_id = ''
    #person_email = 'davidcarrilloyepez@hotmail.com'
    #url = 'https://webexapis.com/v1/memberships'
    #headers = {
    #    'Authorization': 'Bearer {}'.format(access_token),
    #    'Content-Type': 'application/json'
    #}
    #params = {'roomId': room_id, 'personEmail': person_email}
    #res = requests.post(url, headers=headers, json=params)
    #print(res.json())
    

