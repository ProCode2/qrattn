from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.user import User
from models.clas import Class
import json

index_routes = Blueprint('main', __name__, template_folder='templates')

@index_routes.route('/')
def index():
    classes = []

    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        user = User.query.filter_by(name=str(current_user)).first()
        class_ids = json.loads(user.class_ids)["ids"]
        print(class_ids)
        for id in class_ids:
            classes.append(Class.query.filter_by(id = id).first())
    print(classes)
    return render_template("index.html", classes=classes)

@index_routes.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)
