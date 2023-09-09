class Dog:
    name: str = "Garry"

    def __init__(self, name: str = None) -> None:
        if name:
            self.name = name

    def bark(self):
        print(f"I am {self.name} -> motherfucker!")


dog = Dog("Garry2")
dog.bark()

## ============


class Car:
    brand: str

    def __init__(self, brand: str) -> None:
        self.brand = brand

    def print_brand(self):
        print(self.brand)


class BMWCar(Car):
    def __init__(self) -> None:
        super().__init__(brand="BMW")


## ===========

# 1. Create Calculator class
# 2. move computation methods from calculator.py into this class
# 3. declare a variable inside calculator class called tmp_result: int
# 4. tmp_result will hold the result of any computation performed (+, -, / , * and etc)
# 5. Calculator class constructor will take tmp_result parameter as a first argument
# 6. inside while loop calculator class is instantiated during the very first interaction with the user and A is assigned as a tmp_result in a constructor


class Calculator:
    tmp_result: int = 0

    def _add(self, a: int, b: int) -> int:
        return a + b

    def _minus(self, a: int, b: int) -> int:
        return a - b
    
    def _divide(self, a: int, b: int) -> int:
        return a / b

    def _multiply(self, a: int, b: int ) -> int:
        return a * b

    def _percent(self, a: int, b: int ) -> int:
        return ( a / 100 ) * b
    
    def clear(self) -> None:
        self.tmp_result = 0
    
    def compute(self, command: str, a: int, b: int) -> int:
        result = 0

        if command == "+":
            result = self._add(a, b)

        elif command == "-":
            result = self._minus(a, b)

        elif command == "/":
            result = self._divide(a, b)

        elif command == "*":
            result = self._multiply(a, b)
    
        elif command == "%":
            result = self._percent(a, b)

        self.tmp_result = result
        return self.tmp_result


print("Welcome to Asiya's Calculator!\n")

calculator = Calculator()

while True:
    command: str = input("Enter symbol (+, -, /, *, %, C ). Or 'stop' to stop running: ")

    if command == "stop" or command not in ["+", "-", "/", "*", "%" , "C"]:
        break

    if command == "C" :
        calculator.clear()
        continue
    
    a = (
        int(input("Write first number: "))
        if not calculator.tmp_result
        else calculator.tmp_result
    )
    b = int(input("Write second number: "))

    print(calculator.compute(command, a, b))
 
