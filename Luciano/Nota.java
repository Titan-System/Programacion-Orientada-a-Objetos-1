public class Nota {
     
    private double ValorInicial;

    public Nota(double ValorInicial) 
    {
        this.ValorInicial=ValorInicial;
    }   

    public double obtenervalor()
    {
        return ValorInicial;
    }

    public void aprobado(){
        if (this.ValorInicial>=4) {
            System.out.println("Aprobado: "+this.ValorInicial);
        }else{}
    }
    
    public void desaprobado(){
        if (this.ValorInicial<4) {
            System.out.println("desaprobado: "+this.ValorInicial);
        }else{}
    }

    
    public void Recuperar(double Nuevo_valor)
    {
        if (this.ValorInicial<Nuevo_valor) {
            this.ValorInicial=Nuevo_valor;
        }
        else{}
    }

    public static void main(String[] args) {
        Nota alumno=new Nota(1);

        System.out.println(alumno.obtenervalor());
        alumno.aprobado();
        alumno.desaprobado();
        alumno.Recuperar(4);


        System.out.println(alumno.obtenervalor());
        alumno.aprobado();
        alumno.desaprobado();


    }
}
