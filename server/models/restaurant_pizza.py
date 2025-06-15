from .. import db

class RestaurantPizza(db.Model):
  __tablename__ = 'restaurant_pizzas'

  id = db.Column(db.Integer, primary_key=True)
  price = db.Column(db.Integer, nullable=False)
  pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
  
  pizza = db.relationship('Pizza', back_populates='restaurants')
  restaurant = db.relationship('Restaurant', back_populates='pizzas')
  
  def to_dict(self):
    return {
      "id": self.id,
      "price": self.price,
      "pizza": self.pizza.to_dict(),
      "restaurant": self.restaurant.to_dict()
    }