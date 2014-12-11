class Archivo():
    Ruta = ""

    def __init__(self,ruta):
        self.Ruta = ruta
        arch = open(self.Ruta,"w")
        arch.close()

    def Escribir(self,line):
        arch = open(self.Ruta,"a")
        line += "\n"
        arch.write(line)
        arch.close()

    def Leer(self):
        arch = open(self.Ruta,"r")
        line = arch.readline()
        while line != "":
            print(line)
            line = arch.readline()          
        arch.close()
