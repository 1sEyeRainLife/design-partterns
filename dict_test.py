class A:
    def __init__(self, name):
        self.name = name
        self.__dict__.update({name: 'fanbin'})

    def __str__(self):
        return '{}'.format(self.name)

    def run(self):
        return 'run'


a = A('name_a')
print a.run()
print a.__dict__
print a.name_a
print a
