package java.basicos;
public class alumno
{
    String nombre;
    int edad;
    double promedio;
    alumno()
    {
        System.out.println("Soy el Constructor");
    }
    public void darExamen()
    {
        System.out.println("Alumno da examen");
    }
    public static void main(String[] args)
    {
        alumno alu1=new alumno();
        //system.out.println(alu1.);
        alu1.darExamen();
        
    }
}