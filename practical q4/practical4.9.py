#WAP to compute Sum of the series 3 + 6 + 9 + … + 30
sum_series = 0
for num in range(3, 31, 3):
    sum_series += num
print("Sum of the series:", sum_series)
