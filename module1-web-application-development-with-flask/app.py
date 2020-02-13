#In class lecture code for 2/11/20
#pipenv install
#pipenv shell
#pipenv install Flask and other software imported below in pipenv first 
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlite3
app = Flask(__name__)

#Database building code for user data

app.config["CUSTOM_VAR"] = 5 # just an example of app config :-D
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///web_app.db"

#******CREATING DATABASE STEPS

#1. the following command generates app/migrations dir in anaconda prompt
#flask db init

#2. then run flask db.migrate in command line to create the database file (silence app.run() before it

#3. Run flask db.upgrade to populate the database with columns specified in the code below (here id, user name)

#4. Enter web_app.db in .gitignore file (since otherwise it will push changes to github everytime new entry made in database)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("name"))



#Routing code

@app.route("/")
def index():
    return render_template("homepage.html")

#These are GET requests
@app.route("/about")
def about():
    return "About me"
#pipenv install flask-jsonpify
#pipenv install jsonify

#routing code (app.route) can be be put also in a separate file
@app.route("/users)")
@app.route("/users.json")
def users():
    users = User.query.all() #get list of users in IP address/users.json url
    print(type(users))
    print(type(users[0]))

    users_response = []
    for u in users:
        user_dict = u.__dict__
        del user_dict["_sa_instance_state"]
        users_response.append(user_dict)

    return jsonify(users_response)

@app.route("/users/create", methods=["POST"])
def create_user():
    print("CREATING A NEW USER...")
    print("FORM DATA:", dict(request.form))

    #Example DB Code to enter new user name in db file (can add other fields like country etc. too)
    if "name" in request.form:
        name = request.form["name"]
        print(name)
        db.session.add(User(name=name))
        db.session.commit()
    
        return jsonify({"message": "Data entered OK", "name": name})
    else:
        return jsonify({"message": "Oops, error!"})




#*****To run app; enter flask run in anaconda prompt (doesn't need app.run() then

#silence app.run() before flask db.migrate command
#app.run()