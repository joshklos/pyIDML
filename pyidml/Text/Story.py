from .Characters import Character
from .Paragraphs import Paragraph
from .Styles import TextStyles
from pyidml.helpers.parsers import get_style

import os
from lxml import etree


class Story(object):
    """Class to contain the base story object for icml

        Initial creation of the class builds a structure for a story
         Contains:
            id: a unique id that we set just to help identify a particular story
            characters: a collection of character objects
            paragraphs: a collection of paragraph objects
            contents: a generated string made up of the contents of the characters and paragraph breaks
            footnotes: a collection footnote objects
            itemLink: the source ICML file path and name if applicable
            name: a user set name for the story, defaults to the file name if it exists
            notes: a collection of note objects
            parent: a property that only exists if the story is coming from an IDML document (or you've created an IDML
                    document and passed it in). Added if an IDML document object is passed in
            words: Not actually implemented

        While this code is meant to mimix the InDesign JS object model, it does not contain all of the same features.
        I've left out many properties that exist for the story as they should be implemented as paragraph and character
        styles and not set as properties of a story"""
    def __init__(self, is_idml=False):
        self.id = 0
        self.characters = []
        self.contents = None
        self.footnotes = []
        self.itemLink = None
        self.name = None
        self.notes = []
        self.paragraphs = []
        self.paragraphStyles = TextStyles("Paragraph", "paragraph")
        self.characterStyles = TextStyles("Character", "character")
        self.filename = None
        if is_idml:
            self.parent = is_idml

    def add_paragraph(self, style="[Basic Paragraph]"):
        """Creates a new paragraph in the story"""
        para = Paragraph(len(self.paragraphs), style, self)
        self.paragraphs.append(para)
        return para

    def add_character(self, content, para, style="[None]"):
        """Adds character to story and paragraph"""
        char = Character(content, style, len(self.characters), para, self)
        para.characters.append(char)
        self.characters.append(char)

    def add_style_range(self, contents, para, style="[None]"):
        """Add a whole string that has the same character style (only for one paragraph at a time though)"""
        for char in contents:
            self.add_character(char, para, style)

    def generate_contents(self):
        contents_string = ""
        for char in self.characters:
            contents_string += char
        return contents_string

    def parse_story(self, icml):
        """Parses a string of ICML and sorts it into the class"""
        icml_root = icml.getroot()
        for tag in icml_root:
            if tag.tag == "Story":
                for para in tag:
                    # same_style_para is used to determine if we need to create a new para after a Br tag
                    same_style_para = False
                    if para.tag != "ParagraphStyleRange":
                        print("Expected a ParagraphStyleRangeTag received a " + para.tag + " instead.")
                    para_style = get_style(para.get("AppliedParagraphStyle"))
                    new_para = self.add_paragraph(para_style)
                    for style_range in para:
                        char_style = get_style(style_range.get("AppliedCharacterStyle"))
                        if same_style_para:
                            same_style_para = False
                            new_para = self.add_paragraph(para_style)
                        for content in style_range:
                            if content.tag == "Br":
                                same_style_para = True
                                continue
                            if content.text is not None:
                                self.add_style_range(content.text, new_para, char_style)

    def print_contents(self, with_style_prefixes=False):
        for para in self.paragraphs:
            para.print_contents(with_style_prefixes)


class Stories(list):
    def __init__(self):
        super().__init__()

    def new_story(self, file_or_string=None):
        new_story = Story()
        if file_or_string:
            if os.path.isfile(file_or_string):
                new_story.fileName = file_or_string
                parsed = etree.parse(file_or_string)
            else:
                new_story.fileName = None
                parsed = etree.fromstring(file_or_string)
            new_story.parse_story(parsed)
        self.append(new_story)
