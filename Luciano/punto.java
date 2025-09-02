public class punto {

    private double X;
    private double Y;
    private double distancias;

    public punto(double x, double y)
    {   
        this.X=x;
        this.Y=y;
    }

    public double getX() {
        return X;
    }

    public double getY() {
        return Y;
    }

    public void setX(double x) {
        X = x;
    }
    
    public void setY(double y) {
        Y = y;
    }

    public void Moverpunto(double x, double y){
        this.X=x;
        this.Y=y;
    }

// 
    public boolean SobreElEjeX(){

        return this.Y==0;
    }

    public boolean SobreElEjeY(){
        return this.X==0;
    }

    public boolean ElOrigenDeCoordenadas(){
        return this.X==0 && this.Y==0;
    }
    
    public double distancia (double p1, double p2){
        return this.distancias = Math.sqrt(Math.pow(p1, 2)+Math.pow(p2,2));
    }
//

    public static void main(String[] args) {

        punto punto=new punto(2,45);
        
        punto.Moverpunto(3, 2);
    
        System.out.println("X :"+punto.SobreElEjeX());
        System.out.println("Y :"+punto.SobreElEjeY());
        System.out.println("Esta en el origen de la cordenada?: "+punto.ElOrigenDeCoordenadas());
        
        System.out.println("Distancia al origen: "+punto.distancia(punto.getX(),punto.getY()));


    }
}
