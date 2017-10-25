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


class TextStyles(list):
    """A collection of paragraph or character styles
    Styles are contained in a dictionary so they can be easily reference by name"""
    def __init__(self, name, type):
        """Creation of a styles group, takes a name and a type (either "paragraph" or "character")"""
        super().__init__()
        self.name = name
        self.style_groups = []
        self.type = type

    def new_style(self, name):
        if self.type == "paragraph":
            new_style = ParagraphStyle(name)
        else:
            new_style = CharacterStyle(name)

        self.append(new_style)
        return new_style

    def get_style(self, *, by_name=False, by_id=None):
        if by_name:
            for style in self:
                if by_name == style.name:
                    return style
        if by_id is not None:
            for style in self:
                if by_id == style.id:
                    return style
        return None

    def add_or_retrieve_style(self, name):
        if self.get_style(by_name=name) is not None:
            return self.get_style(by_name=name)
        return self.new_style(name)


class TextStyleRange(object):
    def __init__(self):
        self.characters = []
        self.content = ""
        self.appliedCharacterStyle = None

    def generate_contents(self):
        self.content = ""
        for char in self.characters:
            self.content += char.content

    def verify_integrity(self):
        if self.characters:
            char_style = self.characters[0].appliedCharacterStyle.name
            for char in self.characters:
                if char_style != char.appliedCharacterStyle.name:
                    return False
        return True
