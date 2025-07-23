#Funciones de operaciones
def suma(a,b):
    print(f"Resultado: {a+b}")

def resta(a,b):
    print(f"Resultado: {a-b}")

def division(a,b):
    print(f"Resultado: {a/b}")

def multiplicacion(a,b):
    print(f"Resultado: {a*b}")

#Función de menú en consola
def menu():
    while True:
        #Reiniciamos las variables
        op = 0
        op2 = 0

        print("CALCULADORA")
        print("____________")
        print("¿Que operación deseas realizar?")
        print("a) Suma")
        print("b) Resta")
        print("c) Multiplicación")
        print("d) División")
        print("e) Ninguna operación")

        op = input("Introduce tu opción: ")
        op = op.lower()
        
        #Opción para salir del programa
        if op == "e":
            print("Apagando calculadora...")
            print("____________")
            print("Calculadora apagada con éxito.")
            break

        #Operadores
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))

        if op == "a":
            suma(a,b)
        elif op == "b":
            resta(a,b)
        elif op == "c":
            multiplicacion(a,b)
        else:
            division(a,b)
        
        #Menú para volver a empezar o salir del programa
        print("¿Deseas realizar otra operación?")
        print("a) Si")
        print("b) No")

        op2 = input("Introduce tu opción: ")
        op2 = op2.lower()

        if op2 == "b":
            print("Apagando calculadora...")
            print("____________")
            print("Calculadora apagada con éxito.")
            break

menu()
