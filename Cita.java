package DIAGRAMAS_UML;
public class Cita {
        String fecha;
    Animal animal;
    Veterinario veterinario;
    Cliente cliente;
    String motivo;

    public Cita(String fecha, Animal animal, Veterinario veterinario, Cliente cliente, String motivo) {
        this.fecha = fecha;
        this.animal = animal;
        this.veterinario = veterinario;
        this.cliente = cliente;
        this.motivo = motivo;
    }

    public void mostrarDetalle() {
        System.out.println("-------- FACTURA DE AGENDACION DE CITA VETERINARIA LABUENA --------");
        System.out.println("Cita Agendada el dia " + fecha + " para " + animal.nombre + " (Carnet: " + animal.carnet + ") con el veterinario " + veterinario.nombre);
        System.out.println("al nombre del cliente " + cliente.nombre + " con la Cédula " + cliente.cedula + " y con Motivo de " + motivo);
    }
}
