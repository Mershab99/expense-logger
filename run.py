import logging
import os
from datetime import datetime as dt

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.resources import status

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
app.logger.info("Enabling CORS...")

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cars_api"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


CORS(app)
api = Api(app)

#Resources
api.add_resource(status.Status, '/status')

if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 80)))
    #DOCKER DEPLOYMENT
    #app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 80)))