# Curso de Python para Principiantes
En este repositorio se encuentran las preguntas y soluciones de los ejercicios presentados en los videos al igual que
los ejemplos del contenido que vamos cubriendo durante el curso.

## Tabla de Contenido
[2. Variables](#variables) <br>
[3. Tipos de Datos](#3-tipos-de-datos)<br>
[4. Listas](#4-listas)<br>
[5. For-loops, Listas Numericas y Tuples]<br>

## 2. Variables

## 3. Tipos de Datos
En esta seccion vimos como se representan varios tipos de datos en Python.
Las soluciones a los ejercicios se encuentran [aqui.](https://github.com/kenjifushida/curso-python-principiantes/blob/main/3_tipos_de_datos/solutions.py)
### Strings
#### Ejercicios
1. Utiliza una variable para guardar el nombre de un amigo o la manera en la que 
llamas a esa persona e imprime un mensaje para el.
Ej. "Hola pendejo, no te olvides de hacer la tarea."
2. Guarda el nombre de una persona en una variable e imprimelo todo en mayusculas, 
minusculas y por ultimo, solo las iniciales en mayusculas.
3. Busca tu cita favorita, guardala en una variable, y guarda el nombre de la 
persona quien dijo esa cita en otra variable. Por ultimo,
imprime la cita en el siguiente formato: "Andá pa'allá, bobo" - Lionel Messi 
(Qatar 2022)
4. Usa una variable para guardar el nombre y apellido de una persona, 
introduciendo caracteres de espacios al principio y al final del String. Por 
ultimo, imprime esta variable, pero quitando los caracteres de espacios al 
rededor de la variable utilizando los metodos nativos de los Strings.
### Numeros
#### Ejercicios
1. Escribe formulas de suma, resta, multiplicacion y division que den como 
resultado el numero 8. Asegurate de imprimir el resultado de cada una de estas 
formulas como por ejemplo:
```python
print(5+3)
```
2. Utiliza una variable para guardar tu numero favorito, despues, imprime un 
mensaje diciendo que tu numero favorito es ese numero que guardaste.

## 4. Listas
En esta seccion vemos lo que son las listas y lo que podemos hacer con ellas 
en Python. Proximamente los ejercicios relacionados se encontraran aqui.
#### Ejercicios
1. Crea una lista de nombres de tus mejores amigos e imprime el nombre de cada
uno de ellos accediendo los elementos de la lista uno por uno.
2. Imprime un saludo para cada uno de tus amigos guardados en la lista del 
ejercicio anterior. El saludo debe ser el mismo para todos, solo debe cambiar
el nombre de tu amigo.
3. Crea una lista de tus hobbies favoritos e imprime oraciones sobre estos hobbies
accediendo a los elementos guardados en esta lista.<br>
Ej. f"A mi me gusta {hobby}." --> "A mi me gusta jugar PlayStation."
4. Crea una lista de minimo 3 personas que quisieras invitar a una fiesta y 
despues imprime una invitacion para cada una de ellas.
5. Utiliza la lista del ejercicio anterior y al final imprime un mensaje diciendo
que "X" persona ya no va a poder asistir a la fiesta. Despues reemplaza el nombre
de la persona que no puede asistir por el nombre de una persona nueva utilizando
uno de los metodos para modificar listas aprendidos e imprime una nueva serie de
invitaciones.
6. Continuando con el programa del ejercicio anterior, ahora imprime un nuevo mensaje
informando que mas personas van a asistir a la fiesta y despues modifica la lista
de la siguiente manera:
- Utiliza el metodo `insert` para adicionar un nuevo invitado al principio de la lista
- Utiliza el metodo `insert` para adicionar un nuevo invitado al medio de la lista.
- Utiliza el metodo `append` para adicionar un ultimo invitado al final de la lista.<br>
Y por ultimo imprime una nueva serie de invitaciones para cada una de las personas
en tu lista final
## 5. For-loops, Listas Numericas y Tuples
En esta seccion aprendimos a utilizar for-loops para iterar sobre cada uno de los
elementos de una lista o copia de una lista. Tambien aprendimos a utilizar la funcion
de range para crear listas numericas, y por ultimo vimos lo que son los tuples y como
utilizarlos.
### For-loops
#### Ejercicios
1. Crea una lista de tus pizzas favoritas y utliza un for-loop para imprimir una oracion
acerca de estas pizzas. Ej: "Me gusta la pizza de pepperoni."
2. Despues de terminar el loop imprimiento una oracion por cada pizza, finaliza el programa
con una oracion acerca de las pizzas en general.
### Listas Numericas
#### Ejercicios
1. Utiliza la funcion de range en conjunto con un for-loop para imprimir los numeros del 1 al 20.
2. Crea una lista de numeros del 1 hasta 1 millon y despues imprime cada uno de ellos.
3. Crea una lista de numeros impares del 1 al 20 e imprimelos.
4. Utiliza una comprension de lista para crear una lista de los resultados del 1 hasta 10 al cuadrado.
### Tuples
#### Ejercicios
1. Crea un tuple de 3 opciones de un menu de sopas.
2. Trata de cambiar una de las opciones por otra y verifica que Python no te deje realizar este cambio.
3. Reemplaza el tuple entero por otras opciones de sopas e imprimelas.
