def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero")

    return (base * altura) / 2

def area_circulo(radio):
    if radio <= 0:
        raise ValueError("El radio debe ser mayor que cero")

    return 3.1416 * (radio ** 2)

def area_rectangulo(base, altura):
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser mayores que cero")

    return base * altura
