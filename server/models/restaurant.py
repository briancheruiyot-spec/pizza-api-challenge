from .. import db

class Restaurant(db.Model):
  __tablename__ = 'restaurants'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), unique=True, nullable=False)
  address = db.Column(db.String(255), nullable=False)
  
  pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')
  
  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "address": self.address
    }