from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite_people = db.relationship("FavoritePeople", backref="user", lazy=True)
    favorite_planets = db.relationship("FavoritePlanets", backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    birth_year = db.Column(db.Integer, unique=False, nullable=True)
    gender = db.Column(db.String, unique=False, nullable=False)
    eye_color = db.Column(db.String, unique=False, nullable=False)
    hair_color = db.Column(db.String, unique=False, nullable=False)
    favorite_people = db.relationship("FavoritePeople", backref="people", lazy=True)


    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    
class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_name = db.Column(db.String(120), db.ForeignKey("people.name"))
    user_email = db.Column(db.String(120), db.ForeignKey("user.email"))
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "people_name": self.people_name,
            "user_email": self.user_email
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    climate = db.Column(db.String, unique=False, nullable=False)
    gravity = db.Column(db.String, unique=False, nullable=False)
    population = db.Column(db.Integer, unique=False, nullable=False)
    terrain = db.Column(db.String, unique=False, nullable=False)
    favorite_planets = db.relationship("FavoritePlanets", backref="planets", lazy=True)


    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planets_name = db.Column(db.String(120), db.ForeignKey("planets.name"))
    user_email = db.Column(db.String(120), db.ForeignKey("user.email"))
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "planets_name": self.planets_name,
            "user_email": self.user_email
        }
