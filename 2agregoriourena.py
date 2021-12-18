from typing import NewType
import requests
import json
urlorg = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "681b6cfb2df33416cd50337a96f2bb8b936e62ee"
}
response = requests.request('GET', urlorg, headers=headers, data = payload)
orgs = response.json()
sw=0
for org in orgs:    
    if org['name']=="Testlab4":
        sw=1
        ID=org['id']    
if sw==1:
      print("La Organizacion ya existe su ID es:"+ID)      
else:
      payload = '''{ "name": "Testlab4" }'''      
      response = requests.request('POST', urlorg, headers=headers, data = payload)
      org = response.json()
      ID=org['id']      
      print("Organizacion Fue Creada con el ID = "+ID)
urlorgnet = "https://api.meraki.com/api/v1/organizations/"+ID+"/networks"
response = requests.request('GET', urlorgnet, headers=headers, data = payload)
networks = response.json()
sw=0
for network in networks:        
    if network['name']=="Network-Psi":
        sw=1
        ID=network['id']    
if sw==1:
      print("La Red ya existe su ID es:"+ID)
      urlorgnetid = "https://api.meraki.com/api/v1/networks/"+ID
      payload = None
      response = requests.request('DELETE', urlorgnetid, headers=headers, data = payload)
      print("Fue eliminada de la Organizacion")
else:
    payload = '''{
        "name": "Network-Psi",
        "timeZone": "America/Los_Angeles",
        "tags": [ "tag1", "tag2" ],
        "notes": "Combined network for SudAmerica",
        "productTypes": [
            "appliance",
            "switch",
            "camera"
             ]
        }'''
    response = requests.request('POST', urlorgnet, headers=headers, data = payload)
    orgnet = response.json()
    ID=orgnet['id']      
    print("La Red en la Organizacion Fue Creada con el ID = "+ID)