import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['date'])  # Чтение с преобразованием дат
    return data


def generate_temperature_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['tavg'], marker='o', color='red', label='Средняя температура (°C)')
    plt.title('Изменение средней температуры')
    plt.xlabel('Дата')
    plt.ylabel('Температура (°C)')
    plt.grid(True)
    plt.legend()
    plt.savefig('static/temperature_chart.png')
    plt.close()


def generate_rainfall_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['prcp'], marker='o', color='blue', label='Осадки (мм)')
    plt.title('Изменение уровня осадков')
    plt.xlabel('Дата')
    plt.ylabel('Осадки (мм)')
    plt.grid(True)
    plt.legend()
    plt.savefig('static/rainfall_chart.png')
    plt.close()


data = load_data('static/export.csv')  


generate_temperature_chart(data)
generate_rainfall_chart(data)

print("Графики сгенерированы на основе реальных данных.")
