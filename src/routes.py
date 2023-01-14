from flask import Blueprint, current_app
from flask import request, flash
from flask import redirect, url_for
from flask import render_template

from flask_login import login_user, login_required
from flask_login import logout_user, current_user

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from . import db, login_manager
from .models import User
auth = Blueprint("auth", __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


def get_user_data():
    return{
        "name": request.form.get("name"),
        "passw": request.form["passw"],
        "passw2": request.form.get("passw2"),
        "email": request.form["email"]
    }


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method != "POST":
        return render_template("login.html")

    user_ = get_user_data()
    user = User.query.filter_by(email=user_["email"]).first()
    if not user:
        flash("Wrong password or login")
        return redirect(url_for("login"))
    if check_password_hash(user.password, user_["passw"]):
        login_user(user)
        
    next = request.args.get("next")
    return redirect(next or url_for("index"))


@auth.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method != "POST":
        return render_template("signup.html")
    user_ = get_user_data()
    if user_["passw"] != user_["passw2"]:
        flash("Password no match")
        return redirect("/signup")
    if user_["name"]:
        password = generate_password_hash(user_["passw"])
        new_user = User(
            name=user_["name"],
            password=password,
            email=user_["email"]
            )
        db.session.add(new_user)
        db.session.commit()

    return {"message": "accepted"}, 200


@auth.route("/profile")
@login_required
def profile():
    return {
        "message": f"-> {current_user.name}"
        }, 200


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))