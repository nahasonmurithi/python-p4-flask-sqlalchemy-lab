from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    birthday = db.Column(db.DateTime)
    animals = db.relationship('Animal', backref = 'zookeeper' )
    #one-many 1 zookeepr many animals

class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    
    id = db.Column(db.Integer, primary_key=True)
    animals = db.relationship('Animal', backref = 'enclosure')
    # one enclosure many animals
    open_to_visitors = db.Column(db.Boolean)
    environment = db.Column(db.String)

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.String, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.String, db.ForeignKey('enclosures.id'))