package DIAGRAMAS_UML;
public class Main {
    public static void main(String[] args) {
        Gato animal1= new Gato("Lola", 4, "Gato", "Siames", "24-C98");
        Perro animal2= new Perro("Juan", 4, "Perro", "Pastor Alemán", "33-C12");

        Cliente cliente1= new Cliente("Ana Domínguez", 52345932, "30/08/1997");
        cliente1.listaAnimales.add(animal1);
        cliente1.listaAnimales.add(animal2);

        Veterinario vet1= new Veterinario(
            "Andrés López",
            "Medicina Felina y Canina",
            45672344,
            "23/08/1976"
        );

        for (Animal animal : cliente1.listaAnimales) {
            animal.mostrarInfo();
            animal.emitirSonido();
        }

        cliente1.agendarCita(
            animal1,
            "26/08/2025",
            vet1,
            "Chequeo general"
        );
    }
}

#PARA EJECUTAR java -cp . DIAGRAMAS_UML.Main
#javac -d . *.java 1