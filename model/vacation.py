from __init__ import app, db
import logging

class Vacation(db.Model):
    __tablename__ = 'vacations'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    climate = db.Column(db.String(255), nullable=False)  # Changed from 'city' to 'climate'
    country = db.Column(db.String(255), nullable=False)
    
    # Constructor
    def __init__(self, name, climate, country):
        self.name = name
        self.climate = climate
        self.country = country

    # Create method
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error creating vacation: {e}")
            raise e

    # Delete method
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error deleting vacation: {e}")
            raise e

    # Serialize method for JSON representation
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'climate': self.climate,
            'country': self.country
        }

# Function to initialize the database and seed it with tester data
def initVacation():
    """
    The initVacation function creates the Vacation table (if not already created)
    and populates it with test data.
    """
    try:
        db.create_all()

        # Check if data already exists
        if not Vacation.query.first():
            vacations = [
                Vacation(
                    name="Grand Canyon",
                    climate="Arid",
                    country="USA"
                ),
                Vacation(
                    name="Great Wall of China",
                    climate="Continental",
                    country="China"
                ),
                Vacation(
                    name="Eiffel Tower",
                    climate="Temperate",
                    country="France"
                )
            ]
            for vacation in vacations:
                vacation.create()

        logging.info("Vacation table initialized and seeded successfully.")
    except Exception as e:
        logging.error(f"Error initializing Vacation table: {e}")
        raise e
