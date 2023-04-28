'''
Proyecto Final 2
'''
import csv, datetime, time

class Venta:
    def __init__(self, producto, q, p, fecha) -> None:
        self.producto = producto
        self.q = q
        self.p = p
        self.fecha = fecha

class Ventas:
    def __init__(self, ventas) -> None:
        self.ventas = ventas
        
    def registrar_venta(self, venta):
        with open('ventas.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([venta.producto, venta.q, venta.p, venta.fecha])
    
    def consultar_ventas(self, fecha1, fecha2):
        for i in self.ventas:
            if i.fecha <= fecha1 and i.fecha >= fecha2:
                print(i)
            
class ArchivoCSV:
    def __init__(self) -> None:
        pass
    
    def leer_archivo(self):
        ventas = []
        with open("ventas", newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            ventas.append(data)
        return ventas
    
    def escribe_archivo(self, venta):
        with open('ventas.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([venta.producto, venta.q, venta.p, venta.fecha])

Venta1 = Venta("ordenador", "1", "900", "11/11/2011")
Venta2 = Venta("movil", "8", "659", "10/12/2011")
ListaVentas = [Venta1, Venta2]   
Archivo = ArchivoCSV()
Ventas = Ventas(ListaVentas) 
Ventas.registrar_venta(Venta1)
Ventas.registrar_venta(Venta2)
            
def menu():
    print("---------------------------------")
    print("|  [1] Registrar una venta      |")
    print("|  [2] Consultar ventas         |")
    print("|  [3] SALIR                    |")
    print("---------------------------------")
    print("\n")
    
    return int(input("Introduce una opción: "))

'''
    Ejecución del programa
'''
while(True):
    opcion = menu()
    match opcion:
        case 1:
            print("Introduce los datos para registrar una venta: ")
            producto = input("Introduce el nombre del producto")
            q = input("Introduce la cantidad vendida")
            p = input("Introduce el precio de venta")
            fecha = datetime(input("Introduce la fecha de venta"))
            V1 = Venta(producto, q, p, fecha)
            Ventas.registrar_venta(V1)
        case 2:
            fecha1 = datetime(input("Introduce la primera fecha"))
            fecha2 = datetime(input("Introduce la primera fecha"))
            Ventas.consultar_ventas(fecha1, fecha2)
        case 3:
            exit()