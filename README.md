# Programacion-Orientada-a-Objetos-1

POO – Preguntas Generales

¿Cómo se define un programa dentro de POO? Describir sus elementos generales.

    Un programa OO es un conjunto de clases que, en ejecución, producen una población de objetos que colaboran enviándose mensajes. Elementos típicos:
    
    Clases/Interfaces (o protocolos) con atributos y métodos.
    
    Relaciones: asociaciones, dependencias, herencia, composición/agregación.
    
    Mensajes entre objetos (invocaciones) que modifican estado y disparan comportamientos.
    
    Módulos/paquetes que agrupan clases; invariantes y contratos que gobiernan su uso.
    
    Punto de entrada (p. ej., main o script) que construye el grafo inicial de objetos y orquesta el flujo.
    En Python: módulos/paquetes, clases, instancias, y un script ejecutable que inicia las interacciones.

¿Qué es la Programación Orientada a Objetos (POO)?

    Un paradigma que modela el software como objetos con estado (atributos) y comportamiento (métodos)
    organizados en clases. Favorece modularidad, reutilización y mantenimiento.
¿Qué es una clase?

    Un molde/plantilla que define atributos y métodos los cuales al Instanciarlos  crea objetos que comparten esa
    definición es decir comparten mismos atributos y muismos metodos.
¿Qué es un objeto?

       un onjeto es la instancia de una clase la cual comparte sus atributos y sus metodos sin embargo el objeto es dinamico mientras que la clase es estatica  
       
<img width="1023" height="643" alt="image" src="https://github.com/user-attachments/assets/5eada6d8-1a5d-48c5-89ff-cc924fc7dab5" />

        en la foto de arriba podemos observar como al momento de crear un objeto de determinada clase se crea un llamado al sistema que  direcciona a las celdas de la virtual table de esa clase 


¿Cuáles son las similitudes y diferencias entre composición y agregación? Da ejemplos.

    Similitud: ambas son relaciones parte–de (asociaciones estructurales).
    
    Diferencias clave:
    
    Propiedad del ciclo de vida:
    
    Composición: el todo es dueño de las partes. Si el todo se destruye, las partes también. Fuerte.
    
    Agregación: el todo no es dueño de las partes; las partes pueden vivir por sí mismas. Débil.
    
    Notación UML:
    
    Composición: rombo relleno en el lado del todo.
    
    Agregación: rombo hueco en el lado del todo.
    
    Ejemplos:
    
    Composición: Pedido–LíneaDePedido; Casa–Habitación; Auto–Motor.
    
    Agregación: Equipo–Jugador; Curso–Estudiante; Biblioteca–Libro (el libro puede existir sin esa biblioteca).
    
    Implementación práctica: en composición el todo crea/gestiona las partes y no las comparte ampliamente; en agregación las partes pueden compartirse o existir independientemente.

¿Cuál es la diferencia entre mensaje y método?

    Mensaje: la solicitud que un objeto A le envía a un objeto B para que ejecute una operación (nombre + argumentos). Ej.: b.dibujar(x, y).
    
    Método: la implementación concreta en la clase de B que responde a ese mensaje.
    Al enviar un mensaje, el sistema selecciona el método a ejecutar (despacho) según el tipo dinámico del receptor → base del polimorfismo.

¿Un objeto es una entidad estática o dinámica?

    Dinámica: su estado puede cambiar en tiempo de ejecución a través de sus métodos.
    Diferencia entre programación orientada a objetos y no orientada a objetos
    POO organiza en clases/objetos, encapsula datos y usa herencia/polimorfismo. La no-OO (p. ej.,
    procedimental) organiza en funciones y estructuras separadas, con menor unión entre datos y lógica.
    Características de un programa orientado a objetos
    Abstracción, encapsulamiento, herencia, polimorfismo, modularidad, reutilización, mensajes entre
    objetos y separación interfaz/implementación.
¿Qué es el estado del objeto?

    El conjunto de valores actuales de sus atributos; cambia cuando se invocan métodos que los modifican.
