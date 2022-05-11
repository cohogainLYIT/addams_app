from app import getaccomadation
import pytest

def test_getaccomadation(benchmark):
    benchmark(getaccomadation({ "reservation_name":"John Smith", "reservation_date":"07/02/2023", "guests":"4", "nice_to_have":"sea view"}))





