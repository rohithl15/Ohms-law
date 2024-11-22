import streamlit as st

st.title("Ohm's Law Calculator")

# Input fields for voltage, current, and resistance
voltage = st.number_input("Enter Voltage (V)", min_value=0.0, step=0.1)
current = st.number_input("Enter Current (I)", min_value=0.0, step=0.1)
resistance = st.number_input("Enter Resistance (R)", min_value=0.0, step=0.1)

# Calculate the missing value based on the inputs
if voltage and current:
    resistance = voltage / current
    st.write(f"Calculated Resistance (R): {resistance} ohms")
elif voltage and resistance:
    current = voltage / resistance
    st.write(f"Calculated Current (I): {current} amperes")
elif current and resistance:
    voltage = current * resistance
    st.write(f"Calculated Voltage (V): {voltage} volts")
else:
    st.write("Please enter at least two values to calculate the third.")

