#2a.	Crear un script para acceder al Dashboard Meraki (Always On) el cual debe tener tres opciones:
#           i.	Crear en el Dashboard de Meraki una organización llamada Devnet-GroupPsi , en caso ya exista el grupo debe mostrar su el ID de la organización.
#           ii.	Crear una red llamada Network-Psi, en caso ya exista debe permitir borrarla.
#           iii. API-Key: 76d52810510e74aac786e0b34dcb52c42d3fac0b, en caso no sea correcta debe permitir ingresarla mediante el teclado.

from typing import NewType
import requests
import json
#meraki_api_key_valida = "681b6cfb2df33416cd50337a96f2bb8b936e62ee"
meraki_api_key = "76d52810510e74aac786e0b34dcb52c42d3fac0b"
urlorg = "https://api.meraki.com/api/v1/organizations"
payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": meraki_api_key, 
}
response = requests.request('GET', urlorg, headers=headers, data = payload)
if(response.status_code ==401): 
    print("El API KEY UTILIZADO POR DEFECTO NO ES VALIDO")
    meraki_api_key = input("Ingrese un API KEY Valido:")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": meraki_api_key,
    }
    response = requests.request('GET', urlorg, headers=headers, data = payload)        
    if(response.status_code ==200): 
        orgs = response.json()
        sw=0
        for org in orgs:    
            if org['name']=="GroupPsi":
                sw=1
                ID=org['id']    
        if sw==1:
              print("La Organizacion GroupPsi ya existe su ID es:"+ID)      
        else:
            payload = '''{ "name": "GroupPsi" }'''      
            response = requests.request('POST', urlorg, headers=headers, data = payload)
            org = response.json()
            ID=org['id']      
            print("Organizacion GroupPsi Fue Creada con el ID = "+ID)
        urlorgnet = "https://api.meraki.com/api/v1/organizations/"+ID+"/networks"
        response = requests.request('GET', urlorgnet, headers=headers, data = payload)
        networks = response.json()
        sw=0
        for network in networks:        
            if network['name']=="Network-Psi":
                sw=1
                ID=network['id']    
        if sw==1:
            print("La Red Network/Psi ya existe su ID es:"+ID)
            resp = input("Desea eliminar la red Network-Psi <S/N>")
            if (resp=='S') or (resp=='s'):
                urlorgnetid = "https://api.meraki.com/api/v1/networks/"+ID
                payload = None
                response = requests.request('DELETE', urlorgnetid, headers=headers, data = payload)
                print("La red Network-Psi Fue eliminada de la Organizacion GroupPsi")
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
            print("La Red Network-Psi en la Organizacion GroupPsi Fue Creada con el ID = "+ID)
    else:
        print("El NUEVO API KEY INGRESADO TAMPOCO ES VALIDO")        