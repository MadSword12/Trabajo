#desarrollo: Fabian Riveros.

def leer_archivo(ar):
    ar = open("cadena.dat")
    ar.close
    return ar 

#linea donde el programa lee el archivo entregado

def desarrollo(ar):
    cad = list(ar)
    cadsol = [ ] 
    for i in cad: 
        for j in i: 
            if j == "T":
                cadsol.append("A")
            if j == "A":
                cadsol.append("T")
            if j == "G":
                cadsol.append("C")
            if j == "C":
                cadsol.append("G")
    cadsolstr = " "
    for i in cadsol:
        cadsolstr = cadsolstr + i 
    cadstr = " "
    for i in cad:
        cadstr = cadstr + i
    return cadstr, cadsolstr

#linea donde el programa empieza a lograr el objetivo dado reemplazando las letras detro del archivo y las reemplaza por las dadas

def solucion(nombre, cad, cadsol):
    nombre = open(nombre, "w")
    nombre.write("Bases Nitrogenadas\n")
    nombre.write("N1:")
    nombre.write(" ".join(cad))
    nombre.write("\nN2:")
    nombre.write(" ".join(cadsol))
    return

#generacion del archivo, punto dado y exigido en la actividad

if __name__ == "__main__":
    cad = leer_archivo("cadena.dat")
    cadstr, cadsolstr = desarrollo(cad)
    solucion("hélice.dat", cadstr, cadsolstr)

#donde se llama a toda las funciones anteriormente propuestas.
