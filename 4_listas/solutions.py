# Soluciones a las preguntas de Introduccion a Listas

# 1
names = ['Elber Galarga', 'Rosa Melano', 'Juancho Talarga', 'Elva Ginon']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 2
print(f'Hola, {names[0]}')
print(f'Hola, {names[1]}')
print(f'Hola, {names[2]}')
print(f'Hola, {names[3]}')

# 3 
hobbies = ['futbol', 'trotar', 'bouldering', 'bowling']
print(f'A mi me gusta jugar {names[0]}')
print(f'A mi me gusta jugar {names[1]}')
print(f'A mi me gusta jugar {names[2]}')
print(f'A mi me gusta jugar {names[3]}')

# 4 (la linea numero 24 es utilizada para los ejercicios 4, 5 y 6)
guests = ['Naruto', 'Sasuke', 'Sakura']
print(f'{guests[0]}, has sido invitado para la fiesta.')
print(f'{guests[1]}, has sido invitado para la fiesta.')
print(f'{guests[2]}, has sido invitado para la fiesta.')

# 5
print(f'{guests[2]} no puede asistir a la fiesta.')
guests[2] = 'Kakashi'
print(f'{guests[0]}, has sido invitado para la fiesta.')
print(f'{guests[1]}, has sido invitado para la fiesta.')
print(f'{guests[2]}, has sido invitado para la fiesta.')

# 6
print('Mas personas han sido invitadas a la fiesta.')
guests.insert(0, 'Gaara')
guests.insert(2, 'Kankuro')
guests.append('Temari')
print(f'{guests[0]}, has sido invitado para la fiesta.')
print(f'{guests[1]}, has sido invitado para la fiesta.')
print(f'{guests[2]}, has sido invitado para la fiesta.')
print(f'{guests[3]}, has sido invitado para la fiesta.')
print(f'{guests[4]}, has sido invitado para la fiesta.')
print(f'{guests[5]}, has sido invitado para la fiesta.')
