import streamlit as st
st.markdown(
    """
   <style>
        .stButton>button {
            width: 150px;
            height: 50px;
            font-size: 16px;
            font-weight: bold;
            color: black;
            background-color: white;
            border: 1px solid black; /* Black border */
            border-radius: 5px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            transition: background-color 0.3s ease, border-color 0.3s ease; /* Smooth transitions */
        }
        
        .stButton>button:hover {
            background-color: #d3f7d1; /* Light green background */
            border-color: #4caf50; /* Green border */
            color: black; /* Change text color on hover if needed */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state if not already done
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Function to handle button click
def update_input(value):
    st.session_state.input_text += value

# Function to clear the input field
def clear_input():
    st.session_state.input_text = ""
    st.session_state.result = ""

# Function to calculate the result
def calculate():
    try:
        # Evaluate the expression in the input field
        st.session_state.result = str(eval(st.session_state.input_text))
    except:
        st.session_state.result = "Error"

# Text input field with a value from session state
st.text_input('Input', value=st.session_state.input_text, key='input_text')
st.text_input('Result', value=st.session_state.result, key='result', disabled=True)

# Creating columns for buttons
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7, col8 = st.columns(4)
col9, col0, colplus, colsub = st.columns(4)
coldiv, colmul,colc,cole = st.columns(4)

# Buttons in each column and handling button click events
with col1:
    if st.button("1", on_click=update_input, args=("1",)):
        pass

with col2:
    if st.button("2", on_click=update_input, args=("2",)):
        pass

with col3:
    if st.button("3", on_click=update_input, args=("3",)):
        pass

with col4:
    if st.button("4", on_click=update_input, args=("4",)):
        pass

with col5:
    if st.button("5", on_click=update_input, args=("5",)):
        pass

with col6:
    if st.button("6", on_click=update_input, args=("6",)):
        pass

with col7:
    if st.button("7", on_click=update_input, args=("7",)):
        pass

with col8:
    if st.button("8", on_click=update_input, args=("8",)):
        pass

with col9:
    if st.button("9", on_click=update_input, args=("9",)):
        pass

with col0:
    if st.button("0", on_click=update_input, args=("0",)):
        pass

with colplus:
    if st.button("Plus", on_click=update_input, args=("+",)):
        pass

with colsub:
    if st.button("Minus", on_click=update_input, args=("-",)):
        pass

with coldiv:
    if st.button("Division", on_click=update_input, args=("/",)):
        pass

with colmul:
    if st.button("Multiply", on_click=update_input, args=("*",)):
        pass

with colc:
    if st.button("Clear", on_click=clear_input):
        pass
with cole:

# Calculate button
    if st.button("=", on_click=calculate):
        pass
