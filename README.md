# 🍕 Pizza API Challenge

A RESTful API built with Flask to manage restaurants, pizzas, and the relationship between them. This project follows the **MVC (Model-View-Controller)** pattern and uses **SQLAlchemy** for ORM and **Flask-Migrate** for database migrations.

---

## 🗂 Project Structure

.
├── server/
│ ├── init.py
│ ├── app.py
│ ├── config.py
│ ├── models/
│ │ ├── init.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
│ ├── seed.py
├── migrations/
├── challenge-1-pizzas.postman_collection.json
└── README.md

## 🚀 Setup Instructions

### 1. Clone the Repo and Navigate

### 2. Create and Activate a Virtual Environment
-pipenv install flask flask_sqlalchemy flask_migrate
-pipenv shell

### 3. Set Environment Variables

- export FLASK_APP=server/app.py
- export PYTHONPATH=.

## 🧱 Database Setup

### 1. Initialize and Migrate the Database

- flask db init
- flask db migrate -m "Initial migration"
- flask db upgrade

2. Seed the Database

PYTHONPATH=. python server/seed.py

You should now have initial restaurants and pizzas in the database.

## 🧪 API Endpoints

### 📍 GET /restaurants
Returns a list of all restaurants.

### 📍 GET /restaurants/<id>
Returns a single restaurant with its associated pizzas.

### 🗑 DELETE /restaurants/<id>
Deletes a restaurant and associated RestaurantPizzas.

### 📍 GET /pizzas
Returns a list of all pizzas.

### 🆕 POST /restaurant_pizzas
Creates a new record in the RestaurantPizza join table.

## ⚙️ Validation Rules
- RestaurantPizza.price must be between 1 and 30

- All foreign keys (pizza_id, restaurant_id) must point to valid records

- Deleting a Restaurant cascades delete to related RestaurantPizza entries

## 📬 Testing with Postman
- Open Postman

- Click Import

- Upload challenge-1-pizzas.postman_collection.json

- Run requests to test each endpoint

## 💡 Developer Notes
- The app uses PYTHONPATH=. when running scripts so Python can resolve the server/ package.

- app structure follows a strict MVC pattern:

  models/ → database models

  controllers/ → route handlers (blueprints)

  app.py → app entry point and glue

## Author

Brian Cheruiyot briancheruiyot6@gmail.com






