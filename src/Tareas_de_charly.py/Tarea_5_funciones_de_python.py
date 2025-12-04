"""
Manejo de funcones en python 
Abraham Maximilano Hernandez Sanchez
2530454
IM 1-3
""" 
#Resumen ejecutivo

#In this document, we will examine the use of functions in Python,
#which serve different roles, such as def, which defines a function,
#and return, which sends a value back from a function.
#We will also cover parameters with default values and arguments.
#Beyond the basics, the document highlights the importance of functions for reducing code 
#duplication, encapsulating logic, and creating programs that are easier to test and debug.
#Examples and practice problems will illustrate common patterns such as input processing, 
#data transformation, and repeated computations.


#----------------------------------------------------

 #7.3 Problem 1: Rectangle area and perimeter (basic functions)
 #Define two functions to calculate the area and perimeter of a rectangle.
 #The functions should take the width and height of the rectangle as parameters

# Inputs:
# - width (float)
# - height (float)
# Outputs:
# - "Area" (value)
# - "Perimeter" (value)

#validations:
# - width and height must be positive numbers

# Test cases:
# 1) Normal:
#    Input: width=5, height=3
#    Expected: Area=15, Perimeter=16
#
# 2) Border:
#    Input: width=0.01, height=0.01
#    Expected: Area=0.0001, Perimeter=0.04
#
# 3) Error:
#    Input: width=-4, height=2
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def calculate_area(width, height):
    """Returns the area of a rectangle."""
    return width * height


def calculate_perimeter(width, height):
    """Returns the perimeter of a rectangle."""
    return 2 * (width + height)


# ---- Main program (test values) ----
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))    

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", area)
    print("Perimeter:", perimeter)
else:
    print("Error: invalid input")



#7.3 Problem 2: Grade classifier (functions with return string)
# ----------------------------------------------------
# Description:
#   This program defines a function that receives a
#   numeric grade (0–100) and returns a letter category
#   according to standard grading ranges.
#
# Inputs:
# - score (float or int)
#
# Outputs:
# - "Score:" <score>
# - "Category:" <grade_letter>
#
# Validations:
# - 0 <= score <= 100
# - If invalid, print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: score=85
#    Expected: Category="B"
#
# 2) Border:
#    Input: score=90
#    Expected: Category="A"
#
# 3) Error:
#    Input: score=150
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def classify_grade(score):
    """Returns a letter grade based on the numeric score."""
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ---- Main program ----

score = float(input("Enter the score: "))

if 0 <= score <= 100:
    category = classify_grade(score)
    print("Score:", score)
    print("Category:", category)
else:
    print("Error: invalid input")



# =========================================================
# 7.3 Problem 3: List statistics function (min, max, average)
# =========================================================
# ENTRADAS:
#   - Lista de números ingresados por el usuario separados por comas.
# SALIDAS:
#   - Diccionario con {min, max, average}
# VALIDACIONES:
#   - Entrada vacía
#   - Conversión a número
#   - Lista no vacía
# TESTING:
#   summarize_numbers([1,2,3]) -> {"min":1, "max":3, "average":2}

def summarize_numbers(numbers_list):
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {"min": min_value, "max": max_value, "average": average_value}


numbers_text = input("Ingresa números separados por comas: ").strip()

if numbers_text == "":
    print("Error: input vacío")
else:
    try:
        numbers_list = [float(x) for x in numbers_text.split(",")]

        if len(numbers_list) == 0:
            print("Error: lista vacía")
        else:
            stats = summarize_numbers(numbers_list)
            print("---- RESULTADOS ----")
            print("Min:", stats["min"])
            print("Max:", stats["max"])
            print("Average:", stats["average"])

    except ValueError:
        print("Error: input no numérico")


# =========================================================
# 7.4 Problem 4: Apply discount list (pure function)
# =========================================================
# ENTRADAS:
#   - Lista de precios separados por comas
#   - Tasa de descuento entre 0 y 1
# SALIDAS:
#   - Lista nueva con los precios descontados
# VALIDACIONES:
#   - Lista vacía, precios negativos, descuento incorrecto
# TESTING:
#   apply_discount([100, 200], 0.10) -> [90, 180]

