"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import db, connect_db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def root():

    users = Users.query.all()

    return render_template('list.html', users=users)

@app.route('/users/new')
def new_user_form():

    return render_template('new_user.html')

@app.route('/users/new', methods=['POST'])
def add_new_user_to_db():

    new_first_name = request.form['new_first_name']
    new_last_name = request.form['new_last_name']
    new_user_image = request.form['new_user_image']

    user = Users(first_name=new_first_name, last_name=new_last_name, image_url=new_user_image)

    db.session.add(user)
    db.session.commit()


    print(new_first_name,new_last_name, new_user_image)

    return redirect('/')


