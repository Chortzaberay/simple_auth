from flask import Blueprint
from flask import request, flash
from flask import redirect, url_for

from . import db
from .models import User
auth = Blueprint("auth", __name__)

def get_user_data():
    return{
        "name": request.form.get("name"),
        "passw": request.form["passw"],
        "passw2": request.form.get["passw2"],
        "email": request.form["email"]
    }


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method != "POST":
        return {"message": "not available"}, 200
    
    return {"message": "accepted"}, 200


@auth.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method != "POST":
        return {"message": "not available"}, 200
    user_ = get_user_data()
    if user_["passw"] != user_["passw2"]:
        flash("Password no match")
        return redirect("/signup")
    if user_["name"]:
        new_user = User(
            name=user_["name"],
            password=user_["passw"],
            email=user_["email"]
            )
        db.session.add(new_user)
        db.session.commit()

    return {"message": "accepted"}, 200
