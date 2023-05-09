class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))
        self.genero = input("Ingrese el género: ")
        self.altura = float(input("Ingrese la altura en metros: "))

    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nGénero: {self.genero}\nAltura: {self.altura} m"

if __name__ == "__main__":
    persona = Persona()
    print(persona)
