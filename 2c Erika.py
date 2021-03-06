#2c. Crear un script para crear en el router Cisco CSR1000v, 
# una interface Loopback 6, con la dirección IP 10.10.1.6/16 y una
# ruta default usando esa interface Loopback como salida.
# Mostrar como salida del script, la tabla de rutas 

import json
import requests
requests.packages.urllib3.disable_warnings()
api_url = "https://10.10.0.254/restconf/data/ietf-interfaces:interfaces/interface=Loopback6"
headers = { "Accept": "application/yang-data+json",
             "Content-type": "application/yang-data+json"
            }
basicauth = ("admin","cisco")
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback6",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.1.1.6",
                    "netmask": "255.255.0.0"
                }
            ]           
        },
        "ietf-ip:ipv6": {}
    }   
}
resp = requests.put(api_url, data=json.dumps(yangConfig),
 auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
"""
#Creando la ruta por defecto
api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing-state/routing-instance=default/ribs/rib=ipv4-default/routes/route=0.0.0.0%2F0"
headers = { "Accept": "application/yang-data+json",
             "Content-type": "application/yang-data+json"
            }
basicauth = ("admin","cisco")
yangConfig = {
    "ietf-routing:route": {
        "destination-prefix": "0.0.0.0/0",
        "route-preference": 1,
        "metric": 1,
        "next-hop": {
            "outgoing-interface": "Loopback6",
            "next-hop-address": "0.0.0.0"
        },
        "source-protocol": "ietf-routing:static",
        "active": [
            null 
        ],
        "update-source": "0.0.0.0"
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig),
 auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
"""
# mostrando las rutas
requests.packages.urllib3.disable_warnings()
api_url = "https://10.10.0.254/restconf/data/ietf-routing:routing-state/routing-instance=default/ribs/rib=ipv4-default/routes"
headers = { "Accept": "application/yang-data+json", "Content-type":"application/yang-data+json"
            }
basicauth = ("admin", "cisco")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
response_json = resp.json()
print(json.dumps(response_json, indent=4))