#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakery = []
    for baker in Bakery.query.all():

        bakery_dic = baker.to_dict()
        bakery.append(bakery_dic)
    
    #make json more readable 
    # json_str = json.dumps(bakery, indent=4)
    response = make_response(jsonify(bakery),200)

    response.headers["Content-Type"] = "application/json"
   
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()
    
    bakery_dict = bakery.to_dict()

    json_str = json.dumps(bakery_dict, indent=4)
    
    response = make_response(json_str, 200)

    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():

    baked_list = []

    baked_goods =  BakedGood.query.order_by(BakedGood.price).all() 
      
    for baked in baked_goods:  

        baked_dic = baked.to_dict()
        baked_list.append(baked_dic)

    json_str = json.dumps(baked_list, indent=4)
   
    response = make_response(json_str, 200)

    response.headers["Content-Type"] = "application/json" 

    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
     
    baked_goods =  BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first() 
  
    baked_dict = baked_goods.to_dict()

    json_str = json.dumps(baked_dict, indent=4)

    response = make_response(json_str, 200)

    response.headers["Content-Type"] = "application/json" 

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
