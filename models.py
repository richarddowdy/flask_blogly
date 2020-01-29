"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy 

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
                            unique=True)
    
    last_name = db.Column(db.String(20),
                            nullable=False,
                            unique=True)

    image_url= db.Column(db.String(),
                            nullable=True,
                            unique=True)
                            # default=href='default_clown.jpg')