from calculator.operations import add, subtract, multiply, divide, exponentiate, sqrt, modulo
from calculator.memory import Memory
from calculator.history import History
from calculator.settings import Settings

def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
            num2 = None
            if operator not in ('√',):
                num2 = float(input("Enter the second number: "))
            return num1, operator, num2
        except ValueError:
            print("Invalid input. Please enter numbers correctly.")

def calculate(num1, operator, num2):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    elif operator == '^':
        return exponentiate(num1, num2)
    elif operator == '√':
        return sqrt(num1)
    elif operator == '%':
        return modulo(num1, num2)
    else:
        print("Invalid operator")
        return None

def main():
    history = History()
    memory = Memory()
    settings = Settings()

    while True:
        num1, operator, num2 = get_user_input()
        result = calculate(num1, operator, num2)
        
        if result is not None:
            result = settings.round_result(result)
            print(f"Result: {result}")
            history.add_entry(num1, operator, num2, result)
        
        save_memory = input("Do you want to save this result to memory? (y/n): ")
        if save_memory.lower() == 'y' and result is not None:
            memory.store(result)
        
        view_history = input("View calculation history? (y/n): ")
        if view_history.lower() == 'y':
            history.show()
        
        new_calc = input("Would you like to perform another calculation? (y/n): ")
        if new_calc.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
