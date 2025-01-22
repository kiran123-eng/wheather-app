import requests

# Function to get weather data
def get_weather(city):
    api_key = "a83de42c1f5b80ca55661bc3c7e78e54"  # Replace with your actual OpenWeatherMap API key
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

        # Printing the results
        print(f"\nWeather in {city}:\n")
        print(f"Temperature: {temp}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}\n")
    else:
        print("City not found. Please try again.\n")

# Main program to get city input and fetch weather
def main():
    print("Welcome to the Weather App!")
    
    # Loop to continuously ask for a city name until the user types "exit"
    while True:
        city = input("Enter city name (or type 'exit' to quit): ")  # Ask the user for the city
        
        if city.lower() == "exit":
            print("Goodbye!")
            break  # Exit the loop and the program
        
        get_weather(city)  # Fetch and display weather data for the city

if __name__ == "__main__":
    main()
