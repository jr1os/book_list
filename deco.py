def validar(f):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError("numeros negativos")
        return f(x, y)
    return valida


@validar
def soma(num1, num2):
    return num1 + num2


print(soma(2, 6))
