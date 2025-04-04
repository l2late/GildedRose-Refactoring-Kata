# -*- coding: utf-8 -*-

import pytest
from gilded_rose import GildedRose, Item


@pytest.fixture
def aged_brie():
    return Item("Aged Brie", 2, 0)


@pytest.fixture
def sulfuras():
    return Item("Sulfuras, Hand of Ragnaros", 0, 80)


@pytest.fixture
def backstage_pass():
    return Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)


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
    assert items[0].sell_in == -1


def test_given_an_item_foo_with_quality_2_and_sellin_1_when_update_quality_then_quality_is_not_0():
    items = [Item("foo", 1, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1
    assert items[0].sell_in == 0


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
