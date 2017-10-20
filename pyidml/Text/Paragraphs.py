class Paragraph(object):
    """Paragraph class

        Takes three arguments upon creation:
            index: The index for the position of the paragraph within the story
            para_style: the name of the paragraph style that applies to this paragraph
            parent_story: the parent story that this paragraph is a part of"""
    def __init__(self, index, para_style, parent_story):
        self.index = index
        self.appliedParagraphStyle = para_style
        self.contents = ""
        self.footnotes = []
        self.parentStory = parent_story
        self.textStyleRanges = []