¿Qué es un diagrama de clases?

    Diagrama UML O UNIFIED MODELING LANGUAGE que muestra clases, atributos, métodos y relaciones (asociación, herencia, composición,
    etc.). Es la vista estática del modelo.
¿Cuáles son las relaciones entre clases (UML, a alto nivel)?

    Asociación (conoce/usa), Dependencia (usa puntualmente), Agregación (tiene un, parte–todo débil),
    Composición (está compuesto por, parte–todo fuerte), Generalización/Herencia (es un/una), Realización
    (implementa una interfaz).
<img width="1019" height="455" alt="image" src="https://github.com/user-attachments/assets/c0207bd4-b2a7-4815-8f78-77612ac25728" />
<img width="1024" height="485" alt="image" src="https://github.com/user-attachments/assets/556cf4b3-bd88-46e2-b61a-da9da8d66857" />
<img width="1016" height="440" alt="image" src="https://github.com/user-attachments/assets/7834446e-bb00-4d3f-82e3-cb8b783f6eea" />
<img width="1023" height="757" alt="image" src="https://github.com/user-attachments/assets/9354d74a-b022-4ae6-b654-4daf1241b2c2" />

    
¿Cómo representarías agregación y composición en un diagrama de clases?

    Agregación: rombo hueco en el lado del 'todo' (las partes pueden vivir sin él). Composición: rombo
    relleno en el lado del 'todo' (el todo es dueño del ciclo de vida de las partes). Indicar multiplicidades y
    roles según corresponda.
    
    
Encapsulamiento

<img width="561" height="567" alt="image" src="https://github.com/user-attachments/assets/28a5a2e8-bab2-4f78-ba87-a8769429ec1f" />


¿Qué es el encapsulamiento?

    Ocultar la implementación interna y exponer una interfaz pública segura. Protege invariantes y reduce el
    acoplamiento.
¿Qué son los atributos de un objeto?

    Datos/propiedades que describen su estado; en Python suelen inicializarse en __init__.
¿Qué son los métodos definidos en las clases?

    Funciones asociadas a la clase/objeto que operan sobre su estado o colaboran con otros objetos.
¿Qué es un constructor?

    Método especial que inicializa el objeto. En Python es __init__(self, ...), que prepara el estado de la
    instancia recién creada.
    Características de un constructor comparado con otros métodos
    Se ejecuta automáticamente al instanciar, no retorna valores arbitrarios (el 'resultado' es la instancia
    inicializada) y suele garantizar invariantes. Otros métodos se invocan explícitamente y pueden devolver
    cualquier valor.
¿Cómo declaro un método o atributo privado en Python?

    Python usa convención y name mangling: _nombre (uso interno/protegido) y __nombre (se renombra a
    _Clase__nombre). No hay privacidad dura como en Java/C#.
¿Dentro del main puedo acceder a un atributo privado? Si no, ¿cómo lo hago?

    La buena práctica es no acceder directamente. Usar métodos públicos o propiedades que controlen la
    lectura/escritura. Aunque se puede usar _Clase__nombre, no es recomendable.

<img width="893" height="821" alt="image" src="https://github.com/user-attachments/assets/b59c264d-e424-470d-92ea-531851631743" />

¿Qué maneras hay de hacer getter y setter en Python?

    Métodos explícitos get_x/set_x; propiedades con @property y @x.setter (idiomático); o la función
    integrada property().
<img width="624" height="319" alt="image" src="https://github.com/user-attachments/assets/08d3b43c-de7a-4d87-aabb-61ec70cc6c49" />

Herencia 

<img width="539" height="462" alt="image" src="https://github.com/user-attachments/assets/8f781949-f52a-49b6-ad4c-c76a5e2cfa40" />


    
¿Cómo funciona la herencia?

    Una subclase reutiliza y especializa una superclase: hereda atributos y métodos, y puede añadir o
    sobrescribir comportamiento.
¿Cuándo conviene usar herencia?

    Cuando hay una relación 'es un(a)' estable y se busca reutilizar comportamiento común. Para 'tiene
    un(a)' conviene composición.
