import os, sys
p = os.path.abspath('.')
sys.path.insert(0, p)

from Website.main import app
import unittest
import datetime

class FlaskTestCase(unittest.TestCase):
      
    def test_reservation_route(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """
        response = app.test_client().get('/')

        assert response.status_code == 200
        assert b"Reservations" in response.data
    
    def test_reservations(self):
        """
        GIVEN test data for booking
        WHEN the '/' page is requested (POST)
        THEN check that reservation was successful
        """
        tester = app.test_client(self)
        response = tester.post(
            '/',
            data = dict(reservation_name="test", reservation_date=datetime.date.today(), guests=100),
            follow_redirects=True
            )
        self.assertIn(b'Thank you for your booking!', response.data)