#Pattern program in python to show patterns
n = 5  # Change the value of 'n' to adjust the size of the square

#for square
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#for right triangle
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

#inverted right triangle pattern
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#pyramid pattern 

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


#diamond pattern
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

#spiral
def print_spiral(n):
    for i in range(n):
        for j in range(i, n - i):
            print(i + 1, end=" ")
        for j in range(i + 1, n - i):
            print(n - i, end=" ")
        for j in range(i + 1, n - i):
            print(n - i, end=" ")
        for j in range(i + 1, n - i - 1):
            print(i + 1, end=" ")
        print()

print_spiral(n)

#arrow pattern
for i in range(n // 2):
    for j in range(i + 1):
        print("*", end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

#right angled pyramid pattern
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

#hollow square pattern
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
