class Perro:
    def _init_(self,): # Constructor en Python
        self.nombre=""
    def muestra(self):
        print(f"Soy {self.nombre}")    


# CONSTRUCTOR EN C#
"""
Class Perro{
    public string Nombre {get;set;}
    public Perro()
    {

    }
    public void Muestra()
    {
        Console.WriteLine("Soy{Nombre}")
    }
} 
"""

p = Perro()
p.nombre = "fido"
p.muestra()
