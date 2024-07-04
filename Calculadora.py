def calculadora(num1, num2, op):
    print('Bienvenido a la calculadora de python'.center(50, '-'))
    if op == 1:
        print(f'el resultado de la suma de {num1} y {num2} es: {num1 + num2}')
    elif op == 2:
        print(f'el resultado de la resta de {num1} y {num2} es: {num1 - num2}')
    elif op == 3:
        print(f'el resultado de la multiplicacion de {num1} y {num2} es: {num1 * num2}')
    elif op == 4:
        print(f'el resultado de la division de {num1} y {num2} es: {num1 / num2}')
    else:
        print('Opcion no valida')


variable1 = float(input('Introduzca el primer valor'))
variable2 = float(input('Introduzca el segundo valor'))
calculadora(variable1, variable2, 1)
