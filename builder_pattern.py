# -*- coding:utf-8 -*-
import time
from enum import Enum

Progress = Enum('Progress', 'queued preparation baking ready')
Dough = Enum('Dough', 'thin thick')
Sauce = Enum('Sauce', 'tomato')
Topping = Enum('Topping', 'bacon ham mash')
STEP_DELAY = 3


class Pizza(object):
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        time.sleep(STEP_DELAY)


class MarPizza(object):
    def __init__(self):
        self.pizza = Pizza('mar')
        self.progress = Progress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = Progress.preparation
        self.pizza.prepare_dough(Dough.thin)

    def add_sauce(self):
        self.pizza.sauce = Sauce.tomato
        time.sleep(STEP_DELAY)

    def add_topping(self):
        self.pizza.topping.append([i for i in (Topping.bacon,
                                               Topping.ham,
                                               Topping.mash)])

    def bake(self):
        self.progress = Progress.baking
        time.sleep(self.baking_time)
        self.progress = Progress.ready


class Waiter(object):
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce,
                             builder.add_topping,
                             builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('pizza_name:')
        print(pizza_style)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, %s' % err.message)
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MarPizza)
    print(builders)
    valid_input = False
    while not valid_input:
        print(valid_input)
        valid_input, builder = validate_style(builders)
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print('Enjoy your {}!'.format(pizza))

if __name__ == '__main__':
    main()
