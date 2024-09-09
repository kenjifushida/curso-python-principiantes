# Soluciones a la seccion de For loops, Slices y Tuples

# For-loops
# 1
pizzas = ['pepperoni', 'jamon y queso', 'hawaiana']
for pizza in pizzas:
    print(f'Me gusta la pizza de {pizza}')

# 2
pizzas = ['pepperoni', 'jamon y queso', 'hawaiana']
for pizza in pizzas:
    print(f'Me gusta la pizza de {pizza}')

print('Me encanta comer pizza!')

# Listas Numericas
# 1
for number in range(1, 21):
    print(number)

# 2
numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

# 3
oddNumbers = list(range(1, 20, 2))
for number in oddNumbers:
    print(number)

# 4
squaredNumbers = [value ** 2 for value in range(1, 11)]

# Tuples
# 1
soups = ('sancocho', 'ajiaco', 'sopa de miso')
print(soups)

# 2
soups = ('sancocho', 'ajiaco', 'sopa de miso')
soups[0] = 'ramen'

# 3
soups = ('ramen', 'sopa de verduras')
print(soups)
