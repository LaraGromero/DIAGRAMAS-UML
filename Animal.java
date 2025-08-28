package DIAGRAMAS_UML;
public class Animal {
    String nombre;
    int edad;
    String especie;
    String raza;
    String carnet;

    // Constructor
    public Animal(String nombre, int edad, String especie, String raza, String carnet) {
        this.nombre= nombre;
        this.edad= edad;
        this.especie= especie;
        this.raza= raza;
        this.carnet= carnet;
    }

    // Método para mostrar información
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre + ", Edad: " + edad + ", Especie: " + especie + ", Raza: " + raza + ", Carnet: " + carnet);
    }

    // Método para emitir sonido
    public void emitirSonido() {
        System.out.println("Sonido del animal");
    }
}
