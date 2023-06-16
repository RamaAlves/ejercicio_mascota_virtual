import random
from mascota import imagen
 
class MascotaVirtual:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 60
        self.imagen = imagen.inicio
        self.imagen_triste = imagen.triste
        self.imagen_muerto = imagen.muerto
        self.imagen_disgustado = imagen.disgustado
        self.imagen_feliz = imagen.feliz
    
    def alimentar(self):
        #seteando felicidad
        self.felicidad -= random.randint(5, 10)
        if self.felicidad < 0:
            self.felicidad = 0
        if self.hambre ==0:
            print(self.imagen_disgustado)
            print(self.nombre, "esta lleno. Ya no puede comer más!")
        else:
            #seteando hambre
            self.hambre -= random.randint(10, 15)
            if self.hambre < 0:
                self.hambre = 0
            print(self.imagen_feliz)
            print(self.nombre, "ha sido alimentado.")

    def jugar(self):
        if self.hambre < 70:
            #seteando felicidad
            self.felicidad += random.randint(10, 25)
            if self.felicidad > 100:
                self.felicidad = 100
            #seteando hambre
            self.hambre += random.randint(10, 15)
            if self.hambre > 100:
                self.hambre = 100
            print(self.imagen_feliz)
            print(self.nombre, "está jugando. ¡Se divierte mucho!")
 
        else:
            print(self.imagen_disgustado)
            print(self.nombre, "no puede jugar, tiene hambre")

    def estado_animo(self):
        #seteando felicidad
        self.felicidad -= 5
        if self.felicidad < 0:
            self.felicidad = 0
        #seteando hambre
        self.hambre += 5
        if self.hambre > 100:
            self.hambre = 100
        
        if self.hambre >= 70 and self.felicidad <= 50:
            print(self.imagen_muerto)
            print(self.nombre, "está muy hambriento y triste. ¡Necesita comida y atención!")
        elif self.hambre >= 70:
            print(self.imagen_disgustado)
            print(self.nombre, "tiene mucha hambre. ¡Dale de comer!")
        elif self.felicidad <= 50:
            print(self.imagen_triste)
            print(self.nombre, "está triste. ¡Juega con él para alegrarlo!")
        else:
            print(self.imagen_feliz)
            print(self.nombre, "está contento y satisfecho.")

    def presentacion(self):
        print(f"\n╔════════════════════════════════════╗\n║     Te presento a tu mascota!      ║\n╚════════════════════════════════════╝\n{self.imagen}\tSu nombre es {self.nombre}")
        
    def despedida(self):
        print(f"\n╔════════════════════════════════════╗\n║             Nos vemos!             ║\n╚════════════════════════════════════╝{self.imagen}╔════════════════════════════════════╗\n║        Jueguemos otro día!         ║\n╚════════════════════════════════════╝\n")

 
 
# Crear una instancia de MascotaVirtual

interfaz_inicio = '\n╔════════════════════════════════════╗\n║       Bienvenido a tu primer       ║\n║          mascota virtual!          ║\n╚════════════════════════════════════╝\n'
interfaz_juego = '\n╔════════════════════════════════════╗\n║       Opciones disponibles:        ║\n║                                    ║\n║ 1 - Alimentar                      ║\n║ 2 - Jugar                          ║\n║ 3 - Mostrar informacion            ║\n║ 4 - Salir                          ║\n║                                    ║\n╚════════════════════════════════════╝\n'
print(interfaz_inicio)
nombre = input("Elige un nombre para tu mascota: ")
mascota = MascotaVirtual(nombre)
mascota.presentacion()


""" for _ in range(8):
    mascota.alimentar()
    mascota.jugar()
    mascota.estado_animo()
    mascota.estado_animo()
    mascota.estado_animo()
    mascota.estado_animo()
 """

while True:
    print(interfaz_juego)
    op = int(input("Elija una opcion: "))
    if op==1:
        mascota.alimentar()
    elif op== 2:
        mascota.jugar()
    elif op==3:
        mascota.estado_animo()
    elif op==4:
        mascota.despedida()
        break