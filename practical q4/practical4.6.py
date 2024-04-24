#Write a program to display the Fibonacci sequences up to
#nth term where n is provided by the user.
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
