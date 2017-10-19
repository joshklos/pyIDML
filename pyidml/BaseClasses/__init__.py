import os as os


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
    # This class is used to hold and process ICML
    def __init__(self, file_or_string=False):
        # fileOrString, upon creation can parse a file or string of ICML
        if file_or_string:
            if os.path.isfile(file_or_string):
                self.fileName = file_or_string
                self.parse_file()
            else:
                self.fileName = None
                self.parse_string(file_or_string)
        else:
            self.fileName = None

    def parse_file(self):
        print("Parsing " + self.fileName)
        with open(self.fileName, "rt") as icmlFile:
            raw_icml = icmlFile.read()
        self.parse_string(raw_icml)
        pass

    def parse_string(self, raw_icml):
        print("Parsing " + raw_icml)
        pass

