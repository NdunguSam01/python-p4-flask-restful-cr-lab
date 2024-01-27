from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    image=db.Column(db.String)
    price=db.Column(db.DECIMAL(precision=10, scale=2))# Decimal column with 10 total digits and 2 decimal places
