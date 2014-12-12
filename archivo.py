import os


class Archivo():
    Ruta = ""

    def __init__(self, ruta):
        self.Ruta = ruta
        arch = open(self.Ruta, "a+")
        arch.close()

    def Escribir(self):
        arch = open(self.Ruta, "a")
        line, escribir = "", True
        while escribir:
            line = input("Escriba algo en el archivo: ")
            line += "\n"
            arch.write(line)
            resp = input("¿Seguir escribiendo? Introduzca \"n\" pasa salir. ")
            if resp == "n":
                escribir = False
            else:
                os.system("cls")
        arch.close()

    def Leer(self):
        arch = open(self.Ruta, "r")
        print(arch.read())
        arch.close()
