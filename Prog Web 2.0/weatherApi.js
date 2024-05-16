$(document).ready(function() {
    // Usar un endpoint válido de la API de AccuWeather
    var apiKey = 'jvp6FZknjpEJNLDEMkAy7Y9DZolzrG5d';
    var locationKey = '60449'; // Santiago, por ejemplo
    var apiUrl = `http://dataservice.accuweather.com/forecasts/v1/daily/1day/${locationKey}?apikey=${apiKey}&language=en-us&details=true&metric=true`;

    $.get(apiUrl, function(data) {
        var forecast = data.DailyForecasts[0];
        var temperatureCurrent = forecast.Temperature.Maximum.Value + ' °C';
        var temperatureMin = forecast.Temperature.Minimum.Value + ' °C';
        var temperatureDescription = forecast.Day.IconPhrase;
        var date = new Date(forecast.Date).toLocaleDateString();

        $('.temperature').text(temperatureCurrent);
        $('.temperature-description').text(temperatureDescription);
        $('.temperature-range').text('Min: ' + temperatureMin + ' - Max: ' + temperatureCurrent);
        $('#date').text(date);
        
        // Actualizar el estilo del icono del clima
        var weatherIcon = $('#weather-icon');
        weatherIcon.removeClass(); // Remover clases anteriores

        if (temperatureDescription.toLowerCase().includes('rain') || temperatureDescription.toLowerCase().includes('showers')) {
            weatherIcon.addClass('fas fa-cloud-showers-heavy');
        } else if (temperatureDescription.toLowerCase().includes('snow')) {
            weatherIcon.addClass('fas fa-snowflake');
        } else if (temperatureDescription.toLowerCase().includes('thunderstorm')) {
            weatherIcon.addClass('fas fa-bolt');
        } else if (temperatureDescription.toLowerCase().includes('sunny') || temperatureDescription.toLowerCase().includes('clear')) {
            weatherIcon.addClass('fas fa-sun');
        } else if (temperatureDescription.toLowerCase().includes('cloudy') || temperatureDescription.toLowerCase().includes('overcast')) {
            weatherIcon.addClass('fas fa-cloud');
        } else {
            weatherIcon.addClass('fas fa-question'); // Icono por defecto si no coincide con ninguna condición
        }
    });
    
});