import os as os


class pyIDML(object):
    # This class is used to hold and process IDML
    def __init__(self, idmlfile=False):
        # if idmlfile is provided will automatically parse idml file
        if idmlfile:
            self.fileName = idmlfile
            self.parse()
        else:
            self.fileName = None

    def parse(self):
        print("Parsing " + self.fileName)
        pass


class pyICML(object):
    # This class is used to hold and process ICML
    def __init__(self, fileOrString=False):
        # fileOrString, upon creation can parse a file or string of ICML
        if fileOrString:
            if os.path.isfile(fileOrString):
                self.fileName = fileOrString
                self.parse_file()
            else:
                self.fileName = None
                self.parse_string(fileOrString)
        else:
            self.fileName = None

    def parse_file(self):
        print("Parsing " + self.fileName)
        with open(self.fileName, "rt") as icmlFile:
            rawICML = icmlFile.read()
        self.parse_string(rawICML)
        pass

    def parse_string(self, rawICML):
        print("Parsing " + rawICML)
        pass

