from flask import Flask, render_template  # Corrected import statement
from pogoda import data_dict  # Ensure this file is in the same directory
import json

app = Flask(__name__)


@app.route('/')
def another_page():
    temperature = data_dict["main"]["temp"]
    weather_description = data_dict["weather"][0]["description"]
    humidity=data_dict["main"]["humidity"]
    return render_template('index.html', temperature=temperature,
                           weather_description=weather_description,
                           humidity=humidity
                           
                           
                           
                           
                           
                           )  # Render index1.html


@app.route('/Climatic_conditions')
def home():
    temperature = data_dict["main"]["temp"]
    return render_template('index1.html', temperature=temperature)  # Pass temperature to index.html



if __name__ == '__main__':
    app.run(debug=True)