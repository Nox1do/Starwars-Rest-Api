"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import Characters, Planets, Favorites 

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def handle_hello():
    user = User.query.all()
    response_body = list(map(lambda user: user.serialize(), user))

    return jsonify(response_body), 200

#_____________________Characters______________
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Characters.query.all()
    all_characters = list(map(lambda character: character.serialize(), characters))
    return jsonify(all_characters), 200

#____________________Single Characters________
@app.route('/characters/<int:char_id>' , methods=['GET']) 
def single_character(char_id):
        character = Characters.query.get(char_id)
        return jsonify(character.serialize())   

#____________________Planets________
@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    all_planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(all_planets), 200

#____________________Single Planets________
@app.route('/planets/<int:plan_id>' , methods=['GET']) 
def single_planets(plan_id):
        planet = Planets.query.get(plan_id)
        return jsonify(planet.serialize())   

#________________Get Favorites___________
@app.route('/users/favorites', methods=['GET'])
def List_favorites():
    favorites = Favorites.query.all()
    all_favorites = list(map(lambda favorite: favorite.serialize(), favorites))
    return jsonify(all_favorites)


#____________create favorite planets____________#
  
@app.route('/favorites/planets/<plan_id>', methods=['POST'])
def add_planet_fav(planets_id):

    body = request.get_json()
    user_id = body["user_id"]

    planetfav = Favorites(
        user_id=user_id, plan_id=plan_id)
    db.session.add(planetfav)
    db.session.commit()
    return jsonify("ok"), 201

#_______create favorite characters(people)________#
@app.route('/favorites/characters/<char_id>', methods=['POST'])
def add_characters_fav(char_id):

    body = request.get_json()
    user_id = body["user_id"]
   

    characters_fav = Favorites(
        user_id=user_id, char_id=char_id)
    db.session.add(charactersfav)
    db.session.commit()
    return jsonify("ok"), 201

#____________DELETE FAVORIT____________#

@app.route('/favorites/planets/<plan_id>', methods=['DELETE'])
def delete_planet_fav(plan_id):

    planetfav = Favorites.query.get(plan_id)
    if plan_id is None:
        raise APIException("PLANET DELETE", 201)
    db.session.delete(planetfav)
    db.session.commit()

    return jsonify(planetfav.serialize())


@app.route('/favorites/characters/<char_id>', methods=['DELETE'])
def delete_characters_fav(char_id):

    charactersfav = Favorites.query.get(char_id)
    if char_id is None:
        raise APIException("PEOPLE DELETE", 201)
    db.session.delete(charactersfav)
    db.session.commit()

    return jsonify(charactersfav.serialize())





# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
