# server/controllers/restaurant_pizza_controller.py
from flask import Blueprint, jsonify, request
from server.models import db, RestaurantPizza, Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
  data = request.get_json()
  try:
    new_rp = RestaurantPizza(
      price=data['price'],
      pizza_id=data['pizza_id'],
      restaurant_id=data['restaurant_id']
    )
    db.session.add(new_rp)
    db.session.commit()

    return jsonify({
      'id': new_rp.id,
      'price': new_rp.price,
      'pizza_id': new_rp.pizza_id,
      'restaurant_id': new_rp.restaurant_id,
      'pizza': {
        'id': new_rp.pizza.id,
        'name': new_rp.pizza.name,
        'ingredients': new_rp.pizza.ingredients
      },
      'restaurant': {
        'id': new_rp.restaurant.id,
        'name': new_rp.restaurant.name,
        'address': new_rp.restaurant.address
      }
    }), 201
  except Exception as e:
    return jsonify({"errors": [str(e)]}), 400