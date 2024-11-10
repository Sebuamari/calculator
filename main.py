from calculator import Calculator

try:
    input_a = int(input("Enter first input: "))
    input_b = int(input("Enter second input: "))
    calculator = Calculator()
    print(f"{input_a} + {input_b} = {calculator.add(input_a, input_b)}")
    print(f"{input_a} * {input_b} = {calculator.multiply(input_a, input_b)}")
except ValueError:
    print("Invalid input. Input must be number!")
except Exception as e:
    print(e)