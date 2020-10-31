from colorama import *
import eye
import json
import nmap3

def escaneo():
    global ip
    nmap = nmap3.Nmap()
    ip = str(input("ingrese ip o host a escanear >_ "))
    print(Fore.CYAN + "ESCANEANDO..."+Fore.RESET+"")

    resultados = nmap.scan_top_ports(ip)
    #print(resultados)#muestra los resultados en formato json
    #guardando los datos en un archivo json
    cadena = json.dumps(resultados)
    with open('escaneo.json','w') as f:
        json.dump(resultados,f)

def lectura():
    #ordenando los datos json
    with open('escaneo.json') as datos:
        Datos = json.loads(datos.read())
    i = 0

    print(""" \n\n
\t\t\tINICIO_________________________ \n\n
 """, Datos[ip][0])
    try:
        while i <=65535:
            i += 1
            print(Datos[ip][i],"\n")
    except IndexError:
        print(Fore.GREEN+"escaneo completo"+Fore.RESET+"")

if __name__ == "__main__":
    escaneo()
    lectura()
