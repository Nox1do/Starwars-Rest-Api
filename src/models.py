from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#______________users model_________________
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
#______________Characters(people) model_________________
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    gender = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(10))
    skin_color = db.Column(db.String(80))
    hair_color = db.Column(db.String(120))
 
 
   
    
   
    # tell python how to print the class object on the console
    def __repr__(self):
        return '<Characters %r>' % self.name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "id": self.id,
            "Name": self.name,
            "Gender": self.gender,
            "Height": self.height,
            "Skin color": self.skin_color,
            "Hair color": self.hair_color,
          
          
        }
#______________Planets model_________________
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    gravity = db.Column(db.String(250)) 
    terrain = db.Column(db.String(250))

# tell python how to print the class object on the console
    def __repr__(self):
        return '<Planets %r>' % self.name

    # tell python how convert the class object into a dictionary ready to jsonify
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,              
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,          
        }


#     #_________Favorites char and plan model_________________
class Favorites(db.Model):
    __tablename__="favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user = db.relationship('User')
    characters = db.relationship('Characters')
    planets = db.relationship('Planets')

    def __repr__(self):
        return '<favorites %r>' % self.name
                #hace referencia al tablename
    def serialize(self):
        return {
            "id": self.id,
            "user id": self.user_id,
            "characters id": self.characters_id,
            "planets id": self.planets_id
        }
