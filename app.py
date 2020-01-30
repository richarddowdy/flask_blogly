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
    new_user_image = request.form.get('new_user_image')
    if new_user_image == '':
        new_user_image = 'https://media.alienwarearena.com/media/1327-m.jpg'

    user = Users(first_name=new_first_name, last_name=new_last_name, image_url=new_user_image)

    db.session.add(user)
    db.session.commit()


    print(new_first_name,new_last_name, new_user_image)

    return redirect('/')


@app.route('/user/<int:user_id>')
def user_profile(user_id):
    
    user = Users.query.get(user_id)

    return render_template('user_profile.html', user=user)




@app.route('/user/<int:user_id>/edit')
def edit_user_profile(user_id):

    user = Users.query.get(user_id)

    return render_template("edit_user.html", user=user)

@app.route('/user/<int:user_id>/edit', methods=['POST'])
def save_edited_profile(user_id):

    user = Users.query.get(user_id)

    user.first_name = request.form['edited_first_name']
    user.last_name = request.form['edited_last_name']
    user.image_url = request.form.get('edited_user_image')

    db.session.add(user)
    db.session.commit()

    print(user.first_name, user.last_name, user.image_url)

    return redirect(f'/user/{user.id}')


@app.route('/user/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    print('*****', user_id)
    user = Users.query.get(user_id)

    db.session.delete(user)
    db.session.commit()
    return redirect('/')
