from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    gender = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(10))
    skin_color = db.Column(db.String(80))
    hair_color = db.Column(db.String(120))
 
 
   
    
   
    # tell python how to print the class object on the console
    def __repr__(self):
        return '<Platano %r>' % self.name

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