public class Personas {


    private int edad;
    private String nombre;

    public Personas()
    {
        this.edad=0;
        this.nombre="";
    }

    public void setNombre(String nombre)
    {
        this.nombre=nombre;
    }

    public String getNombre()
    {
        return this.nombre;
    }


    public void setedad(int edad)
    {
        this.edad=edad;
    }

    public int getedad()
    {
        return edad;
    }


    public void cumpleanos()
    {   
        System.out.println(getNombre());
        System.out.println(getedad());
        this.edad+=1;
        
    }

    public static void main(String[] args) {
        Personas chico= new Personas();

        chico.setNombre("luciano");
        chico.setedad(22);

        System.out.println(chico.getNombre());
        System.out.println(chico.getedad());

        chico.cumpleanos();
        chico.cumpleanos();
        chico.cumpleanos();
        chico.cumpleanos();



    }

}
