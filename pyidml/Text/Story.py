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
        if is_idml:
            self.parent = is_idml