import string


class Parser:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def url(self, path: str, parameters: dict[any]) -> str:
        return self.base_url + "/" + self.substitute_parameters(path, parameters)
        pass

    def substitute_parameters(self, path: str, parameters: dict[any]) -> str:
        parts = path.split("/")
        result = []

        for part in parts:
            if part == None or part == "":
                continue

            name = ""
            if part.startswith(":"):
                name = part[1:]
            elif part.startswith("$"):
                pos = part.index("<")
                if pos != -1:
                    name = part[1:pos]
                else:
                    name = part[1:]
            elif part.startswith("{") and part.endswith("}"):
                name = part[1:len(part) - 1]

            if parameters[name]:
                part = self.to_string(parameters[name])

            result.append(part)

        return ",".join(result)
        pass

    def to_string(self, value: any) -> string:
        return "" + value
        pass
