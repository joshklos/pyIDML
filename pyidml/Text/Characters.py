class Character(object):
    """Class to contain the basic building block of a story, individual characters

        Upon creation takes 5 arguments:
        content: The actual character itself
        char_style: The applied character style for this character (takes a string)
        para_style: The applied paragraph style for this character's parent paragraph (takes a string)
        index: An index number indicating the position of the character in a story
        parent: The parent paragraph object
    """
    def __init__(self, content, char_style, index, parent_para, parent_story):
        self.content = content
        self.appliedCharacterStyle = char_style
        self.appliedParagraphStyle = parent_para.appliedParagraphStyle
        self.index = index
        self.kerningValue = 0
        self.parentParagraph = parent_para
        self.parentStory = parent_story
