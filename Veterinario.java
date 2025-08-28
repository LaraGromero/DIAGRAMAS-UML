package DIAGRAMAS_UML;
public class Veterinario {
    String nombre;
    String especialidad;
    int numId;
    String fechaNac;

    public Veterinario(String nombre, String especialidad, int numId, String fechaNac) {
        this.nombre= nombre;
        this.especialidad= especialidad;
        this.numId= numId;
        this.fechaNac= fechaNac;
    }

    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre + ", Especialidad: " + especialidad + ", ID: " + numId + ", Fecha Nac: " + fechaNac);
    }

    public void atenderCita(Cita cita) {
        System.out.println("El veterinario " + nombre + " está atendiendo la cita del animal " + cita.animal.nombre);
    }
}
