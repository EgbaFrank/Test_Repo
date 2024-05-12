#!/usr/bin/env python3
"""
This module contains test cases of the item module
"""
import os
import sys
import json
import unittest
import datetime
from item import Item
from io import StringIO


class test_item(unittest.TestCase):
    def setUp(self):
        self.swissroll = Item("swissroll", 500, 10)
        self.filename = "item.txt"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_docs(self):
        mod_len = len(__import__("item").__doc__)
        cls_len = len(__import__("item").Item.__doc__)

        self.assertTrue(mod_len > 1)
        self.assertTrue(cls_len > 1)

    # Testing successes
    def test_init(self):
        self.assertEqual(self.swissroll.name, "swissroll")
        self.assertEqual(self.swissroll.price, 500)
        self.assertEqual(self.swissroll.quantity, 10)
        self.assertTrue(self.swissroll.id)
        self.assertTrue(self.swissroll.time_entered)
        self.assertTrue(Item.nb_items, 1)
        self.assertTrue(Item.current_datetime, datetime.datetime.now())

        self.swissroll.price = 0
        self.swissroll.quantity = 0

        self.assertEqual(self.swissroll.price, 0)
        self.assertEqual(self.swissroll.quantity, 0)

    def test_defaults(self):
        pen = Item("pen")

        self.assertEqual(pen.name, "pen")
        self.assertEqual(pen.price, 0)
        self.assertEqual(pen.quantity, 0)

    def test_get_total_value(self):
        self.assertEqual(self.swissroll.get_total_value(), 5000)

    def test_update_stock(self):
        self.swissroll.update_stock(5)

        self.assertEqual(self.swissroll.quantity, 15)

    # Testing exceptions
    def test_args_counts(self):
        with self.assertRaises(TypeError):
            eraser = Item()

        with self.assertRaises(TypeError):
            eraser = Item("name", 3, 4, 5)

    def test_args_types(self):
        with self.assertRaises(TypeError):
            eraser = Item(6, 3, 2)

        with self.assertRaises(TypeError):
            eraser = Item("name", "test", 3)

        with self.assertRaises(TypeError):
            eraser = Item("Test", 8, True)

    def test_args_value(self):
        with self.assertRaises(ValueError):
            eraser = Item("Test", -1, 21)

        with self.assertRaises(ValueError):
            eraser = Item("Test", 28, -2)

    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        print(self.swissroll)

        sys.stdout = sys.__stdout__

        printed_output = captured_output.getvalue().strip()

        self.assertEqual(str(self.swissroll), printed_output)

    def test_str(self):
        expected_str = f"Item name: {self.swissroll.name}\nItem price: {self.swissroll.price}\nItem quantity: {self.swissroll.quantity}"
        self.assertEqual(str(self.swissroll), expected_str)

    def test_to_json_string(self):
        test_list = [{"name": "pen", "price": 500, "quantity": 10}, {"name": "rule", "price": 100, "quantity": 5}]
        result = Item.to_json_string(test_list)
        self.assertEqual(result, '[{"name": "pen", "price": 500, "quantity": 10}, {"name": "rule", "price": 100, "quantity": 5}]')

        result = Item.to_json_string(None)
        self.assertEqual(result, "[]")

        result = Item.to_json_string([])
        self.assertEqual(result, "[]")

    def test_save_to_file(self):
        pen = Item("pen", 500, 10)
        Item.save_to_file([self.swissroll, pen])

        self.assertTrue(os.path.exists(self.filename))

        with open(self.filename, encoding="utf-8") as file:
            saved_data = json.load(file)
        self.assertEqual(saved_data, [self.swissroll.to_dict(), pen.to_dict()])
