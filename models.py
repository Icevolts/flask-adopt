from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE = 'https://media.istockphoto.com/id/541833910/vector/dog-and-cat-icon.jpg?s=1024x1024&w=is&k=20&c=3G7SG82ybqcVBkjaODEpL-Gf3rv5ak6ufVXU1qVzAkg='

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    '''Pet info'''
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text,nullable = False)
    species = db.Column(db.Text, nullable = False)
    photo_url = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)

    def image(self):
        '''Return a stock photo if a picture wasn't provided'''
        return self.photo_url or DEFAULT_IMAGE