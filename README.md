# Programacion-Orientada-a-Objetos-1

POO – Preguntas Generales

¿Qué es la Programación Orientada a Objetos (POO)?

    Un paradigma que modela el software como objetos con estado (atributos) y comportamiento (métodos)
    organizados en clases. Favorece modularidad, reutilización y mantenimiento.
¿Qué es una clase?

    Un molde/plantilla que define atributos y métodos. Instanciar la clase crea objetos que comparten esa
    definición.
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

    Diagrama UML que muestra clases, atributos, métodos y relaciones (asociación, herencia, composición,
    etc.). Es la vista estática del modelo.
¿Cuáles son las relaciones entre clases (UML, a alto nivel)?

    Asociación (conoce/usa), Dependencia (usa puntualmente), Agregación (tiene un, parte–todo débil),
    Composición (está compuesto por, parte–todo fuerte), Generalización/Herencia (es un/una), Realización
    (implementa una interfaz).
¿Cómo representarías agregación y composición en un diagrama de clases?

    Agregación: rombo hueco en el lado del 'todo' (las partes pueden vivir sin él). Composición: rombo
    relleno en el lado del 'todo' (el todo es dueño del ciclo de vida de las partes). Indicar multiplicidades y
    roles según corresponda.
    
    
Encapsulamiento

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
¿Qué maneras hay de hacer getter y setter en Python?

    Métodos explícitos get_x/set_x; propiedades con @property y @x.setter (idiomático); o la función
    integrada property().
    
    Herencia 
    
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

¿Cómo funciona el polimorfismo?

    Permite invocar la misma operación sobre objetos de tipos distintos y que cada uno responda según su
    implementación. En Python es dinámico (duck typing).
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
