package DIAGRAMAS_UML;
class Gato extends Animal {
    public Gato(String nombre, int edad, String especie, String raza, String carnet) {
        super(nombre, edad, especie, raza, carnet);
    }

    @Override
    public void emitirSonido() {
        System.out.println("Miau!");
    }
}
