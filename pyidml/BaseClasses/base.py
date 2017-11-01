import os as os
from pyidml.Text.Story import Stories
from pyidml.Text.Styles import TextStyles
from lxml import etree


class pyIDML(object):
    # This class is used to hold and process IDML
    def __init__(self, file_or_string=False):
        self.domVersion = "7.0"
        self.self = None
        self.accurateLABSpots = None
        self.activeLayer = None
        self.activeProcess = None
        self.afterBlendingIntent = None
        self.cmykPolicy = None
        self.cmykProfile = None
        self.cmykProfileList = None
        self.converted = None
        self.defaultImageIntent = None
        self.filePath = None
        self.fullName = None
        self.id = None
        self.modified = None
        self.name = None
        self.rgbPolicy = None
        self.rgbProfile = None
        self.rgbProfileList = None
        self.readOnly = None
        self.recovered = None
        self.saved = None
        self.solidColorIntent = None
        self.storyList = None
        self.transparencyAttributeDefaultProperty = None
        self.unusedSwatches = None
        self.visible = None
        self.zeroPoint = None
        self.properties = []
        self.stories = Stories()
        self.paragraphStyles = TextStyles("para_styles", "paragraph")
        self.characterStyles = TextStyles("char_styles", "character")
        self._inputType = None
        # if idmlfile is provided will automatically parse idml file
        if file_or_string:
            extension = file_or_string[-4:].lower()
            if extension == "idml":
                self._inputType = "IDML"
            elif extension == "icml":
                self._inputType = "ICML"
            else:
                self._inputType = "STRING"

    def parse(self):
        print("Parsing " + self.filePath)
        pass


class pyICML(object):
    """This is the base class used to hold and process ICML"""
    def __init__(self, file_or_string=False):
        """Creation of ICML object

        file_or_string can receive a file, a string, or nothing
        If nothing, creates an empty shell
        If it receives an ICML string it will attempt to parse the ICML string
        If it receive a file, it will attempt to parse the file"""
        self.paragraphStyles = TextStyles("Paragraph", "paragraph")
        self.characterStyles = TextStyles("Character", "character")
        self.stories = Stories()
        if file_or_string:
            self.stories.new_story(file_or_string)
