"""Factorial.py"""


class FactorialCalculator:
    """Clase Factorial"""

    def factorial(self, n):
        """Metode Factorial"""
        if not isinstance(n, int):
            raise TypeError("El factorial només es pot calcular per enters")
        if n < 0:
            raise ValueError("El factorial no està definit per a enters negatius")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def more(self, n):
        """Funcio per a que no me diga que falta un public method"""


if __name__ == "__main__":
    calculator = FactorialCalculator()
    num = int(input("Introdueix un nombre per calcular el seu factorial: "))
    try:
        print("El factorial de", num, "és:", calculator.factorial(num))
    except (TypeError, ValueError) as e:
        print("Error:", e)
