#esto es un set
diccionario = {"hola", "adios", "entrada","a","b","c","d","e","f","g","h","y","j"}
#fallos(extremidades)
f = 0
#aciertos
a = 0
#posiciones
p = "vacio"
#respuesta
r = "vacio"
def elegirPalabra():
    respuesta = ""
    for palabra in diccionario:
        respuesta = palabra
    return respuesta
#nota al volver a correr el programa, las palabras recien agregadas se pierden y solo agrega las nuevas
def agregarPalabra():
    print("Palabara a agregar: ")
    nuevaPalabra = str(input())
    diccionario.add(nuevaPalabra)

def dividirPalabra(respuesta):
    #contenido
    c = []
    for x  in range(len(respuesta)):
        c.append(respuesta[x])
    return c
def obtenerTamaño(palabra):
    return len(palabra)

def analizarRespuesta(c,a,f,p):
    print("Diga una letra")
    r = str(input())
    p = "vacio"
    for x in range(len(c)):
        if(c[x]==r):
            #p = (c.index(r))+1
            p = x+1
            a+=1
            #mostrar la letra adivinada en pantalla
            print("prueba",p)
            #llamar a ganar
    if(p=="vacio"):
        p = "vacio"
        f+=1
        #llamar a perder
        # try:
        #     p = (c.index(r))+1
        #     a+=1
        #     #llamar a ganar  
        # except:
        #     p = "vacio"
        #     f+=1
        #     #llamar a perder
    return (p,a,f)



# agregarPalabra()
# print(diccionario)

# hola = elegirPalabra()
# print(hola)

#c = dividirPalabra("hola")
#print(c)

#t = obtenerTamaño("hola")
#print(t)

#hay un detalle en el metodo analizarRespuesta por que solo arroja la ultima posicion obtenida, 
#pero si busca todas las coincidencias
p,a,f = analizarRespuesta(['h','o','l','o'],a,f,p)
print(a)
print(f)
print(p)
# prueba = ["hola","adios"]
# print(prueba[0])

