#WAP to compute the Sum of the Series 4 + 8 + 12 + … + 40
sum_series = 0
for num in range(4, 41, 4):
    sum_series += num

print("Sum of the series:", sum_series)
