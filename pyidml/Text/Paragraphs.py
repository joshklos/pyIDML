from .Styles import TextStyleRange


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
        self.content = ""
        self.footnotes = []
        self.parentStory = parent_story
        self.textStyleRanges = []

    def print_contents(self, with_style_prefixes=False):
        output = ""
        if self.content == "":
            self.generate_contents()
        if with_style_prefixes:
            output += "<"
            output += self.appliedParagraphStyle.name
            output += ">"
        output += self.content
        print(output)

    def generate_contents(self):
        self.content = ""
        for char in self.characters:
            self.content += char.content

    def generate_text_style_ranges(self):
        new_range = TextStyleRange()
        new_range.appliedCharacterStyle = self.characters[0].appliedCharacterStyle
        for char in self.characters:
            if char.appliedCharacterStyle == new_range.appliedCharacterStyle:
                new_range.characters.append(char)
            else:
                new_range.generate_contents()
                self.textStyleRanges.append(new_range)
                new_range = TextStyleRange()
                new_range.appliedCharacterStyle = char.appliedCharacterStyle
        new_range.generate_contents()
        self.textStyleRanges.append(new_range)

    def update(self):
        self.generate_contents()
        self.textStyleRanges = []
        self.generate_text_style_ranges()
