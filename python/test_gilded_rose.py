# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, Item

# TODO: check out nested conditional refactoring first
# https://www.youtube.com/watch?v=fLaXlBVUb0c&ab_channel=EmilyBache


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


if __name__ == "__main__":
    unittest.main()
