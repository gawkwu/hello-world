from unittest import TestCase

from test import Rectangle


class TestRectangle(TestCase):
    def test_area_succeeds(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_succeeds(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)