¿Qué pasa con constructores en la herencia (Python)?

    La subclase puede definir su __init__ y llamar al de la superclase con super().__init__(...) para inicializar
    la parte base.
¿Qué problemas puede traer la herencia mal usada?

    Árboles rígidos, acoplamiento fuerte, fragilidad ante cambios y confusión (especialmente con herencia
    múltiple mal diseñada).
¿Qué es una clase abstracta? ¿Cómo se simula en Python?

    Clase que no puede instanciarse y que define operaciones que las subclases deben implementar. En
    Python: usar ABC y @abstractmethod del módulo abc; alternativamente, typing.Protocol para
    polimorfismo estructural.
    
Polimorfismo

<img width="530" height="443" alt="image" src="https://github.com/user-attachments/assets/b87e1a18-ab14-4e52-9019-a598b0cf74fb" />


¿Cómo funciona el polimorfismo?

    Permite invocar la misma operación sobre objetos de tipos distintos y que cada uno responda según su
    implementación. En Python es dinámico.
¿Para qué se usa el polimorfismo?

    Para desacoplar el código del tipo concreto, habilitar extensibilidad y simplificar diseños (colecciones
    heterogéneas con interfaz común).
    Formas comunes de polimorfismo
    Por subtipo (sobrescritura), por interfaces/protocolos, duck typing (Python) y sobrecarga (típica en
    Java/C#, no en Python).
¿Sobrecarga vs sobrescritura de métodos?

    Sobrecarga: mismo nombre, distinta firma en la misma clase; el sistema elige por parámetros/tipos.
    Python no la soporta de forma nativa: se simula con parámetros opcionales, *args/**kwargs o
    functools.singledispatch. Sobrescritura: una subclase redefine un método de la superclase manteniendo
    el contrato; puede invocar super() para extender.

¿Qué es unittest? 

    unittest es el módulo de pruebas unitarias de Python, usado para verificar el correcto funcionamiento de partes específicas del código             (funciones, clases, métodos).

¿Receta?

<img width="349" height="276" alt="image" src="https://github.com/user-attachments/assets/1c7a5213-68c9-496e-a9c5-2f327947dea4" />

Diferencia entre sobreescritura parcial y total (con ejemplos)

    Sobreescritura total: la subclase reemplaza completamente el método heredado.
    
    Sobreescritura parcial: la subclase modifica el método pero reutiliza parte del original (usando super()).

<img width="332" height="303" alt="image" src="https://github.com/user-attachments/assets/8212fa66-a843-4d38-88c3-e650dbd91040" />

¿Qué es una clase abstracta?

    Una clase abstracta es una clase especial que sirve como modelo o plantilla base para otras clases. Se define para establecer una interfaz  común, pero no está pensada para ser utilizada directamente (es decir, no se puede instanciar por sí sola).
    
    Su propósito es forzar a las subclases a implementar ciertos métodos, asegurando que todas las clases derivadas compartan una estructura  mínima.

<img width="437" height="384" alt="image" src="https://github.com/user-attachments/assets/9c3472c3-9cdf-4297-a02f-338182e71436" />


Cual es la diferencia entre clase abstracta y clase común?

    Clase Abstracta	                                Clase Común
                                                    
    No se puede instanciar	                        Se puede instanciar
    Contiene métodos abstractos	                    Todos los métodos están definidos
    Se usa como plantilla para herencia	            Puede ser usada directamente
    
¿Qué es el late binding?    

    Es el enlace tardío (o despacho dinámico) de una llamada a método: la selección del método concreto se resuelve en tiempo de ejecución según  el tipo dinámico del objeto receptor.
    
    Para qué sirve: habilita polimorfismo real (mismo mensaje, respuestas distintas).
    
    En Python: el despacho de métodos es dinámico por defecto. (Nota: “late binding” también puede referir, en otro contexto de Python, a la captura tardía de variables en closures; aquí hablamos del despacho de métodos.)

<img width="885" height="717" alt="image" src="https://github.com/user-attachments/assets/949864d8-772f-40b7-b6ae-b8ee635ef1f0" />

