from parsy import regex, seq, string, string_from


class ResponseParser:
    def __init__(self):
        # TODO: finish this parser to it does more than just parse indi and GPO reponses
        indi_operator = string_from("indi")
        gp_operator = string_from("GPO", "GPI")
        space = string(" ")
        obj = regex(r"[a-zA-Z0-9.#\[\]:/]*")
        name = regex(r"[a-zA-Z]*")
        simple_string = regex(r"[a-zA-Z ]*")
        equals = string("=")
        value = regex(r"[^,]*") | regex(r'".*"')
        number = regex(r"[0-9]+")
        gp_value = regex(r"[hl]").map(lambda v: {"h": False, "l": True}[v]) * 5

        indi_parser = seq(indi_operator << space).then(
            seq(
                path=obj << space.optional(),
                info=seq(name=name << equals, value=value << string(", ").optional())
                .map(lambda x: {x["name"]: x["value"]})
                .many()
                .map(lambda kv: {k: v for d in kv for k, v in d.items()}),
            )
        )
        gp_parser = seq(gp_operator << space).then(
            seq(number=number << space, pins=gp_value)
        )
        error_parser = seq(string("ERROR") << space).then(
            seq(number << space, simple_string)
        )

        self.p = indi_parser | gp_parser | error_parser

    def parse(self, string):
        return self.p.parse(string)
