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

# Initialize session state for input values
if 'num1' not in st.session_state:
    st.session_state['num1'] = 0.0
if 'num2' not in st.session_state:
    st.session_state['num2'] = 0.0
if 'result' not in st.session_state:
    st.session_state['result'] = ''

# Create the Streamlit app interface
st.title("Scientific Calculator")

# Get user input and store in session state
st.session_state['num1'] = st.number_input("Enter first number", value=st.session_state['num1'], key="input_num1")
st.session_state['num2'] = st.number_input("Enter second number (if needed)", value=st.session_state['num2'], key="input_num2")

# Operation buttons
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide", "Sin", "Cos", "Tan", "Log", "Sqrt"])

# Result output
if st.button("Calculate"):
    num1 = st.session_state['num1']
    num2 = st.session_state['num2']
    if operation == "Add":
        st.session_state['result'] = add(num1, num2)
    elif operation == "Subtract":
        st.session_state['result'] = subtract(num1, num2)
    elif operation == "Multiply":
        st.session_state['result'] = multiply(num1, num2)
    elif operation == "Divide":
        st.session_state['result'] = divide(num1, num2)
    elif operation == "Sin":
        st.session_state['result'] = sin(num1)
    elif operation == "Cos":
        st.session_state['result'] = cos(num1)
    elif operation == "Tan":
        st.session_state['result'] = tan(num1)
    elif operation == "Log":
        if num1 > 0:
            st.session_state['result'] = log(num1)
        else:
            st.session_state['result'] = "Error: Logarithm of non-positive number"
    elif operation == "Sqrt":
        if num1 >= 0:
            st.session_state['result'] = sqrt(num1)
        else:
            st.session_state['result'] = "Error: Square root of negative number"
    
    st.success(f"Result: {st.session_state['result']}")

# Clear button
if st.button("Clear"):
    st.session_state['num1'] = 0.0
    st.session_state['num2'] = 0.0
    st.session_state['result'] = ''

    # This resets the inputs and results on the interface without rerunning the app
    st.experimental_rerun()
