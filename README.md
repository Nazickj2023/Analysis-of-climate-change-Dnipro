# Analysis of climate change Dnipro

## Опис проекту

**Analysis of climate change Dnipro** — це веб-додаток, що аналізує кліматичні зміни у місті Дніпро,  API для відображення поточних кліматичних умов і динаміки змін. Додаток надає користувачам інструменти для візуалізації кліматичних даних у вигляді інтерактивних карт та графіків.

---

## Основні функції

1. **Аналіз кліматичних даних**:
   - Поточна погода в місті Дніпро (температура, вологість, опис стану погоди).
   - Візуалізація змін кліматичних параметрів.

2. **Інформація про команду**:
   - Сторінка, де представлена команда, яка працювала над проектом.

---

## Технології

- **Backend**: Python
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **API**: OpenWeatherMap для отримання кліматичних даних
- **Графіка**: Matplotlib для візуалізації (можливість заміни реальними картами з зовнішнього джерела)
- **Розгортання**: Flask (локально або на хостинг-платформах, таких як Heroku)

---

## Встановлення та запуск

### Вимоги
- Python 3.8+
- Встановлений `pip`

### Інструкції

1. **Склонуйте репозиторій**:
   - git clone https://github.com/username/klimat-dnipro.git](https://github.com/Nazickj2023/Analysis-of-climate-change-Dnipro.git
   - cd klimat-dnipro
2. **Створіть віртуальне середовище та активуйте його**
- python -m venv venv
- source venv/bin/activate   # для Linux/MacOS
- venv\Scripts\activate      # для Windows
3. **Встановіть залежності**
- pip install -r requirements.txt
4. **Налаштуйте API ключ**
- Зареєструйтесь на OpenWeatherMap та отримайте API ключ.
- В файле pogoda.py добавьте ваш API-ключ в переменную API_KEY вместо your_openweathermap_api_key
5. **Запустіть сервер**
- python app.py
6. **Відкрийте додаток у браузері:**
- http://127.0.0.1:5000/


