#importes
import sys

#clase principal
class biblioteca():


    @staticmethod
    def leeTxt(libro_solicitado, cantidad_solicitada):
        print("loading....")
        archivo = open("catalogo.txt", "r")
        contador = 0
        for linea in archivo.readlines():
            print("linea que estoy leyendo.."+linea)
            iterador = iter(linea)
            letra = next(iterador)
            contador = contador + 1
            print("letra.."+letra)
            libro = ""
            
            while (letra != ","):
                libro += letra
                letra = next(iterador)
                contador = contador + 1
            
            if(libro == libro_solicitado):
                print("libro encontrado.."+libro)
                letra = next(iterador)
                contador = contador + 1
                if(letra >= cantidad_solicitada):
                    print("FELICIDADES! la cantidad solicitada esta disponible.."+letra)
                    
                    print(contador)
#main
if __name__ == '__main__':
    sacarLibro = biblioteca()

    sacarLibro.leeTxt("harry potter 1", "1")
