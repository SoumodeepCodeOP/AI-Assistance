import requests

def Weather():
    api_key = 'bd5e378503939ddaee76f12ad7a97608'  # Replace with your actual OpenWeatherMap API key
    city = 'Kolkata'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        return f"Error fetching weather: {response.status_code}"

    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    unit = "°C"

    return f"Weather in {city} is {temp} {unit} {desc.capitalize()}"