def apply_discount(prices_list, discount_rate):
    return [price * (1 - discount_rate) for price in prices_list]


prices_text = input("Ingresa precios separados por comas: ").strip()

try:
    discount_rate = float(input("Ingresa la tasa de descuento (0 a 1): "))
except ValueError:
    print("Error: la tasa debe ser numérica")
    discount_rate = -1  # Forzar error

if prices_text == "" or not (0 <= discount_rate <= 1):
    print("Error: input inválido")
else:
    try:
        prices_list = [float(p) for p in prices_text.split(",")]

        if any(p < 0 for p in prices_list):
            print("Error: los precios deben ser mayores que 0")
        else:
            discounted_list = apply_discount(prices_list, discount_rate)

            print("---- RESULTADOS ----")
            print("Original prices:", prices_list)
            print("Discounted prices:", discounted_list)

    except ValueError:
        print("Error: input no numérico")


# =========================================================
# 7.5 Problem 5: Greeting function (default parameters)
# =========================================================
# ENTRADAS:
#   - Nombre y título opcional
# SALIDAS:
#   - Cadena con saludo formateado
# TESTING:
#   greet("Alice") -> "Hello, Alice!"
#   greet("Bob", "Dr.") -> "Hello, Dr. Bob!"

def greet(name, title=""):
    name = name.strip()
    title = title.strip()
    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"

print(greet("Alice"))
print(greet("Bob", "Dr."))
print(greet(name="Charlie", title="Eng."))
# =========================================================

# ----------------------------------------------------
# Problem 6: Factorial function (iterative or recursive)
# Description:
#   This program defines a function factorial(n) that
#   returns the factorial of a non-negative integer n.
#   The implementation used here is iterative, because
#   it avoids recursion depth limits and is easier to
#   understand for large values of n.
#
# Inputs:
# - n (int)
#
# Outputs:
# - "n:" <n>
# - "Factorial:" <factorial_value>
#
# Validations:
# - n must be an integer
# - n >= 0
# - Optional: n <= 20 to avoid extremely large numbers
# - If validation fails, print "Error: invalid input"
#
# Test cases:
# 1) Normal:
#    Input: n=5
#    Expected: Factorial=120
#
# 2) Border:
#    Input: n=0
#    Expected: Factorial=1
#
# 3) Error:
#    Input: n=-3
#    Expected: "Error: invalid input"
# ----------------------------------------------------

def factorial(n):
    """Returns n! using an iterative approach."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# ---- Main program ----

# Ask user for input
user_input = input("Enter a non-negative integer: ")

# Validate that input is an integer
if user_input.isdigit():  # ensures digits only, no negatives
    n = int(user_input)

    # Validate range
    if 0 <= n <= 20:
        fact_value = factorial(n)
        print("n:", n)
        print("Factorial:", fact_value)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")


#Conclusions
#Functions are essential building blocks in Python programming.
#They allow for code reuse, modularity, and better organization.
#By defining functions, we can encapsulate logic, reduce duplication,
#and create programs that are easier to test and debug.
#Common patterns include input processing, data transformation,
#and repeated computations, all of which benefit from the use of functions.


#References
"""
Python Software Foundation.
Python Documentation – Built-in Types: Numeric Types (int, float, complex).
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Python Software Foundation.
Boolean Type — bool.
https://docs.python.org/3/library/stdtypes.html#truth-value-testing

Python Software Foundation.
Input and Output — The input() function.
https://docs.python.org/3/library/functions.html#input

*Python Documentation – Expressions and Operators.
(Arithmetic, comparison, logical operators)
https://docs.python.org/3/reference/expressions.html

Real Python.
Understanding Data Types in Python (Numbers, Booleans, Type Casting).
https://realpython.com/python-data-types/

W3Schools Python Tutorial.
Python If…Else, Logical Operators, and Conditions.
https://www.w3schools.com/python/python_conditions.asp

Automate the Boring Stuff with Python – Chapter 2.
Flow Control, Boolean Logic, Input Validation.
https://automatetheboringstuff.com/

Think Python (Allen B. Downey).
Chapter 7–8: Loops, Conditionals, boolean expressions.
http://greenteapress.com/thinkpython2/thinkpython2.pdf
"""