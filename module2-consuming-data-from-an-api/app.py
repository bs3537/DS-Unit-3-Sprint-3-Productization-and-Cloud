#In class lecture code for 2/11/20
#pipenv install
#pipenv shell
#pipenv install Flask and other software imported below in pipenv first import os
from dotenv import load_dotenv
from flask import Flask #, jsonify, request, render_template
#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
import os
from .models import db, User, Tweet, migrate
#from .routes import routes
from .twitter_service import twitter_api_client
from .routes import my_routes
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

def create_app():
    #load_dotenv()
    #app_env = os.environ.get("FLASK_ENV", "development") # set to "production" in the production environment
    #secret_key = os.environ.get("SECRET_KEY", "my super secret") # overwrite this in the production environment
    #testing = False # True if app_env == "test" else False
    #app = Flask(__name__, instance_relative_config=True)
    #app.config.from_mapping(ENV=app_env, SECRET_KEY=secret_key, TESTING=testing)
    #app.register_blueprint(home_routes)
    #app.register_blueprint(product_routes)

    app = Flask(__name__)
    app.config["CUSTOM_VAR"] = 100 # just an example of app config :-D
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app_200.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["TWITTER_API_CLIENT"] = twitter_api_client()

    #db = SQLAlchemy(app)
    #migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app, db)
    #with app.app_context():
    #    db.create_all()

    

    app.register_blueprint(my_routes)

    return app