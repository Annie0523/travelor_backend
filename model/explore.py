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
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error creating the map filter: {str(e)}")
            return None
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logging.warning(f"Error deleting map filter: {str(e)}")
            raise e

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'value': self.value,
            'position': self.position,
            'category': self.category,
            'interest': self.interest
        }

def initExplore():
    """
    The initexplore function creates the explore table and adds tester data to the table.

    Uses:
        The db ORM methods to create the table.
    """
    db.create_all()
    # Add tester data
    if not Explore.query.first():
        explores = [
    Explore(name="Tokyo", value="tokyo", position="35.6895, 139.6917", category="Modern", interest="TOKYO:, technology, anime, Cherry Blossom, Temples, Shibuya"),
    Explore(name="Mumbai", value="mumbai", position="19.0760, 72.8777", category="Religious", interest="MUMBAI:, bollywood, curry, Ganesh, Beaches, Elephants, Street Food, Taj Mahal"),
    Explore(name="Cairo", value="cairo", position="30.0444, 31.2357", category="historical", interest="CAIRO:, pyramids, Egypt, Sphinx, Nile River, mosques"),
    Explore(name="Lagos", value="lagos", position="6.5244, 3.3792", category="Scenic", interest="LAGOS:, afrobeat, Beaches, Nike Art gallery, Jazz, Nightlife, Makoko"),
    Explore(name="London", value="london", position="51.5074, -0.1278", category="historical", interest="LONDON:, theatre, Buckingham Palace, Big Ben, King of England, Harry Potter, Tea"),
    Explore(name="Paris", value="paris", position="48.8566, 2.3522", category="cultural", interest="PARIS:, fashion, Eiffel Tower, Louvre Museum, France, Baguette, Notre Dame Cathedral"),
    Explore(name="New York City", value="new_york_city", position="40.7128, -74.0060", category="Modern", interest="NEW YORK CITY:, Empire State, Times Square, Central Park, Broadway, Statue of Liberty, Wall Street, 9/11 memorial, Brooklyn Bridge, pizza, hot dogsc"),
    Explore(name="Mexico City", value="mexico_city", position="19.4326, -99.1332", category="cultural", interest="abc"),
    Explore(name="Sao Paulo", value="sao_paulo", position="-23.5505, -46.6333", category="Natural", interest="abc"),
    Explore(name="Buenos Aires", value="buenos_aires", position="-34.6037, -58.3816", category="historical", interest="abc")
]
        for explore in explores:
            explore.create()

