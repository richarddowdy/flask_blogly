from unittest import TestCase
from app import app
from flask import Flask


class BloglyViewsTestCase(TestCase):

    def test_list_page(self):
        with app.test_client() as client: 
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_add_user(self):
        with app.test_client() as client:

            resp = client.post('/users/new', data ={'new_first_name': 'Kyle', 'new_last_name': 'Test'})
            self.assertEqual(resp.status_code, 302)

    def test_updated_user_list(self):
        with app.test_client() as client:
            resp = client.post('/users/new', data ={'new_first_name': 'Kyle', 'new_last_name': 'Test'}, follow_redirects=True)

            html = resp.get_data(as_text=True)


            self.assertEqual(resp.status_code, 200)
            self.assertIn("Kyle Test", html)

    def test_user_profile(self):
        with app.test_client() as client:

            resp = client.get('/user/1')

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Adam Levitz</h1>", html)