"""
Take not of these required imports for creating the table Drinks
>> from app import db
>> from app import app
>> from app import Drink
"""
import json
from flask import Flask, request
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return "Hello!"


@app.route('/drinks')
@app.route('/drinks/<id>')
def get_drinks():
    with app.app_context():
        drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return {"drinks": output}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    with app.app_context():
        db.session.add(drink)
        db.session.commit()
        return {'id': drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink():
    with app.app_context():
        drink = Drink.query.get(id)
        if not drink:
            return {"error": "not found"}
        db.session.delete(drink)
        db.session.commit()
        return {"message": "yay"}


app.run(debug=True)
