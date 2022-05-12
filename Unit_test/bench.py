import os, sys
p = os.path.abspath('.')
sys.path.insert(0, p)

from app import app
import pytest

def test_getaccomadation(benchmark):
    benchmark(getaccomodations({ "reservation_name":"John Smith", "reservation_date":"07/02/2023", "guests":"4", "nice_to_have":"sea view"}))
    print("Run")




