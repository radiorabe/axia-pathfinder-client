from pathfinder.model import ObjectPart


class TestObjectPartModel:
    def test_init(self):
        o = ObjectPart("Device#0")
        assert o.name == "Device#0"

    def test_str(self):
        o = ObjectPart("Device#0")
        assert str(o) == "ObjectPart(Device#0)"
