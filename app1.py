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
    # Add a colorful title and description
    st.markdown("<h1 style='text-align: center; color: #FF6347;'>🌡️ Temperature Converter 🌡️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Easily convert temperatures between Celsius, Fahrenheit, and Kelvin!</p>", unsafe_allow_html=True)

    # Side panel for extra interaction
    st.sidebar.title("⚙️ Settings")
    st.sidebar.write("Use this panel to change settings or view additional information!")

    # Options for conversion types
    option = st.selectbox("Select conversion type:", 
                          ("Celsius to Fahrenheit 🌞", 
                           "Fahrenheit to Celsius ❄️", 
                           "Celsius to Kelvin 🔥", 
                           "Kelvin to Celsius 🌡️", 
                           "Fahrenheit to Kelvin 🧊", 
                           "Kelvin to Fahrenheit 🌈"))

    # Get input from user with default temperature set to 0
    temp = st.number_input("Enter the temperature:", value=0.0, step=0.1)

    # Perform conversion based on selected option
    if option == "Celsius to Fahrenheit 🌞":
        result = celsius_to_fahrenheit(temp)
        st.success(f"🌡️ {temp}°C is equal to {result}°F")
    elif option == "Fahrenheit to Celsius ❄️":
        result = fahrenheit_to_celsius(temp)
        st.success(f"❄️ {temp}°F is equal to {result}°C")
    elif option == "Celsius to Kelvin 🔥":
        result = celsius_to_kelvin(temp)
        st.success(f"🔥 {temp}°C is equal to {result}K")
    elif option == "Kelvin to Celsius 🌡️":
        result = kelvin_to_celsius(temp)
        st.success(f"🌡️ {temp}K is equal to {result}°C")
    elif option == "Fahrenheit to Kelvin 🧊":
        result = fahrenheit_to_kelvin(temp)
        st.success(f"🧊 {temp}°F is equal to {result}K")
    elif option == "Kelvin to Fahrenheit 🌈":
        result = kelvin_to_fahrenheit(temp)
        st.success(f"🌈 {temp}K is equal to {result}°F")

    # Add an image or GIF for aesthetics (optional)
    st.markdown("<br><hr><p style='text-align: center;'>Have fun with conversions! 🚀</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/I6e0dLN.png", use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
