import tkinter as tk
from tkinter import messagebox
import requests

# Function to get weather data
def get_weather(city):
    api_key = "a83de42c1f5b80ca55661bc3c7e78e54"  # Replace with your  OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Constructing the URL for the API request
    url = f"{base_url}q={city}&appid={api_key}&units=metric"

    # Sending the request
    response = requests.get(url)
    data = response.json()

    # Checking if the city was found
    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Extracting relevant data
        temp = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["description"]

        # Displaying results in the GUI
        result_label.config(text=f"Weather in {city}:\n"
                                f"Temperature: {temp}°C\n"
                                f"Pressure: {pressure} hPa\n"
                                f"Humidity: {humidity}%\n"
                                f"Description: {description.capitalize()}")
    else:
        # If city not found, display error message in the GUI
        messagebox.showerror("City not found", "Please enter a valid city name.")

# Function to be called when the user presses the "Get Weather" button
def on_get_weather_button_click():
    city = city_entry.get()  # Get the city name from the input field
    if city:
        get_weather(city)
    else:
        messagebox.showwarning("Input error", "Please enter a city name.")

# Creating the main window
window = tk.Tk()
window.title("Weather App")

# Creating the input field for city name
city_label = tk.Label(window, text="Enter city name:")
city_label.pack(pady=5)

city_entry = tk.Entry(window, width=30)
city_entry.pack(pady=5)

# Creating the button to fetch weather data
get_weather_button = tk.Button(window, text="Get Weather", command=on_get_weather_button_click)
get_weather_button.pack(pady=10)

# Label to display the results
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI main loop
window.mainloop()
