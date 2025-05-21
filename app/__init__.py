import os
from flask import Flask
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)

    # Read Mongo URI from environment variable
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/mydatabase")

    # Initialize Mongo client
    mongo_client = MongoClient(mongo_uri)
    app.mongo_db = mongo_client.get_default_database()

    from .routes import main
    app.register_blueprint(main)

    return app

