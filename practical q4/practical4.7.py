#WAP that prints multiplication table of a umber using for loop.
num = int(input("Enter the number: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
