#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakery = []
    for baker in Bakery.query.all():
        baker_dic = {
            "id":baker.id,
            "name":baker.name,
            "created_at":baker.created_at
        
           }
        bakery.append(baker_dic)
    response = make_response(jsonify(bakery),200)

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    
    bakery_dict = {
        "id": bakery.id,
        "name":bakery.name,
        "created_at":bakery.created_at
    }
    response = make_response(bakery_dict, 200)

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    baked_list = []

    baked_goods =  BakedGood.query.order_by(BakedGood.price).all() 
      
    for baked in baked_goods:  
        baked_dict = {
            "id": baked.id,
            "name":baked.name,
            "price":baked.price,
            "created_at":baked.created_at
        }
        baked_list.append(baked_dict)

    response = make_response(jsonify(baked_list), 200)

    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
     
    baked_list = []
     
    baked_goods =  BakedGood.query.order_by(BakedGood.price.desc()).limit(1).all() 
    
    for baked in baked_goods:  
        baked_dict = {
            "id": baked.id,
            "name":baked.name,
            "price":baked.price
        }
        baked_list.append(baked_dict)

    response = make_response(jsonify(baked_list), 200)

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
