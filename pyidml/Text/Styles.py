class ParagraphStyle(object):
    """Right now a basic holder for information about a paragraph style, to be fleshed out"""
    def __init__(self, name):
        self.name = name
        self.id = 0


class CharacterStyle(object):
    """Right now a basic holder for information about a character style, to be fleshed out"""
    def __init__(self, name):
        self.name = name
        self.id = 0


class TextStyles(object):
    """A collection of paragraph or character styles
    Styles are contained in a dictionary so they can be easily reference by name"""
    def __init__(self, name, type):
        """Creation of a styles group, takes a name and a type (either "paragraph" or "character")"""
        self.name = name
        self.styles = {}
        self.style_groups = {}
        self.type = type

    def new_style(self, name):
        if self.type == "paragraph":
            new_style = ParagraphStyle(name)
        else:
            new_style = CharacterStyle(name)

        self.styles[name] = new_style
        return new_style

    def get_style(self, *, by_name=False, by_id=None):
        if by_name:
            if by_name in self.style:
                return self.styles[by_name]
        if by_id is not None:
            for style_name in self.styles:
                if self.styles[style_name].id == by_id:
                    return self.styles[style_name]


class TextStyleRange(object):
    def __init__(self):
        self.characters = []
        self.content = ""
        self.appliedCharacterStyle = None

    def generate_contents(self):
        self.content = ""
        for char in self.characters:
            self.content += char.content
