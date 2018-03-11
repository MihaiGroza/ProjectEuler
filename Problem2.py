# Building a Fibonacci sequence under 4 mil.

fibonacci = [1,2]

while fibonacci[-1] < 4000000:
    new_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(new_number)

fibonacci = fibonacci[:-1]

even_values = []
for value in fibonacci:
    if value%2 == 0:
        even_values.append(value)

result = sum(even_values)
print(result)
