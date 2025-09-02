import java.util.Scanner;

public class Calculadora {

    private double a;
    private double b;

    public Calculadora()
    {
        this.a=0;
        this.b=0;
    }

    public void setA(double a) {
        this.a = a;
    }

    public void setB(double b) {
        this.b = b;
    }

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }
// 

    public void suma(){
        System.out.println("suma: "+(a+b));

    }

    public void resta(){
        System.out.println("resta: "+(a-b));

    }

    public void division(){      
        System.out.println("division: "+(a/b));

    }


    public void multiplicacion(){
        System.out.println("multiplicacion: "+(a*b));
    }

    public void potencia()
    {
        System.out.println("potencia: "+Math.pow(a, b));

    }
// 


    public void Init(){
        Scanner input=new Scanner(System.in);

        System.out.println("Ingrese el primer valor: ");
        setA(input.nextInt());

        System.out.println("Ingrese el segundo valor: ");
        setB(input.nextInt());
        System.out.println("\n");

    }



    public static void main(String[] args) {

        Calculadora calculo=new Calculadora();


        calculo.Init();


        calculo.suma();
        calculo.resta();
        calculo.multiplicacion();
        calculo.potencia();
        
        

    }

}
