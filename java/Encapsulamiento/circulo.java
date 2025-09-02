public class circulo {
    
    
    private punto punto;
    private double R;

    public circulo(double D, double A){
        this.punto = new punto(D, A);
        this.R = Math.sqrt(Math.pow(D, 2)+Math.pow(A,2));
    }

    // 

    public void MoverCirculo(double A, double v){
        punto.Moverpunto(A, v);
    }

    public void ubicacion(){
        System.out.println("X: "+punto.getX()+"\n"+"Y: "+punto.getY());
    }

    public double Radio()
    {
        return R= Math.sqrt(Math.pow(punto.getX(), 2)+Math.pow(punto.getY(),2));
    }

    public double Diametro(){
        return 2*Radio();
    }
    
    public double Perimetro(){
        return 2*Math.PI*Radio();
    }
    public double Area(){
        return Math.PI*Math.pow(Radio(), 2);
    }

    public static void main(String[] args) {
        circulo redondo= new circulo(2,1);

        System.out.println("Radio: " + redondo.Radio());
        System.out.println("Diámetro: " + redondo.Diametro());
        System.out.println("Perímetro: " + redondo.Perimetro());
        System.out.println("Área: " + redondo.Area());

        // mover el círculo
        redondo.MoverCirculo(5, 5);
        redondo.ubicacion();

    }
}