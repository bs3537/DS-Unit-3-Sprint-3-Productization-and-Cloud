#from .routes import my_routes
#from .models import db

#migrate = Migrate()

#def create_app(config):
    #app = Flask(__name__)
    #app.config("SQLALCHEMY_DATABASE_URI") = "sqlite:///organized_lambdata.db"

    #app.register_blueprint(routes)

    #db.init_app(app)
    #migrate.init_app(app, db)

    #app.config["db"] = db

    #return app










from .app import create_app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)