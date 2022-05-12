import os, sys
p = os.path.abspath('.')
sys.path.insert(0, p)

from app import app
import pytest
import datetime

def test_getaccomadation(benchmark):
    tester = app.app.test_client()
    benchmark(tester.post(
    '/getaccomodations',
    data = dict(reservation_name="John Smith", reservation_date=datetime.date.today(), guests=4, nice_to_have="balcony"),
    follow_redirects=True
    ))




