# -*- coding:utf-8 -*-

import copy


class Prototype:
    value = 'default'

    def clone(self, **kwargs):
        """Clone a prototype and update inner attributes dictionary"""
        obj = copy.deepcopy(self)
        obj.__dict__.update(kwargs)
        return obj


class PrototypeDispatcher:
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category='a')
    b = prototype.clone(value='b-value', is_checked=True)
    dispatcher.register_object('objecta', a)
    dispatcher.register_object('objectb', b)
    dispatcher.register_object('objectc', d)
    print [{n: p.__dict__} for n, p in dispatcher.get_objects().items()]

if __name__ == '__main__':
    main()
