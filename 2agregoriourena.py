from typing import NewType
import requests
import json
url = "https://api.meraki.com/api/v1/organizations"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}
response = requests.request('GET', url, headers=headers, data = payload)
orgs = response.json()
print(json.dumps(orgs, indent=4))
sw=0
for org in orgs:    
    if org['name']=="Testlab":
        sw=1
        ID=org['id']    
if sw==1:
      print("La Organizacion ya existe su ID es:")
      print(ID)      
else:
      payload = '''{ "name": "Testlab" }'''
      url = "https://api.meraki.com/api/v1/organizations"
      response = requests.request('POST', url, headers=headers, data = payload)
      print("Organizacion Fue Creada...")
response = requests.request('GET', url, headers=headers, data = payload)
orgs = response.json()
for org in orgs:    
    url = "https://api.meraki.com/api/v1/organizations/"+org['id']+"/networks"
    networks = requests.get(url,headers=headers)
    networks = networks.json()
    for network in networks:
        print(network['id'])