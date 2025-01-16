from sqlite3 import IntegrityError
from __init__ import app, db


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    def __init__ (self, comment):
        self.comment = comment
    def create(self):
        
        try:
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.rollback()
            return None


def initComments():
    with app.app_context():
        
        c1 = Comment('I like to travel around the world')
        c2 = Comment('I usually travel in Asian countries')
        comments = [c1, c2] 
        
        for comment in comments:
            try:
                comment.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()

