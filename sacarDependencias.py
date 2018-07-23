# -*- coding: utf-8 -*-
import argparse
import os.path

#Funciones
def revisarImport(linea):
    if 'import ' in linea or ' import ' in linea:
        if  "from" in linea:
            linea = linea.split('from')[1].split(' ')
            for line in linea:
                if line != "":
                    f.write(line.replace(",","") + str("\n"))
                    print('Añadida: ' + line.replace(",",""))
        else:
            linea = linea.split(' ')
            f.write(linea[1] + str("\n"))
            print('Añadida: ' + linea[1])

def leerFichero(fichero):
    with open(fichero, "r") as ObjFichero:
        for line in ObjFichero:
            revisarImport(line.replace("\n",""))

#Argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-f" , "--file",  help="Fichero a depurar")
parser.add_argument("-d" , "--directory",  help="Directorio a depurar")
args = parser.parse_args()

if not args.file and not args.directory:
    parser.print_help()
else:
    if args.file:
        f = open("requeriments.txt", 'w')
        leerFichero(args.file)
        f.close()

    if args.directory:
        f = open("requeriments.txt", 'w')
        for dirpath, dirnames, filenames in os.walk(args.directory):
            for filename in [f for f in filenames if f.endswith(".py")]:
                leerFichero(os.path.join(dirpath, filename))
        f.close()
