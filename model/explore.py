from __init__ import app, db
import logging

class Explore(db.Model):
    __tablename__ = 'explores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    interest = db.Column(db.String(255), nullable=False)

    def __init__(self, name, value, position, category, interest):
        self.name = name
        self.value = value
        self.position = position
        self.category = category
        self.interest = interest

    def create(self):
        """Insert this Explore into the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error creating the map filter: {str(e)}")
            return None
        return self

    def delete(self):
        """Delete this Explore from the database."""
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error deleting map filter: {str(e)}")
            raise e

    def serialize(self):
        """Return object data in easily serializable format."""
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'position': self.position,
            'category': self.category,
            'interest': self.interest
        }

    def read(self):
        """Alias for serialize, if needed by other parts of your code."""
        return self.serialize()

    def update(self, data):
        """
        Update existing fields based on a dict 'data'.
        Example: data = {
            "name": "...",
            "value": "...",
            "position": "...",
            "category": "...",
            "interest": "..."
        }
        """
        try:
            for field in ["name", "value", "position", "category", "interest"]:
                if field in data:
                    setattr(self, field, data[field])
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error updating Explore: {str(e)}")
            return None

    @staticmethod
    def restore(data):
        """
        Re-inserts Explore records from a list of dictionaries (typically from backup).
        Only inserts records that don't exist already.
        """
        try:
            for item in data:
                existing_explore = Explore.query.filter_by(
                    name=item['name'],
                    value=item['value'],
                    position=item['position'],
                    category=item['category'],
                    interest=item['interest']
                ).first()

                if not existing_explore:
                    explore = Explore(
                        name=item['name'],
                        value=item['value'],
                        position=item['position'],
                        category=item['category'],
                        interest=item['interest']
                    )
                    db.session.add(explore)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error restoring explores: {str(e)}")
            return False


def initExplore():
    """
    Creates the 'explores' table (if it doesn't exist) and populates it with default data.
    Used for initial setup or re-initialization.
    """
    db.create_all()

    # Only add default data if the table is empty
    if not Explore.query.first():
        explores = [
            Explore(name="Tokyo", value="tokyo", position="35.6895, 139.6917", category="Modern",
                    interest="TOKYO:, technology, anime, Cherry Blossom, Temples, Shibuya"),
            Explore(name="Mumbai", value="mumbai", position="19.0760, 72.8777", category="Religious",
                    interest="MUMBAI:, bollywood, curry, Ganesh, Beaches, Elephants, Street Food, Taj Mahal"),
            Explore(name="Cairo", value="cairo", position="30.0444, 31.2357", category="historical",
                    interest="CAIRO:, pyramids, Egypt, Sphinx, Nile River, mosques"),
            Explore(name="Lagos", value="lagos", position="6.5244, 3.3792", category="Scenic",
                    interest="LAGOS:, afrobeat, Beaches, Nike Art gallery, Jazz, Nightlife, Makoko"),
            Explore(name="London", value="london", position="51.5074, -0.1278", category="historical",
                    interest="LONDON:, theatre, Buckingham Palace, Big Ben, King of England, Harry Potter, Tea"),
            Explore(name="Paris", value="paris", position="48.8566, 2.3522", category="cultural",
                    interest="PARIS:, fashion, Eiffel Tower, Louvre Museum, France, Baguette, Notre Dame Cathedral"),
            Explore(name="New York City", value="new_york_city", position="40.7128, -74.0060", category="Modern",
                    interest="NEW YORK CITY:, Empire State, Times Square, Central Park, Broadway, Statue of Liberty, Wall Street, 9/11 memorial, Brooklyn Bridge, pizza, hot dogsc"),
            Explore(name="Mexico City", value="mexico_city", position="19.4326, -99.1332", category="cultural",
                    interest="MEXICO CITY:, Hispanic, Volcanic horizons, Day of the dead, Mariachi, tacos, burritos, Lucha Libre"),
            Explore(name="Sao Paulo", value="sao_paulo", position="-23.5505, -46.6333", category="Natural",
                    interest="SAO PAULO:, Neon parties, Samba Beats, Soccer, Urban Jungles, party, Carnival, Brazil, Football, Street Art, Paulista Avenue, Beco do Batman"),
            Explore(name="Buenos Aires", value="buenos_aires", position="-34.6037, -58.3816", category="historical",
                    interest="BUENOS AIRES:, football, Argentina, Steak, La Boca Neighborhood, Tango, Cafe Culture, Palermo Park")
        ]
        for explore in explores:
            explore.create()