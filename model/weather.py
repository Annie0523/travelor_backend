from __init__ import app, db
import logging

class Weather(db.Model):
    __tablename__ = 'weathers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    temperature = db.Column(db.String(255), nullable=False)
    feelslike = db.Column(db.String(255), nullable=False)
    humidity = db.Column(db.String(255), nullable=False)
    pressure = db.Column(db.String(255), nullable=False)
    windspeed = db.Column(db.String(255), nullable=False)
    winddirection = db.Column(db.String(255), nullable=False)

    def __init__(self, name, temperature, feelslike, humidity, pressure, windspeed, winddirection):
        self.name = name
        self.temperature = temperature
        self.feelslike = feelslike
        self.humidity = humidity
        self.pressure = pressure
        self.windspeed = windspeed
        self.winddirection = winddirection

    def create(self):
        """Insert this Weather entry into the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error creating weather: {str(e)}")
            return None
        return self

    def delete(self):
        """Delete this Weather from the database."""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error deleting weather: {str(e)}")
            raise e

    def read(self):
        """Return a dict representation of this record."""
        return {
            'id': self.id,
            'name': self.name,
            'temperature': self.temperature,
            'feelslike': self.feelslike,
            'humidity': self.humidity,
            'pressure': self.pressure,
            'windspeed': self.windspeed,
            'winddirection': self.winddirection
        }

    @staticmethod
    def restore(data):
        """
        Bulk-restore Weather entries from a list of dictionaries.
        Typically called if you have a JSON backup.
        """
        try:
            for item in data:
                existing_weather = Weather.query.filter_by(
                    name=item['name'],
                    temperature=item['temperature'],
                    feelslike=item['feelslike'],
                    humidity=item['humidity'],
                    pressure=item['pressure'],
                    windspeed=item['windspeed'],
                    winddirection=item['winddirection']
                ).first()

                if not existing_weather:
                    weather = Weather(
                        name=item['name'],
                        temperature=item['temperature'],
                        feelslike=item['feelslike'],
                        humidity=item['humidity'],
                        pressure=item['pressure'],
                        windspeed=item['windspeed'],
                        winddirection=item['winddirection']
                    )
                    db.session.add(weather)

            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error restoring weathers: {str(e)}")
            return False


def initWeather():
    """
    The initWeather function creates the Weather table (if it doesn't exist)
    and adds tester data to the table.
    """
    try:
        db.create_all()
        # Add tester data
        if not Weather.query.first():
            weathers = [
                Weather(name="San Diego", temperature="20°C", feelslike="19°C", humidity="18%", pressure="1021 hPa", windspeed="3.6 m/s", winddirection="300°"),
                Weather(name="Tokyo", temperature="5°C", feelslike="4°C", humidity="55%", pressure="1020 hPa", windspeed="1.54 m/s", winddirection="200°"),
                Weather(name="Mumbai", temperature="24°C", feelslike="24°C", humidity="60%", pressure="1011 hPa", windspeed="1.37 m/s", winddirection="100°"),
                Weather(name="Cairo", temperature="14°C", feelslike="14°C", humidity="72%", pressure="1020 hPa", windspeed="0.51 m/s", winddirection="90°"),
                Weather(name="Lagos", temperature="24°C", feelslike="25°C", humidity="84%", pressure="1009 hPa", windspeed="1.72 m/s", winddirection="233°"),
                Weather(name="London", temperature="4°C", feelslike="1°C", humidity="86%", pressure="1037 hPa", windspeed="2.68 m/s", winddirection="259°"),
                Weather(name="Paris", temperature="-1°C", feelslike="-4°C", humidity="85%", pressure="1039 hPa", windspeed="2.06 m/s", winddirection="350°"),
                Weather(name="New York City", temperature="5°C", feelslike="1°C", humidity="53%", pressure="1013 hPa", windspeed="5.14 m/s", winddirection="260°"),
                Weather(name="Mexico City", temperature="23°C", feelslike="22°C", humidity="29%", pressure="1012 hPa", windspeed="1.34 m/s", winddirection="70°"),
                Weather(name="Sao Paulo", temperature="19°C", feelslike="19°C", humidity="79%", pressure="1012 hPa", windspeed="6.17 m/s", winddirection="160°")
            ]
            for weather in weathers:
                weather.create()
            logging.info("Weather table initialized and seeded.")
    except Exception as e:
        logging.error(f"Error initializing Weather table: {e}")
        raise e