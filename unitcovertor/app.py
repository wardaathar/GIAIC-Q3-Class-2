import streamlit as st
from forex_python.converter import CurrencyRates
from pint import UnitRegistry

def main():
    st.set_page_config(page_title="Unit Converter", layout="centered")
    st.title(" Unit Converter 🌍")
    
    option = st.selectbox("Select  Type", ["Length", "Weight", "Temperature", "Currency"])
    
    if option == "Length":
        convert_units("Length", "meter", "kilometer", "mile", "foot")
    elif option == "Weight":
        convert_units("Weight", "gram", "kilogram", "pound", "ounce")
    elif option == "Temperature":
        convert_temperature()
    elif option == "Currency":
        convert_currency()

def convert_units(category, *units):
    ureg = UnitRegistry()
    st.subheader(f"{category} Converter")
    value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
    from_unit = st.selectbox("From:", units)
    to_unit = st.selectbox("To:", units)
    
    if st.button("Convert"):
        try:
            result = (value * ureg(from_unit)).to(to_unit)
            st.success(f"{value} {from_unit} = {result.magnitude:.4f} {to_unit}")
        except:
            st.error("Invalid conversion. Please try again!")

def convert_temperature():
    st.subheader("Temperature Converter")
    value = st.number_input("Enter temperature:", format="%.2f")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert"):
        result = None
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
        
        st.success(f"{value:.2f} {from_unit} = {result:.2f} {to_unit}")

def convert_currency():
    st.subheader("Currency Converter")
    c = CurrencyRates()
    value = st.number_input("Enter amount:", min_value=0.0, format="%.2f")
    from_currency = st.text_input("From Currency (e.g., USD, EUR, INR):").upper()
    to_currency = st.text_input("To Currency (e.g., USD, EUR, INR):").upper()
    
    if st.button("Convert"):
        try:
            rate = c.get_rate(from_currency, to_currency)
            result = value * rate
            st.success(f"{value:.2f} {from_currency} = {result:.2f} {to_currency}")
        except:
            st.error("Invalid currency code or API error. Try again!")

if __name__ == "__main__":
    main()
