from __init__ import app, db
import logging

class Landscape(db.Model):
    __tablename__ = 'landscapes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, country, city, description):
        self.name = name
        self.country = country
        self.city = city
        self.description = description

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error creating landscape: {str(e)}")
            return None

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error deleting landscape: {str(e)}")
            raise e

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'country': self.country,
            'city': self.city,
            'description': self.description
        }

def initLandscape():
    """
    The initLandscape function creates the Landscape table and adds tester data to the table.

    Uses:
        The db ORM methods to create the table.
    """
    try:
        db.create_all()

        # Check if data already exists
        if not Landscape.query.first():
            landscapes = [
                Landscape(
                    name="Grand Canyon",
                    country="USA",
                    city="Arizona",
                    description="A steep-sided canyon carved by the Colorado River."
                ),
                Landscape(
                    name="Great Wall of China",
                    country="China",
                    city="Beijing",
                    description="A series of fortifications made of stone, brick, tamped earth, wood, and other materials."
                ),
                Landscape(
                    name="Eiffel Tower",
                    country="France",
                    city="Paris",
                    description="A wrought-iron lattice tower on the Champ de Mars in Paris, France."
                )
            ]
            for landscape in landscapes:
                landscape.create()

        logging.info("Landscape table initialized and seeded successfully.")
    except Exception as e:
        logging.error(f"Error initializing Landscape table: {e}")
        raise e