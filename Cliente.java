package DIAGRAMAS_UML;
import java.util.ArrayList;
public class Cliente {
    String nombre;
    int cedula;
    String fechaNac;
    ArrayList<Animal> listaAnimales= new ArrayList<>();

    public Cliente(String nombre, int cedula, String fechaNac) {
        this.nombre= nombre;
        this.cedula= cedula;
        this.fechaNac= fechaNac;
    }

    public void agendarCita(Animal animal, String fecha, Veterinario vet, String motivo) {
        Cita cita = new Cita(fecha, animal, vet, this, motivo);
        cita.mostrarDetalle();
        vet.atenderCita(cita);
    } 
}
