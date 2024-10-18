import streamlit as st

# Temperature conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Streamlit app
def main():
    st.title("Temperature Converter")

    # Options for conversion types
    option = st.selectbox("Select conversion type:", 
                          ("Celsius to Fahrenheit", 
                           "Fahrenheit to Celsius", 
                           "Celsius to Kelvin", 
                           "Kelvin to Celsius", 
                           "Fahrenheit to Kelvin", 
                           "Kelvin to Fahrenheit"))

    # Get input from user
    temp = st.number_input("Enter the temperature:")

    # Perform conversion based on selected option
    if option == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temp)
        st.write(f"{temp}°C is {result}°F")
    elif option == "Fahrenheit to Celsius":
        result = fahrenheit_to_celsius(temp)
        st.write(f"{temp}°F is {result}°C")
    elif option == "Celsius to Kelvin":
        result = celsius_to_kelvin(temp)
        st.write(f"{temp}°C is {result}K")
    elif option == "Kelvin to Celsius":
        result = kelvin_to_celsius(temp)
        st.write(f"{temp}K is {result}°C")
    elif option == "Fahrenheit to Kelvin":
        result = fahrenheit_to_kelvin(temp)
        st.write(f"{temp}°F is {result}K")
    elif option == "Kelvin to Fahrenheit":
        result = kelvin_to_fahrenheit(temp)
        st.write(f"{temp}K is {result}°F")

# Run the app
if __name__ == "__main__":
    main()
