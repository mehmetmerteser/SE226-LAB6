from math import pi

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)

term = lambda x, i: ((-1) ** i) * ((x ** (2 * i + 1)) / factorial(2 * i + 1))

def sine_x(x, n):
    x = x * pi / 180
    result = 0
    for i in range(n):
        result += term(x, i)
    return result

result = 0

def recursive_sum(n):
    global result
    if n == 0:
        return
    result += n
    recursive_sum(n - 1)

if __name__ == "__main__":
    x_fact = int(input("Faktöriyel hesaplamak için x girin: "))
    print(f"{x_fact}! =", factorial(x_fact))

    x_sin = float(input("\nsin(x) için x açısını (derece): "))
    n_sin = int(input("sin(x) için terim sayısını girin (n): "))
    print(f"sin({x_sin}°) ≈", sine_x(x_sin, n_sin))

    n_sum = int(input("\nToplam için n girin: "))
    result = 0
    recursive_sum(n_sum)
    print(f"1'den {n_sum}'e kadar toplam:", result)
