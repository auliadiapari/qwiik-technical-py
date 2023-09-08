



from fibonacci_logic import generate_fibonacci

def main():
    n = int(input("Enter a number: "))
    fibonacci_series = generate_fibonacci_series(n)
    print("Fibonacci series up to", n, "is:", fibonacci_series)

if __name__ == "__main__":
    main()