#from flask import Blueprint
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
#from ..emails import mail_message
from . import auth
from werkzeug.security import generate_password_hash, check_password_hash

#auth = Blueprint('auth',__name__)


@auth.route('/login')
def login():
  form = LoginForm()

  return render_template('auth/login.html', form=form)

@auth.route('/login', methods=['POST'])
def login_post():
  form = LoginForm()

  email = request.form.get('email')
  password = request.form.get('password')
  print(email)
  print(password)

  user = User.query.filter_by(email=email).first()

  if not user or not check_password_hash(user.password_secure, password):
    flash('please check your login details and try again')

    return render_template('auth/login.html', form=form)

  login_user(user, remember=True)

  return redirect(url_for('main.index'))

@auth.route('/register')
def register():
  form = RegistrationForm()

  return render_template('auth/register.html', form=form)

@auth.route('/register', methods = ['POST'])
def register_post():
  loginForm = LoginForm()
  registerForm = RegistrationForm()

  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')
  password_confirm = request.form.get('password_confirm')

  user = User.query.filter_by(email=email).first()

  if user:
    flash('Email address already exists')
    return render_template('auth/register.html', form=registerForm)

  if password != password_confirm:
    flash('Passwords don\'t match')
    return render_template('auth/register.html', form=registerForm)

  new_user = User(name=name, email=email, password_secure=generate_password_hash(password, method='sha256'))
  db.session.add(new_user)
  db.session.commit()

  login_user(new_user, remember=True)
  
  return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))
