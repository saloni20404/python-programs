# Program to generate the first n numbers in the Fibonacci sequence
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print("The Fibonacci sequence is:", fibonacci(n))
