# server/seed.py
from server.models import db, Restaurant, Pizza, RestaurantPizza
from server.app import app

with app.app_context():
  db.drop_all()
  db.create_all()

  r1 = Restaurant(name="Domino's", address="123 Main St")
  r2 = Restaurant(name="Kiki's Pizza", address="address3")

  p1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
  p2 = Pizza(name="BBQ Chicken", ingredients="Dough, BBQ Sauce, Chicken")

  db.session.add_all([r1, r2, p1, p2])
  db.session.commit()

  rp1 = RestaurantPizza(price=10, pizza_id=p1.id, restaurant_id=r1.id)
  rp2 = RestaurantPizza(price=5, pizza_id=p1.id, restaurant_id=r2.id)

  db.session.add_all([rp1, rp2])
  db.session.commit()

  print("Seeded database successfully!")