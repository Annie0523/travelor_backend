const btn = document.getElementById('btn');

btn.addEventListener('click', async function () {
    const city = document.getElementById('city').value.trim();

    if (!city) {
        document.getElementById('result').innerHTML = 'Please enter a city name.';
        return;
    }

    try {
        const weatherData = await fetchWeatherData(city);
        displayWeather(weatherData);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = 'Error fetching weather data. Please try again.';
    }
});

// Fetch weather data from the OpenWeatherMap API
async function fetchWeatherData(city) {
    const apiKey = 'e0064657765b47ca4e8b74e09e042fe5'; // Replace with your API key
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

    const response = await fetch(url);
    if (!response.ok) {
        throw new Error('City not found or API error');
    }
    return await response.json();
}

// Display weather data on the frontend
function displayWeather(data) {
    const result = document.getElementById('result');
    result.innerHTML = `
        <h2>Weather of ${data.name}</h2>
        <h4>Temperature: ${Math.round(data.main.temp - 273.15)}°C</h4>
        <h4>Feels like: ${Math.round(data.main.feels_like - 273.15)}°C</h4>
        <h4>Humidity: ${data.main.humidity}%</h4>
        <h4>Pressure: ${data.main.pressure} hPa</h4>
        <h4>Wind speed: ${data.wind.speed} m/s</h4>
        <h4>Wind direction: ${data.wind.deg}°</h4>
    `;
}
