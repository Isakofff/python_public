# -*- coding: utf-8 -*-
__author__ = "Isakov Anton"

from utils import get_input_function


class Storage(object):  # storage = Storge()
    obj = None

    # store all 'to do' tasks
    items = None

    @classmethod
    def __new__(cls, *args):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
            cls.items = []
        return cls.obj


class BaseItem(object):
    def __init__(self, heading):
        self.heading = heading
        self.done = False

    def __repr__(self):
        return self.__class__

    @classmethod
    def construct(cls):
        raise NotImplemented()


class ToDoItem(BaseItem):
    def __str__(self):
        return f"{'+' if self.done else '-'} ToDo: {self.heading}"

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        return ToDoItem(heading)


class ToBuyItem(BaseItem):
    def __init__(self, heading, price):
        super(ToBuyItem, self).__init__(heading)
        self.price = price

    def __str__(self):
        return f"{'+' if self.done else '-'} ToBuy: {self.heading} for {self.price}"

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        price = input_function('Input price: ')
        return ToBuyItem(heading, price)

class ToReadItem(BaseItem):
    def __init__(self, heading, url):
        super(ToReadItem, self).__init__(heading)
        self.url = url

    def __str__(self):
        return f"{'+' if self.done else '-'} ToRead: {self.heading} for {self.url}"

    @classmethod
    def construct(cls):
        input_function = get_input_function()
        heading = input_function('Input heading: ')
        url = input_function('Input url: ')
        return ToReadItem(heading, url)