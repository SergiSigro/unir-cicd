import app
import app.util
import math  # Importamos la librería math para la función de logaritmo y raíz cuadrada


class InvalidPermissions(Exception):
    """Excepción personalizada para permisos inválidos."""
    pass


class Calculator:
    def add(self, x, y):
        self.check_permissions(f"{x} + {y}")
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_permissions(f"{x} - {y}")
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        self.check_permissions(f"{x} * {y}")
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_permissions(f"{x} / {y}")
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_permissions(f"{x} ** {y}")
        self.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        self.check_permissions(f"sqrt({x})")
        self.check_type(x)
        if x < 0:
            raise TypeError("Cannot compute the square root of a negative number")
        return math.sqrt(x)

    def log10(self, x):
        self.check_permissions(f"log10({x})")
        self.check_type(x)
        if x <= 0:
            raise TypeError("Logarithm undefined for non-positive values")
        return math.log10(x)

    def check_permissions(self, operation):
        if not app.util.validate_permissions(operation, "user1"):
            raise InvalidPermissions('User has no permissions')

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_type(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("Parameter must be a number")

if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
