from annotators import must_be_professor
from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
import json

from models.clas import Class
from models.user import User
from db import db

classes = Blueprint("classes", __name__, template_folder="templates")

@classes.route("/class")
@login_required
@must_be_professor
def index():
  return render_template("add_class.html")

@classes.route("/class", methods=["POST"])
@login_required
@must_be_professor
def class_post():
  name = request.form.get("name")
  if not name:
    flash("Name is required")
    return redirect(url_for("classes.index"))
  cl = Class(name=name)
  db.session.add(cl)

  user = User.query.filter_by(name=str(current_user)).first()
  class_ids = json.loads(user.class_ids)

  class_ids["ids"].append(cl.id)
  print(cl.id)
  user.class_ids = json.dumps(class_ids)

  db.session.commit()

  return redirect(url_for("main.index"))
