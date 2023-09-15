
import requests


# Function to fetch weather data from OpenWeatherMap API
def get_weather_data(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        return data
    else:
        return None


# Function to generate and display the weather report
def generate_weather_report(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        report = f"Weather in {city}:\n"
        report += f"Temperature: {temperature}°C\n"
        report += f"Humidity: {humidity}%\n"
        report += f"Condition: {weather_desc}\n"
        report += f"Wind Speed: {wind_speed} m/s\n"

        return report
    else:
        return "Weather data not found for the specified location."


def main():
    api_key = "4fb8807eaf5fd0e7db711298f6cc2365"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")

    weather_data = get_weather_data(api_key, city)
    report = generate_weather_report(weather_data)

    print(report)


if __name__ == "__main__":
    main()