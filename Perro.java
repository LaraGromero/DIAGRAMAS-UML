package DIAGRAMAS_UML;
public class Perro extends Animal {
    public Perro(String nombre, int edad, String especie, String raza, String carnet) {
        super(nombre, edad, especie, raza, carnet); // llama al constructor de Animal
    }

    @Override
    public void emitirSonido() {
        System.out.println("Guau!");
    }
}