class Polynomial:
    def __init__(self, coefficients):
        # Inicializa el polinomio con una lista de coeficientes
        self.coefficients = coefficients

    def __str__(self):
        # Crea una representación en cadena del polinomio
        terms = [
            # Construye cada término del polinomio
            f"{coeff}x^{power}" if power != 0 else f"{coeff}"
            for power, coeff in enumerate(self.coefficients) if coeff
        ]
        # Une los términos en orden inverso y reemplaza '1x' por 'x'
        return " + ".join(terms[::-1]).replace(' 1x', ' x')

    def __add__(self, other):
        # Realiza la suma de dos polinomios
        result = [
            # Suma los coeficientes correspondientes de ambos polinomios
            (self.coefficients[i] if i < len(self.coefficients) else 0) +
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max(len(self.coefficients), len(other.coefficients)))
        ]
        return Polynomial(result)

    def __sub__(self, other):
        # Realiza la resta de dos polinomios
        result = [
            # Resta los coeficientes correspondientes de ambos polinomios
            (self.coefficients[i] if i < len(self.coefficients) else 0) -
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max(len(self.coefficients), len(other.coefficients)))
        ]
        return Polynomial(result)
    
    def __mul__(self, other):
        # Realiza la multiplicación de dos polinomios
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for self_power, self_coeff in enumerate(self.coefficients):
            for other_power, other_coeff in enumerate(other.coefficients):
                # Multiplica y suma los términos correspondientes
                result[self_power + other_power] += self_coeff * other_coeff
        return Polynomial(result)

# Ejemplo de uso
poly1 = Polynomial([1, 2, 3])  # Representa 3x^2 + 2x + 1
poly2 = Polynomial([3, 4])     # Representa 4x + 3

print("Poly1:", poly1)         # Imprime Poly1: 3x^2 + 2x + 1
print("Poly2:", poly2)         # Imprime Poly2: 4x + 3

sum_poly = poly1 + poly2       # Suma de poly1 y poly2
print("Suma:", sum_poly)       # Imprime Suma: 3x^2 + 6x + 4

diff_poly = poly1 - poly2      # Resta de poly1 y poly2
print("Diferencia:", diff_poly) # Imprime Diferencia: 3x^2 - 2x - 2

product_poly = poly1 * poly2   # Producto de poly1 y poly2
print("Producto:", product_poly) # Imprime Producto: 12x^3 + 17x^2 + 10x + 3