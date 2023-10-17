

class Parser:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def url(self, path: str, parameters: dict[any]) -> str:
        return self.base_url + "/" + self.substitute_parameters(path, parameters)
        pass

    def query(self):
        pass

    def substitute_parameters(self, path: str, parameters: dict[any]) -> str:
        return ""
        pass

    def to_string(self):
        pass

    def normalize_base_url(self):
        pass
