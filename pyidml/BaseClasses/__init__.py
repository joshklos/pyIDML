import os as os
from pyidml.Text.Story import Story
from lxml import etree

class pyIDML(object):
    # This class is used to hold and process IDML
    def __init__(self, idml_file=False):
        # if idmlfile is provided will automatically parse idml file
        if idml_file:
            self.fileName = idml_file
            if os.path.isfile(self.fileName):
                self.parse()
            else:
                print("File does not exist: " + self.fileName)
        else:
            self.fileName = None

    def parse(self):
        print("Parsing " + self.fileName)
        pass


class pyICML(object):
    """This is the base class used to hold and process ICML"""
    def __init__(self, file_or_string=False):
        """Creation of ICML object

        file_or_string can receive a file, a string, or nothing
        If nothing, creates an empty shell
        If it receives an ICML string it will attempt to parse the ICML string
        If it receive a file, it will attempt to parse the file"""
        self.paragraphStyles = []
        self.characterStyles = []
        self.story = Story()
        if file_or_string:
            if os.path.isfile(file_or_string):
                self.fileName = file_or_string
                self.parse_file()
            else:
                self.fileName = None
                parsed = etree.fromstring(file_or_string)
                self.story.parse_story(parsed)
        else:
            self.fileName = None

    def parse_file(self):
        print("Parsing " + self.fileName)
        parsed = etree.parse(self.fileName)
        self.story.parse_story(parsed)
        pass
