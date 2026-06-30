import sys
import requests
from datetime import datetime

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)

# Replace with your OpenWeatherMap API Key
API_KEY = "81e0967d31a0bc39b93b58881370dc4f"


class WeatherApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Weather App Pro")
        self.resize(500, 650)

        self.setup_ui()

    def setup_ui(self):

        layout = QVBoxLayout()

        self.title = QLabel("🌦 Weather App Pro")
        self.title.setObjectName("title")

        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText(
            "Enter City Name"
        )

        self.search_btn = QPushButton(
            "Search Weather"
        )

        self.search_btn.clicked.connect(
            self.get_weather
        )

        self.temp_label = QLabel("--°C")
        self.temp_label.setObjectName("temp")

        self.weather_label = QLabel(
            "Condition"
        )

        self.humidity_label = QLabel(
            "Humidity"
        )

        self.wind_label = QLabel(
            "Wind Speed"
        )

        self.feels_like_label = QLabel(
            "Feels Like"
        )

        self.pressure_label = QLabel(
            "Pressure"
        )

        self.sunrise_label = QLabel(
            "Sunrise"
        )

        self.sunset_label = QLabel(
            "Sunset"
        )

        layout.addWidget(self.title)
        layout.addWidget(self.city_input)
        layout.addWidget(self.search_btn)

        layout.addWidget(self.temp_label)
        layout.addWidget(self.weather_label)

        layout.addWidget(self.feels_like_label)
        layout.addWidget(self.humidity_label)
        layout.addWidget(self.wind_label)

        layout.addWidget(self.pressure_label)
        layout.addWidget(self.sunrise_label)
        layout.addWidget(self.sunset_label)

        self.setLayout(layout)

        self.setStyleSheet("""
        QWidget{
            background:#1E1E1E;
            color:white;
            font-family:Segoe UI;
        }

        QLineEdit{
            background:#2D2D2D;
            color:white;
            padding:12px;
            border-radius:10px;
            font-size:16px;
        }

        QPushButton{
            background:#2196F3;
            color:white;
            padding:12px;
            border:none;
            border-radius:10px;
            font-size:16px;
        }

        QPushButton:hover{
            background:#1976D2;
        }

        QLabel#title{
            font-size:28px;
            font-weight:bold;
        }

        QLabel#temp{
            font-size:60px;
            font-weight:bold;
        }

        QLabel{
            font-size:18px;
            padding:4px;
        }
        """)

    def get_weather(self):

        city = self.city_input.text().strip()

        if city == "":
            return

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
            "&units=metric"
        )

        try:

            response = requests.get(url)

            data = response.json()

            if response.status_code != 200:

                self.temp_label.setText("Error")
                self.weather_label.setText(
                    "City Not Found"
                )

                return

            temp = data["main"]["temp"]

            feels_like = data["main"][
                "feels_like"
            ]

            humidity = data["main"][
                "humidity"
            ]

            pressure = data["main"][
                "pressure"
            ]

            wind = data["wind"]["speed"]

            condition = data["weather"][0][
                "description"
            ]

            sunrise = data["sys"][
                "sunrise"
            ]

            sunset = data["sys"][
                "sunset"
            ]

            sunrise_time = datetime.fromtimestamp(
                sunrise
            ).strftime("%I:%M %p")

            sunset_time = datetime.fromtimestamp(
                sunset
            ).strftime("%I:%M %p")

            self.temp_label.setText(
                f"{temp} °C"
            )

            self.weather_label.setText(
                f"Condition : {condition.title()}"
            )

            self.feels_like_label.setText(
                f"Feels Like : {feels_like} °C"
            )

            self.humidity_label.setText(
                f"Humidity : {humidity}%"
            )

            self.wind_label.setText(
                f"Wind Speed : {wind} m/s"
            )

            self.pressure_label.setText(
                f"Pressure : {pressure} hPa"
            )

            self.sunrise_label.setText(
                f"Sunrise : {sunrise_time}"
            )

            self.sunset_label.setText(
                f"Sunset : {sunset_time}"
            )

        except Exception as e:

            self.temp_label.setText(
                "Error"
            )

            self.weather_label.setText(
                str(e)
            )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = WeatherApp()
    window.show()

    sys.exit(app.exec())