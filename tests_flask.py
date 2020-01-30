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