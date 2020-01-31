"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy 
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Users(db.Model):
    """ User """

    __tablename__ = 'users'

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    
    first_name = db.Column(db.String(20),
                            nullable=False,
                            unique=False)
    
    last_name = db.Column(db.String(20),
                            nullable=False,
                            unique=False)

    image_url = db.Column(db.String(),
                            nullable=False,
                            unique=False,
                            default='https://media.alienwarearena.com/media/1327-m.jpg')


class Posts(db.Model):
    """ Post """

    __tablename__ = 'posts'

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    
    title = db.Column(db.String(100),
                            nullable=False,
                            unique=False)
    
    content = db.Column(db.String(),
                            nullable=False,
                            unique=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                            nullable=False,
                            unique=False)
    
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    user = db.relationship('Users', backref='posts')