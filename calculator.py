## small calculator program


svar = input("Vill du räkna? (y/n)")

while svar == 'y':
    operator = input("Enter operator ( + -  * /): ")

    if operator == '+':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 + num2)

    elif operator == '-':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 - num2)

    elif operator == '*':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 * num2)

    elif operator == '/':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1 / num2)

    print("Vill du fortsätta räkna? (y/n)")
    svar2 = input()
    if svar2 == 'y':
        continue
    else:
        break

else:
    print("Okej stänger av programmet")