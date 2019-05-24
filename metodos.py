#esto es un set
import random
diccionario = ["hala", "adios", "entrada"]
#fallos(extremidades)
f = 0
#aciertos
a = 0
#posiciones
#p = "vacio"
p = []
#respuesta
r = "vacio"
#contenido
c = []
def elegirPalabra():
    random.shuffle(diccionario)
    respuesta = ""
    for palabra in diccionario:
        respuesta = palabra
    return respuesta
#nota al volver a correr el programa, las palabras recien agregadas se pierden y solo agrega las nuevas
def agregarDiccionario(nuevaPalabra):
    diccionario.append(nuevaPalabra)

def dividirPalabra(respuesta):
    #contenido
    #c = []
    for x  in range(len(respuesta)):
        c.append(respuesta[x])
    return c
def obtenerTamaño(palabra):
    return len(palabra)


def analizarRespuesta(c,r,a,f,p):
    # print("Diga una letra")
    # r = str(input())
    #p = "vacio"
    p = []
    for x in range(len(c)):
        if(c[x]==r):
            #p = (c.index(r))+1
            p.append(x+1)
            a+=1
            #mostrar la letra adivinada en pantalla
            #print("prueba",p)
            #llamar a ganar
    if(p==[]):
        p = []
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
#p,a,f = analizarRespuesta(['h','o','l','o'],"a",a,f,p)
#print(a)
#print(f)
#print(p)
# prueba = ["hola","adios"]
# print(prueba[0])

