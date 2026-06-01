def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def menu():
    print("\n--- CALCULADORA SIMPLE (ejercicio:3.0.0) ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '5':
            print("¡Adiós!")
            break
            
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == '1':
                    print(f"Resultado: {sumar(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {restar(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {multiplicar(num1, num2)}")
                elif opcion == '4':
                    # Agregamos la llamada a la función dividir
                    print(f"Resultado: {dividir(num1, num2)}")
                    
            except ValueError as e:
                # Captura tanto el error de división por cero como si ingresan texto
                print(f"Error: {e}")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")