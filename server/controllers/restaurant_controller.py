from flask import Blueprint, jsonify, request
from ..models import db, Restaurant, RestaurantPizza

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

@restaurants_bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    pizzas = [rp.pizza.to_dict() for rp in restaurant.pizzas]
    return jsonify({
        **restaurant.to_dict(),
        "pizzas": pizzas
    })

@restaurants_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204