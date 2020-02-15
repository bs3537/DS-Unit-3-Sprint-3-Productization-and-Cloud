from flask import Blueprint, jsonify, request, render_template, current_app, redirect

from .models import User, Tweet, db

my_routes = Blueprint("my_routes", __name__)

#
# EXAMPLES
#

@my_routes.route("/")
def index():
    #return "Hello World!"
    return render_template("homepage.html")

@my_routes.route("/about")
def about():
    return "About Me"

# GET /hello
# GET /hello?name=Polly
@my_routes.route("/hello")
def hello(name=None):
    print("VISITING THE HELLO PAGE")
    print("REQUEST PARAMS:", dict(request.args))

    if "name" in request.args:
        name = request.args["name"]
        message = f"Hello, {name}"
    else:
        message = "Hello World"

    #return message
    return render_template("hello.html", message=message)

#
# USERS
#

@my_routes.route("/users")
@my_routes.route("/users.json")
def get_users():
    #users = [
    #    {"id":1, "name": "First User"},
    #    {"id":2, "name": "Second User"},
    #    {"id":3, "name": "Third User"},
    #]
    #return jsonify(users)

    users = User.query.all() # returns a list of <class 'alchemy.User'>
    print(type(users))
    #print(type(users[0]))
    #print(len(users))

    users_response = []
    for u in users:
        user_dict = u.__dict__
        del user_dict["_sa_instance_state"]
        users_response.append(user_dict)

    return jsonify(users_response)

@my_routes.route("/users/create", methods=["POST"])
def create_user():
    print("CREATING A NEW USER...")
    print("FORM DATA:", dict(request.form))
    # todo: create a new user
    #return jsonify({"message": "CREATED OK (TODO)"})
    if "name" in request.form:
        name = request.form["name"]
        print(name)
        db.session.add(User(name=name))
        db.session.commit()
        return jsonify({"message": "CREATED OK", "name": name})
    else:
        return jsonify({"message": "OOPS PLEASE SPECIFY A NAME!"})

#
# PREP
#

@my_routes.route("/do_stuff")
def do_stuff():

    #client = twitter_api_client()
    client = current_app.config["TWITTER_API_CLIENT"]
    user = client.me() # get information about the currently authenticated user
    print(user)
    print(type(user))
    return jsonify({"message": "OK"})