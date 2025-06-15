from flask import Blueprint, jsonify, request
from ..models import db, RestaurantPizza, Restaurant, Pizza

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validation
    if not all(key in data for key in ['price', 'pizza_id', 'restaurant_id']):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    try:
        price = int(data['price'])
        if not (1 <= price <= 30):
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"errors": ["Price must be an integer between 1 and 30"]}), 400
    
    # Check if restaurant and pizza exist
    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])
    
    if not restaurant or not pizza:
        return jsonify({"errors": ["Restaurant or Pizza not found"]}), 404
    
    # Create new association
    rp = RestaurantPizza(
        price=price,
        restaurant_id=restaurant.id,
        pizza_id=pizza.id
    )
    
    db.session.add(rp)
    db.session.commit()
    
    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza": pizza.to_dict(),
        "restaurant": restaurant.to_dict()
    }), 201