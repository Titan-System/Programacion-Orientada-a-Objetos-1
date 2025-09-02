public class Estudiante {

    private String nombre;
    private double nota;

    // Constructor vacío (inicializa valores por defecto)
    public Estudiante() {
        this.nombre = "Juan";
        this.nota = 6.5;
    }

    // Constructor con parámetros
    public Estudiante(String nombre, double nota) {
        this.nombre = nombre;
        this.nota = nota;
    }

    // Getters y Setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getNota() {
        return nota;
    }

    public void setNota(double nota) {
        this.nota = nota;
    }

    public void resulatdo()
    {
        if (getNota() >= 4) {
            System.out.println("aprobado");
        }
        else System.out.println("desaprobado");
    }


    public static void main(String[] args) {
            
        Estudiante alumno =new Estudiante();

        System.out.println(alumno.getNombre());
        System.out.println(alumno.getNota());

        alumno.setNombre("roberto");
        alumno.setNota(5);

        System.out.println(alumno.getNombre());

        alumno.resulatdo();
    }

}