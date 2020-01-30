""" Seed file to make the data for users DB. """

from models import Users, Posts, db        
from app import app

"""Create all Tables"""
db.drop_all()
db.create_all()

# """Empty tables if they aren't already empty"""
# Users.query.delete()

# add dummy user data
adam = Users(first_name='Adam', last_name='Levitz', image_url='https://cdn-04.independent.ie/regionals/newrossstandard/lifestyle/3f1d5/37048554.ece/AUTOCROP/w620/2018-06-26_wex_42023220_I1.JPG')

richard = Users(first_name='Richard', last_name='Dowdy')

adam_post = Posts(title="Adam Test 1", 
                    content="Test post 1 for Adam User.", 
                    user_id=1)

richard_post = Posts(title="Richard Test 1",
                        content="Test post 1 for Richard user.",
                        user_id=2)

#add new instances to the session
db.session.add(adam)
db.session.add(richard)
db.session.add(adam_post)
db.session.add(richard_post)


#commit sessions
db.session.commit()