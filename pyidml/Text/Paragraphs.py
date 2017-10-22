class Paragraph(object):
    """Paragraph class

        Takes three arguments upon creation:
            index: The index for the position of the paragraph within the story
            para_style: the name of the paragraph style that applies to this paragraph
            parent_story: the parent story that this paragraph is a part of"""
    def __init__(self, index, para_style, parent_story):
        self.index = index
        self.appliedParagraphStyle = para_style
        self.characters = []
        self.contents = ""
        self.footnotes = []
        self.parentStory = parent_story
        self.textStyleRanges = []

    def print_contents(self, with_style_prefixes=False):
        output = ""
        if with_style_prefixes:
            output += "<"
            output += self.appliedParagraphStyle
            output += ">"
        for char in self.characters:
            output += char.content
        print(output)
