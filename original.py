class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # lista de coeficientes

    def __str__(self):
        terms = []  # lista para almacenar los términos del polinomio
        for power, coeff in enumerate(self.coefficients):  # iterar sobre los coeficientes y sus índices
            if coeff:  # si el coeficiente no es cero
                terms.append(f"{coeff}x^{power}")  # agregar el término como cadena a la lista
        # unir los términos en orden inverso, reemplazar 'x^0' por '', y '1x' por 'x'
        return " + ".join(terms[::-1]).replace('x^0', '').replace('1x', 'x')

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))  # longitud máxima de los dos polinomios
        result = [0] * max_len  # lista de ceros para almacenar los coeficientes del polinomio resultante
        for i in range(max_len):  # iterar hasta la longitud máxima
            if i < len(self.coefficients):  # si el índice es menor que la longitud del primer polinomio
                result[i] += self.coefficients[i]  # sumar el coeficiente correspondiente del primer polinomio
            if i < len(other.coefficients):  # si el índice es menor que la longitud del segundo polinomio
                result[i] += other.coefficients[i]  # sumar el coeficiente correspondiente del segundo polinomio
        return Polynomial(result)  # devolver un nuevo polinomio con los coeficientes resultantes

    def __sub__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))  # longitud máxima de los dos polinomios
        result = [0] * max_len  # lista de ceros para almacenar los coeficientes del polinomio resultante
        for i in range(max_len):  # iterar hasta la longitud máxima
            if i < len(self.coefficients):  # si el índice es menor que la longitud del primer polinomio
                result[i] += self.coefficients[i]  # sumar el coeficiente correspondiente del primer polinomio
            if i < len(other.coefficients):  # si el índice es menor que la longitud del segundo polinomio
                result[i] -= other.coefficients[i]  # restar el coeficiente correspondiente del segundo polinomio
        return Polynomial(result)  # devolver un nuevo polinomio con los coeficientes resultantes
    
    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)  # lista de ceros para el polinomio resultante
        for self_power, self_coeff in enumerate(self.coefficients):  # iterar sobre los coeficientes del primer polinomio
            for other_power, other_coeff in enumerate(other.coefficients):  # iterar sobre los coeficientes del segundo polinomio
                result[self_power + other_power] += self_coeff * other_coeff  # multiplicar y sumar los términos correspondientes
        return Polynomial(result)  # devolver un nuevo polinomio con los coeficientes resultantes
    
# Ejemplo de uso
poly1 = Polynomial([1, 2, 3])  # Representa 3x^2 + 2x + 1
poly2 = Polynomial([3, 4])     # Representa 4x + 3

print("Poly1:", poly1)  # Imprimir el primer polinomio
print("Poly2:", poly2)  # Imprimir el segundo polinomio

sum_poly = poly1 + poly2
print("Sum:", sum_poly)  # Imprimir la suma de los dos polinomios

diff_poly = poly1 - poly2
print("Difference:", diff_poly)  # Imprimir la resta de los dos polinomios

product_poly = poly1 * poly2
print("Product:", product_poly)  # Imprimir la multiplicación de los dos polinomios