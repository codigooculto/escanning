from colorama import *
import eye
import json
import nmap3
import datetime

class Pymap:
    def __init__(self):
        global x #variable global
        global ip #variable global
        self.x = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.nmap = nmap3.Nmap()
        self.ip = str(input("ingrese ip o host a escanear: "))
        print(Fore.CYAN + "Escaneando..."+Fore.RESET+"")
        self.resultados = self.nmap.scan_top_ports(self.ip)
        #print(self.resultados)
        
        #guardando los datos en un archivo json
        
        self.cadena = json.dumps(self.resultados)
        with open('json/escaneo1_{}.json'.format(self.x),'w') as self.f:
            json.dump(self.resultados,self.f)
            
    def lectura(self):
        #ordenando los datos en json
        with open('json/escaneo1_{}.json'.format(self.x)) as self.datos:
            self.Datos = json.loads(self.datos.read())
        
        self.i = 0
        print(""" \n\n
\t\t\tINICIO_________________________ \n\n
 """, self.Datos[self.ip][0])
        try:
            while self.i <=65535:
                self.i += 1
                self.imprime = print(self.Datos[self.ip][self.i],"\n")

        except IndexError:
            print(Fore.GREEN+"escaneo completo"+Fore.RESET+"")
            
            
ejecucion = Pymap()#se ejecuta luego que se crea un objeto de la clase Pymap

ejecucion.lectura()
