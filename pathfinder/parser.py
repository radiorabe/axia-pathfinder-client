from parsy import regex, seq, string, string_from

from pathfinder.model import Object, ObjectPart


class ResponseParser:
    def __init__(self):
        # TODO: finish this parser to it does more than just parse indi reponses
        operator = string_from("indi")
        space = string(" ")
        dot = string(".")
        obj = regex(r"[a-zA-Z]*#[0-9a-zA-Z]*").map(lambda o: ObjectPart(o))
        name = regex(r"[a-zA-Z]*")
        equals = string("=")
        value = regex(r"[^,]*") | regex(r'".*"')

        self.p = seq(
            operator.map(lambda n: n.upper()) << space,
            obj.sep_by(dot, min=1).map(lambda o: Object(o)) << space.optional(),
            seq(name << equals, value).sep_by(string(", "), min=0).optional(),
        )

    def parse(self, string):
        r = self.p.parse(string)
        params = {}
        for v in r[2]:
            params[v[0]] = v[1]
        r[2] = params
        return r
