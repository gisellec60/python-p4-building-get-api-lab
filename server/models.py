from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialized_rules = ('-baked_goods.bakery')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)

    baked_goods = db.relationship('BakedGood', backref='bakery')

    def __repr__(self):
       return f'<Bakery: {self.name} was created at {self.created_at} and updated at {self.updated_at}>'

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialized_rules = ('-bakery.baked_goods')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    created_at = db.Column(db.String)
    updated_at = db.Column(db.String)
    
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    def __repr__(self):
       return f'<BakedGood: {self.name} the cost is {self.price} was created at {self.created_at} and updated at {self.updated_at}>'