class Character(object):
    """Class to contain the basic building block of a story, individual characters

        Upon creation takes 5 arguments:
        content: The actual character itself
        char_style: The applied character style for this character (takes a string)
        para_style: The applied paragraph style for this character's parent paragraph (takes a string)
        id: An id number indicating the position of the character in a story
        parent: The parent paragraph object
    """
    def __init__(self, content, char_style, para_style, id, parent):
        self.content = content
        self.charStyle = char_style
        self.paraStyle = para_style
        self.id = id
        self.parentParagraph = parent
        