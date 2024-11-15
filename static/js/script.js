// Функция для получения данных о погоде с сервера
function fetchWeatherData() {
    fetch('/weather-data')
        .then(response => response.json())
        .then(data => {
            // Обновляем информацию на странице
            document.getElementById('temp').textContent = `Температура: ${data.main.temp}°C`;
            document.getElementById('description').textContent = `Погода: ${data.weather[0].description}`;

            // Обновляем карту
            updateMap(data.coord.lat, data.coord.lon, data.weather[0].description, data.main.temp);
        })
        .catch(error => console.error('Ошибка при получении данных о погоде:', error));
}

// Функция для обновления карты
function updateMap(lat, lon, description, temp) {
    var map = L.map('map').setView([lat, lon], 10);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

    L.marker([lat, lon])
        .addTo(map)
        .bindPopup(`<b>Погода:</b> ${description}<br><b>Температура:</b> ${temp}°C`)
        .openPopup();
}

// Запускаем обновление погоды каждые 30 секунд
setInterval(fetchWeatherData, 30000);

// Вызовем сразу при загрузке страницы
fetchWeatherData();
