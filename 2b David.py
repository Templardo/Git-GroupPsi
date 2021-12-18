#b.	(David)Crear un script para acceder al DNA center (Always On), el cual debe mostrar: 
#    todos los dispositivos registrados (inventario) con sus respectivas direcciones IP
#    de gestión y el número de serie de cada equipo, en formato de texto ordenado
#    (no en formato JSON). El script deberá generar el token de acceso de ser necesario.

import requests
from requests.api import head
from urllib3.exceptions import InsecureRequestWarning
import json
import sys

URL_BASE = "https://sandboxdnac.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "Cisco123!"

#CREAMOS UNA FUNCIÓN PARA QUE NOS GENERE EL TOKEN
def obtener_token(urlbase, user,passw):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)    
    URL_TOKEN= urlbase+"/dna/system/api/v1/auth/token"    
    try:
        r = requests.post(URL_TOKEN,auth=(user,passw),verify=False)
        return r.json()["Token"]
    except:        
        print("Status: %s"%r.status_code)
        print("Response: %s"%r.text)
        sys.exit()

#FUNCIÓN PARA OBTENER LA LISTA DE DISPOSITIVOS (API - NETWORK-DEVICE)
def Dispositivos(urlbase,cabeceras,modificador):
    URL_LISTADISP = urlbase+"/dna/intent/api/v1/network-device"+modificador
    try:        
        r = requests.get(URL_LISTADISP,headers=cabeceras,verify=False)
        return r
    except:        
        print("Status: %s"% r.status_code)
        print("Response: %s"% r.text)
        sys.exit()

#GENERAMOS EL TOKEN PARA LA MANIPULACIÓN DEL DNA CENTER sandboxdnac.cisco.com

token = obtener_token(URL_BASE,USERNAME,PASSWORD)
#print("Token: ",(token))

#Generamos la cabecera
cabecera= {"x-auth-token":token}
#Utilizamos la API COUNT POR MEDIO DEL MODIFICADOR /count
modificador="/count"
resp=Dispositivos(URL_BASE,cabecera,modificador)
#OBTENEMOS EL TOTAL DE DISPOSITIVOS
cantidadDispositivos = int(json.dumps(resp.json()["response"]))
print("\nCantidad de Dispositivos encontrados:",cantidadDispositivos,"\n")
modificador=""
#OBTENEMOS LOS DISPOSITIVOS EN FORMATO JSON
resp=Dispositivos(URL_BASE,cabecera,modificador)
json_resp=resp.json()["response"]

#FILTRAMOS LA INFORMACIÓN POR MEDIO DE UN BUCLE
for i in range(0,cantidadDispositivos):
    dispositivo=json_resp[i]
    print("Switch#%d Tipo: %s \nIPGestión: %s \nNroSerie: %s"%(i,dispositivo['type'],dispositivo['managementIpAddress'],dispositivo['serialNumber']))