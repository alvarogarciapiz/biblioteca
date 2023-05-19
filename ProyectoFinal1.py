'''
    Proyecto final biblioteca - Álvaro García Pizarro
    27 de abril de 2023
    Formación Banco Santander - Python python 
'''
#Librerías necesarias
import csv

#Almacén de los libros en una lista
Libros = []

'''
    Clase Libro
'''
class Libro:
    def __init__(self, titulo, autor, añoPubli, paginas, estado) -> None:
        self.titulo = titulo
        self.autor = autor
        self.añoPubli = añoPubli
        self.paginas = paginas
        self.estado = estado
        
    def prestar(self):
        self.estado = False
        #Se entiende que False es que no está disponible (está prestado)
        
    def devolver(self):
        self.estado = True
        #Se entiende que True es que está disponible (se ha devuelto)
    
    def __str__(self) -> str:
        PR = ""
        if self.estado:
            PR = "no disponible"
        else:
            PR = "disponible"
        print("=>  " + self.titulo + " escrito por " + self.autor + " en " + self.añoPubli + " con " +
               self.paginas + " páginas y está " + PR + ".\n")
'''
    Métodos usados para el correto funcionamiento del programa
'''
def calcularPaginasTotal():
    totalPaginas = 0
    for Libro in Libros:
        totalPaginas+=int(Libro.paginas)
    return totalPaginas

def calcularMediaPaginas():
    return calcularPaginasTotal()/len(Libros)

def librosEnAño():
    año = int(input("Introduce el año del que quieres conocer cuántos libros hay en la biblioteca: "))
    num = 0
    for Libro in Libros:
        if año==int(Libro.añoPubli):
            num+=1
    print("Hay " + str(num) + " libro/s del año " + str(año))
        

def validarSTR(query):
    while True:
        a = input(query)
        res = isinstance(a, str)
        if res:
            return a
            break
        
def bibliotecaACsv():
    with open('biblioteca.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for x in Libros:
            writer.writerow([x.titulo, x.autor, x.añoPubli, x.paginas, x.estado])
        
def CsvABiblioteca():
    nombreFichero = input("Introduce el nombre del fichero del que quieres importar los datos: ")
    with open(nombreFichero, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
    #Ahora se pasa de la lista a objetos y se añaden a la biblioteca
    for a in data:
        L1 = Libro(a[0], a[1], a[2], a[3], bool(a[4]))
        Libros.append(L1)
        
def end():
    print("El número total de páginas de la biblioteca es de " + str(calcularPaginasTotal()))
    print("El número medio de páginas de un libro de la biblioteca es de " + str(calcularMediaPaginas()))
    librosEnAño()
    
def buscarPorAutor():
    autor = input("Introduce el nombre del autor del que quieras buscar libros: ")
    for Libro in Libros:
        if autor == Libro.autor:
            Libro.__str__()
            
def buscarPorTitulo():
    titulo = input("Introduce el titulo del libro que quieras buscar: ")
    for Libro in Libros:
        if titulo == Libro.titulo:
            Libro.__str__()
#Menú
def menu():
    print("---------------------------------")
    print("|  [1] Añadir un libro          |")
    print("|  [2] Buscar libro por autor   |")
    print("|  [3] Buscar libro por título  |")
    print("|  [4] Listar todos los libros  |")
    print("|  [5] Exportar a archivo       |")
    print("|  [6] Cargar desde archivo     |")
    print("|  [7] SALIR                    |")
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
            print("Introduce los siguientes datos para añadir un libro a la biblioteca ")
            titulo = validarSTR("Titulo :")
            autor = validarSTR("Autor: ")
            añoPubli = validarSTR("Año de publicación: ")
            paginas = validarSTR("Número de páginas: ")
            estado = False
            Lx = Libro(titulo, autor, añoPubli, paginas, estado)
            print("Se ha añadido el siguiente libro: ")
            Lx.__str__()
            Libros.append(Lx)
        case 2:
            buscarPorAutor()
        case 3:
            buscarPorTitulo()
        case 4:
            for Libro in Libros:
                Libro.__str__()
        case 5:
            bibliotecaACsv()
        case 6:
            CsvABiblioteca()
        case 7:
            end()
            exit()
            
            
'''
    biblioteca.csv =>
    
    El quijote,Cervantes,1789,431,False
    Un libro,Juan,2021,381,False
    Patrones de diseño, Refactoring Guru, 2022, 1032, False

Se puede usar a modo de ejemplo para cargar libros de la biblioteca
    
'''