
import unittest

class TestApp(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 1)

def test_suma():
    assert 2 + 2 == 4

def test_string():
    assert "docker".upper() == "DOCKER"