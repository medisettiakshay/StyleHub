
from app.db import Base, SessionLocal, engine
from app.models import Product

products = [
    {
        "name": "Classic Denim Jacket",
        "description": "Classic everyday denim jacket",
        "price_cents": 4999,
        "category": "Jackets",
        "stock": 20,
        "image_url": None,
    },
    {
        "name": "Minimal White Tee",
        "description": "Comfortable cotton white T-shirt",
        "price_cents": 1999,
        "category": "T-Shirts",
        "stock": 50,
        "image_url": None,
    },
    {
        "name": "Relaxed Cargo Pants",
        "description": "Relaxed fit utility cargo pants",
        "price_cents": 3599,
        "category": "Pants",
        "stock": 30,
        "image_url": None,
    },
    {
        "name": "Everyday Sneakers",
        "description": "Comfortable everyday sneakers",
        "price_cents": 5499,
        "category": "Footwear",
        "stock": 25,
        "image_url": None,
    },
]

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    existing = db.query(Product).count()

    if existing == 0:
        db.add_all([
            Product(**product)
            for product in products
        ])
        db.commit()
        print("Products inserted successfully!")
    else:
        print(f"Products already exist: {existing}")

finally:
    db.close()
