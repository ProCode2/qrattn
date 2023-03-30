from flask import Blueprint, render_template, abort, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from db import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(name=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page


    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here

    name = request.form.get('name')
    role = request.form.get('role')
    password = request.form.get('password')

    if not (role == 'student' or role == 'professor'):
      flash("Role can only be student or professor")
      return redirect(url_for('auth.signup'))

    user = User.query.filter_by(name=name).first()

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash("Email already exists")
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(name=name, password=generate_password_hash(password, method='sha256'), role=role)

    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
