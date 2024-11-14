




const apiUrl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=CITY:UP000023&startdate=2020-01-01&enddate=2023-01-01&datatypeid=TAVG&units=metric';

// Твій API-ключ
const apiKey = 'YOUR_NOAA_API_KEY';

// Функція для отримання даних про клімат
async function getClimateData() {
  try {
    const response = await fetch(apiUrl, {
      method: 'GET',
      headers: {
        token: apiKey
      }
    });

    const data = await response.json();

    // Обробка отриманих даних
    const temperatures = data.results.map(item => item.value);
    const dates = data.results.map(item => item.date.split('T')[0]);

    // Відображення даних на графіку
    renderTemperatureChart(dates, temperatures);
  } catch (error) {
    console.error('Помилка завантаження кліматичних даних:', error);
  }
}

// Функція для відображення графіку температури за допомогою Chart.js
function renderTemperatureChart(labels, data) {
  const ctxTemp = document.getElementById('temperature-chart').getContext('2d');
  new Chart(ctxTemp, {
    type: 'line',
    data: {
      labels: labels,
      datasets: [{
        label: 'Середня температура (°C)',
        data: data,
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 2,
        fill: false
      }]
    }
  });
}

// Виклик функції для отримання кліматичних даних при завантаженні сторінки
window.onload = function() {
  getClimateData();
};
