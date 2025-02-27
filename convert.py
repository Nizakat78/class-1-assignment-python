import streamlit as st

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34,
    }
    
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return None
    
    meters = value * conversion_factors[from_unit]
    converted_value = meters / conversion_factors[to_unit]
    return converted_value

# Streamlit UI Enhancements
st.set_page_config(page_title="Length Converter", page_icon="📏", layout="centered")
st.title("📏 Length Converter")

st.markdown("### Convert between different length units effortlessly!")

# Default values for international standards
units = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]
from_unit = st.selectbox("From Unit:", units, index=2)  # Default meter
to_unit = st.selectbox("To Unit:", units, index=3)  # Default kilometer

value = st.number_input("Enter Length Value:", min_value=0.0, value=1.0, format="%.6f")

if st.button("Convert", use_container_width=True):
    result = convert_length(value, from_unit, to_unit)
    if result is not None:
        st.success(f"✅ {value} {from_unit} is equal to {result:.6f} {to_unit}")
    else:
        st.error("⚠️ Invalid unit selection.")

st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
