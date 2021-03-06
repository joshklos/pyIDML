import os as os
from pyidml.Text.Story import Stories
from pyidml.Text.Styles import TextStyles
from lxml import etree
import zipfile


class pyIDML(object):
    # This class is used to hold and process IDML
    def __init__(self, file_or_string=False):
        self.domVersion = "8.0"
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
                self.filePath = file_or_string
            elif extension == "icml":
                self._inputType = "ICML"
                self.filePath = file_or_string
            else:
                self._inputType = "STRING"

    def parse(self):
        if self._inputType == "IDML":
            self.parse_idml(self.filePath)
        pass

    def parse_idml(self, file_name):
        with zipfile.ZipFile(file_name, 'r') as idml_file:
            with idml_file.open('designmap.xml') as design_map:
                print(design_map.read())
