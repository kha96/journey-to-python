# data types 

# # primitive data types 
# # syntax for creating a variable
# # {name_of_variable} = {value}

# # python variables naming convention is 'snake-case' https://en.wikipedia.org/wiki/Snake_case

# int_variable: int = 123
# string_test: str = "my_string"
# float_var: float = 12.12
# byte_string: bytes = b'my_byte_string'
# print(int_variable)


## Calculator app
### How to declare a function? -> def {name_of_function}({name_of_argument}:{type_of_argument}) -> None

### +, -, /, *

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> int: 
    safe_b = 1 if b <= 0 else b
    return a // safe_b


# print(add(1, 1))
# print(subtract(1, 2))
# print(multiply(9, 1000000))
# print(divide(4, 2))
# print(divide(4, 3))

print("Welcome to Asiya's Calculator!\n")

while True:
    command: str = input("Entre symbol (+, -, /, *). Or 'stop' to stop running: ")

    if command == "stop" or command not in ["+", "-", "/", "*"]:
        break

    a = int(input("Write first number: "))
    b = int(input("Write second number: "))

    if command == "+": 
        print(add(a, b))

    elif command == "-": 
        print(subtract(a, b))

    elif command == "/": 
        print(divide(a, b))
    
    elif command == "*": 
        print(multiply(a, b))