class ParagraphStyle(object):
    """Right now a basic holder for information about a paragraph style, to be fleshed out"""
    def __init__(self, name):
        self.name = name


class CharacterStyle(object):
    """Right now a basic holder for information about a character style, to be fleshed out"""
    def __init__(self, name):
        self.name = name


class TextStyles(object):
    """A collection of paragraph or character styles
    Styles are contained in a dictionary so they can be easily reference by name"""
    def __init__(self, name, type):
        """Creation of a styles group, takes a name and a type (either "paragraph" or "character")"""
        self.name = name
        self.styles = {}
        self.type = type

    def new(self, name):
        if self.type == "paragraph":
            new_style = ParagraphStyle(name)
        else:
            new_style = CharacterStyle(name)

        self.styles[name] = new_style
        return new_style

    def get_style(self, name):
        return self.styles[name]
