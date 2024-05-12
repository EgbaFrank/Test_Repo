#!/usr/bin/env python3
"""
This module contains an item class
"""
import json
import uuid
import datetime

class Item:
    """This class houses the blueprint for an item object"""

    # A class attribute
    nb_items = 0
    current_datetime = datetime.datetime.now()

    def __init__(self, name, price, quantity):
        """ Initializes class attributes"""
        self.__id = str(uuid.uuid4())
        self.__time_entered = str(datetime.datetime.now())
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.nb_items += 1

    # ID attribute
    @property
    def id(self):
        """Gets the id attribute"""
        return self.__id

    # Time_entered attribute
    @property
    def time_entered(self):
        """Gets the time_entered attribute"""
        return self.__time_entered

    # Name attribute
    @property
    def name(self):
        """Gets the name attribute"""
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name attribute"""
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        self._name = name

    # Price attribute
    @property
    def price(self):
        """Gets price attribute"""
        return self._price

    @price.setter
    def price(self, price):
        """Sets price attribute"""
        if price < 0:
            raise ValueError("price cannot be negative")
        if type(price) is not int:
            raise TypeError("price should be a integer")
        self._price = price

    # Quantity attribute
    @property
    def quantity(self):
        """Gets quantity attribute"""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets quantity attribute"""
        if quantity < 0:
            raise ValueError("stock cannot be negative")
        if type(quantity) is not int:
            raise TypeError("stock should be an integer")
        self._quantity = quantity

    def update_stock(self, delta):
        """Raise stock quantity by delta"""
        self._quantity += delta

    def decrease_stock(self, delta):
        """Decreases stock quantity by delta"""
        self._quantity -= delta

    def get_total_value(self):
        """Calculates the total value of item in stock"""
        return self._price * self._quantity

    def __str__(self):
        """Overrides print, to print item attributes"""
        return f"Item name: {self._name}\nItem price: {self._price}\nItem quantity: {self._quantity}"

    def to_dict(self):
        """Return the dict representation of an instance"""
        return self.__dict__

    @staticmethod
    def to_json_string(dict_list):
        """Converts a list of dictionaries to a json string"""
        if dict_list is None:
            return "[]"

        return json.dumps(dict_list)

    @staticmethod
    def save_to_file(obj_list):
        if obj_list is None:
            obj_list = []

        dict_list = []

        for item in obj_list:
            dict_list.append(item.to_dict())

        jstr = Item.to_json_string(dict_list)

        with open("item.txt", "w", encoding='utf-8') as file:
            file.write(jstr)
