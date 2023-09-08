



def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1

    while a <= n:
        fibonacci_series.append(a)
        a, b = b, a + b

    return fibonacci_series