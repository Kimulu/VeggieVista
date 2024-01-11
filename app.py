# app.py

from flask import Flask, render_template
from models import db, Fruit, Vegetable, BestsellerProduct

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Adjust this based on your database setup
db.init_app(app)

with app.app_context():
    db.create_all()

    bestseller_data = [
        {"name": "Organic Tomato", "image_url": "img/best-product-1.jpg", "rating": 4.5, "price": 3.12},
        {"name": "Fresh Apple", "image_url": "img/best-product-2.jpg", "rating": 4.2, "price": 4.99},
        {"name": "Exotic Vegetable", "image_url": "img/best-product-3.jpg", "rating": 4.7, "price": 5.99},
        # Add more bestseller data as needed
    ]

    for product_info in bestseller_data:
        # Check if the product already exists in the database
        existing_product = BestsellerProduct.query.filter_by(name=product_info["name"]).first()
        if not existing_product:
            product = BestsellerProduct(
                name=product_info["name"],
                image_url=product_info["image_url"],
                rating=product_info["rating"],
                price=product_info["price"]
            )
            db.session.add(product)

    # Sample data for fruits
    fruit_data = [
        {"name": "Fresh Apples", "discount": "20% OFF", "image": "img/featur-1.jpg"},
        {"name": "Tasty Fruits", "discount": "Free delivery", "image": "img/featur-2.jpg"},
        {"name": "Exotic Vegitable", "discount": "Discount 30$", "image": "img/featur-3.jpg"},
    ]

    for fruit_info in fruit_data:
        # Check if the fruit already exists in the database
        existing_fruit = Fruit.query.filter_by(name=fruit_info["name"]).first()
        if not existing_fruit:
            fruit = Fruit(name=fruit_info["name"], discount=fruit_info["discount"], image=fruit_info["image"])
            db.session.add(fruit)

    # Sample data for vegetables
    vegetable_data = [
        {"name": "Parsely", "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit", "price": 4.99, "image": "img/vegetable-item-6.jpg"},
        {"name": "Bell Papper", "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit", "price": 7.99, "image": "img/vegetable-item-4.jpg"},
        {"name": "Potatoes", "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit", "price": 7.99, "image": "img/vegetable-item-5.jpg"},
    ]

    for vegetable_info in vegetable_data:
        # Check if the vegetable already exists in the database
        existing_vegetable = Vegetable.query.filter_by(name=vegetable_info["name"]).first()
        if not existing_vegetable:
            vegetable = Vegetable(
                name=vegetable_info["name"],
                description=vegetable_info["description"],
                price=vegetable_info["price"],
                image=vegetable_info["image"]
            )
            db.session.add(vegetable)

    db.session.commit()

@app.route('/')
def home():
    # Query all fruits and vegetables from the respective tables
    fruits = Fruit.query.all()
    vegetables = Vegetable.query.all()
    bestsellers = BestsellerProduct.query.all()
    return render_template('index.html', fruits=fruits, vegetables=vegetables, bestsellers=bestsellers)

if __name__ == '__main__':
    app.run(debug=True)
