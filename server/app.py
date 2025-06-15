from flask import Flask, jsonify
from flask_migrate import Migrate
from .config import Config
from .models import db

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)
  
  db.init_app(app)
  migrate = Migrate(app, db)
  
  from .controllers.restaurant_controller import restaurants_bp
  from .controllers.pizza_controller import pizzas_bp
  from .controllers.restaurant_pizza_controller import restaurant_pizzas_bp
  
  app.register_blueprint(restaurants_bp)
  app.register_blueprint(pizzas_bp)
  app.register_blueprint(restaurant_pizzas_bp)
  
  @app.route('/')
  def index():
    return jsonify({"message": "Pizza Restaurant API"})
  
  return app

if __name__ == '__main__':
  app = create_app()
  app.run(port=5555, debug=True)