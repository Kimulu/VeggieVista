from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fruit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discount = db.Column(db.String(20), nullable=True)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Fruit('{self.name}', '{self.discount}', '{self.image}')"

class Vegetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Vegetable('{self.name}', '{self.description}', '{self.price}', '{self.image}')"


class BestsellerProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<BestsellerProduct {self.name}>'