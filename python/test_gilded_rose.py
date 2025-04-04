# -*- coding: utf-8 -*-

from gilded_rose import GildedRose, Item


def test_given_sulfuras_of_quality_80_when_update_quality_then_quality_80():
    items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 80


def test_given_sulfuras_of_quality_80_when_update_quality_trice_then_quality_80():
    items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert items[0].quality == 80
    assert items[0].sell_in == 1


def test_given_aged_brie_when_update_quality_then_quality_increases():
    items = [Item("Aged Brie", 2, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1


def test_given_aged_brie_of_quality_49_when_update_quality_then_quality_50():
    items = [Item("Aged Brie", 1, 49)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_given_aged_brie_of_quality_50_when_update_quality_then_quality_50():
    items = [Item("Aged Brie", 1, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50


def test_given_name_is_foo_when__is_set():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"


def test_given_an_item_foo_with_quality_1_when_update_quality_then_quality_is_0():
    items = [Item("foo", 0, 1)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_given_an_item_foo_with_quality_2_and_sellin_1_when_update_quality_then_quality_is_not_0():
    items = [Item("foo", 1, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1


def test_given_an_item_foo_with_quality_0_when_update_quality_then_quality_is_0():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_given_an_item_foo_with_sellin_1_when_update_quality_then_sell_in_is_0():
    items = [Item("foo", 1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 0


def test_given_an_item_foo_with_sellin_0_when_update_quality_then_sell_in_is_minus_1():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == -1


def test_given_an_item_foo_with_quality_0_when_update_quality_twice_then_quality_is_non_negative():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    assert items[0].quality > -1


def test_given_backstage_passes_with_quality_20_and_sellin_11_when_update_quality_then_quality_is_21():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 21


def test_given_backstage_passes_with_quality_20_and_sellin_10_when_update_quality_then_quality_increases_by_2():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 22


def test_given_backstage_passes_with_quality_20_and_sellin_5_when_update_quality_then_quality_increases_by_3():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 23


def test_given_backstage_passes_with_quality_20_and_sellin_0_when_update_quality_then_quality_is_0():
    items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_given_conjured_item_quality_decreases_by_2():
    items = [Item("Conjured", 10, 20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 18
