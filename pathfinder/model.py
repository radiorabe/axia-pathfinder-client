class ObjectPart:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "ObjectPart({0})".format(self.name)


class Object:
    def __init__(self, parts):
        self.parts = parts

    def __str__(self):
        return "Object(({0}))".format(", ".join(map(lambda o: str(o), self.parts)))
