import streamlit as st
import math

# Define functions for the calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    return math.log10(x)

def sqrt(x):
    return math.sqrt(x)

# Create the Streamlit app interface
st.title("Scientific Calculator")

# Get user input
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number (if needed)", value=0.0)

# Operation buttons
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide", "Sin", "Cos", "Tan", "Log", "Sqrt"])

# Result output
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Sin":
        result = sin(num1)
    elif operation == "Cos":
        result = cos(num1)
    elif operation == "Tan":
        result = tan(num1)
    elif operation == "Log":
        if num1 > 0:
            result = log(num1)
        else:
            result = "Error: Logarithm of non-positive number"
    elif operation == "Sqrt":
        if num1 >= 0:
            result = sqrt(num1)
        else:
            result = "Error: Square root of negative number"
    
    st.success(f"Result: {result}")

# Clear button (reset values)
if st.button("Clear"):
    st.experimental_rerun()
