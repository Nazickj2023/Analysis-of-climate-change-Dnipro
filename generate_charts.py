import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['date'])  
    return data


def generate_temperature_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['tavg'], marker='o', color='red', label='Середня температура (°C)')
    plt.title('Зміна середньої температури')
    plt.xlabel('Дата')
    plt.ylabel('Температура (°C)')
    plt.grid(True)
    plt.legend()
    plt.savefig('static/temperature_chart.png')
    plt.close()


def generate_rainfall_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['prcp'], marker='o', color='blue', label='Опади (мм)')
    plt.title('Зміна рівня опадів')
    plt.xlabel('Дата')
    plt.ylabel('Опади (мм)')
    plt.grid(True)
    plt.legend()
    plt.savefig('static/rainfall_chart.png')
    plt.close()


data = load_data('static/export.csv')  


generate_temperature_chart(data)
generate_rainfall_chart(data)

print("Графіки згенеровані з урахуванням реальних даних")