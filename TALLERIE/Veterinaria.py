
class Animal: #Se define una clase base llama animal
    def __init__(self, nombre, edad, especie, raza, carnet): #def define una funcion y el init es función especial que se ejecuta automaticamente cuando se crea. Las dos conforman el metodo constructor. Lo que esta dentro del parentesis son los atributos del objeto
        self.nombre= nombre #self representa en estas lineas el animal que estoy creado
        self.edad= edad #self.edad guarda la informacion dentro del animal
        self.especie= especie #=especie toma la entrada de dato y la guarda tambien
        self.raza= raza
        self.carnet= carnet

    def mostrar_info(self): #Se crea el metodo/accion de la clase y aparte se muestra la informacion del animal
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Especie: {self.especie}, Raza: {self.raza}, Carnet: {self.carnet}")#imprime la informacion guardada anteriormente

    def emitir_sonido(self): #Se crea un segunto metodo de la clase pero esta vez para el sonido que haga el animal
        print("Sonido del animal")

# Clase Perro hereda de Animal. Una Subclase
class Perro(Animal): #Con esta linea marcamos que el Perro es un animal pero con diferencias.
    def emitir_sonido(self):
        print("Guau!") #Modificamos el metodo de sonido y ingresamos el ladrido.

#Lo mismo con la subclase Gato.
class Gato(Animal):
    def emitir_sonido(self):
        print("Miau!")

class Veterinario: #Se crea la clase para representar a los veterinarios
    def __init__(self, nombre, especialidad, num_id, fecha_nac): #Constructor que guarda los datos del veterinario.
        self.nombre= nombre
        self.especialidad= especialidad #Guarda cada dato dentro del objeto veterinario.
        self.num_id= num_id
        self.fecha_nac= fecha_nac

    def mostrar_info(self): #Muestra los datos del veterinario mediante el metodo de la clase y el objeto
        print(f"Nombre: {self.nombre}, Especialidad: {self.especialidad}, ID: {self.num_id}, Fecha Nac: {self.fecha_nac}")

    def atender_cita(self, cita): #Crea un metodo que atienda la cita y se manda a llamar al animal mediante la clase CITA
        print(f"El veterinario {self.nombre} está atendiendo la cita del animal {cita.animal.nombre}.")

class Cliente:
    def __init__(self, nombre, cedula, fecha_nac): #Volvemos a construir un espacio para guardar los datos de los clientes.
        self.nombre= nombre #Guarda cada dato dentro del objeto
        self.cedula= cedula
        self.fecha_nac= fecha_nac
        self.lista_animales= [] #- crea una lista vacía para guardar sus animales para hacer el ejemplo del Polimorfismo

    def agendar_cita(self, animal, fecha, veterinario, motivo): #Esta función sirve para crear una cita mediante la creación del metodo de agendar cita.
        cita= Cita(fecha, animal, veterinario, self, motivo) #Se crea una variable con el nombre de cita con los datos a pedir
        cita.mostrar_detalle() #Muestra la cita y hace que el veterinario la atienda.
        veterinario.atender_cita(cita)

class Cita: #Se crea la clase Cita
    def __init__(self, fecha, animal, veterinario, cliente, motivo): #Se construye el espacio para guardar los datos de la cita
        self.fecha= fecha #Guarda todos los datos de la cita.
        self.animal= animal
        self.veterinario= veterinario
        self.cliente= cliente
        self.motivo= motivo

    def mostrar_detalle(self):#Muestra toda la información de la cita.
        print("""-------- FACTURA DE AGENDACION DE CITA VETERINARIA LABUENA --------""")
        print(f"Cita Agendada el dia {self.fecha} para {self.animal.nombre} (Carnet: {self.animal.carnet}) con el veterinario {self.veterinario.nombre}.")
        print(f"al nombre del cliente {self.cliente.nombre} con la Cédula {self.cliente.cedula}  y con Motivo de {self.motivo}")

print ("""... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...
       ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...""")

animal1 = Gato("Lola", 4, "Gato", "Siames", "24-C98") #Se crea una variable para el primer animal con los datos en orden de creación.
animal2 = Perro("Juan", 4, "Perro", "Pastor Alemán", "33-C12") #Lo mismo aqui

cliente1 = Cliente("Ana Domínguez", 52345932, "30/08/1997") #Lo mismo pero con los datos de cliente.
cliente1.lista_animales.append(animal1) #Esta linea lo que hace es agregar los animales a la lista personal del cliente que se mando a llamar.
cliente1.lista_animales.append(animal2) #Lo mismo

vet1 = Veterinario("Andrés López", "Medicina Felina y Canina", 45672344, "23/08/1976") #Se llenan los datos del veterinario.

# Polimorfismo: mismo método, diferentes sonidos
for animal in cliente1.lista_animales: #Recorre cada animal que tiene el cliente1 en su lista
    animal.mostrar_info() #Muestra los datos de los animales
    animal.emitir_sonido() #Muestra el sonido que hace.


cliente1.agendar_cita(animal1, "26/08/2025", vet1, "Chequeo general") #Aqui se hace uso de la función del cliente 'agendar' una cita a el animal1 del cliente1 al veterinario1
#Fin.