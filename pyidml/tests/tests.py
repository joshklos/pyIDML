import unittest
import resources
from pyidml import pyIDML

class TestPyIDML(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_idml_extension(self):
        testIdml = pyIDML("Orthodoxy.idml")
        self.assertEqual(testIdml._inputType, "IDML")

    def test_icml_extension(self):
        testIdml = pyIDML("Chapter 1.icMl")
        self.assertEqual(testIdml._inputType, "ICML")

    def test_string_pass(self):
        testIdml = pyIDML(resources.contents)
        self.assertEqual(testIdml._inputType, "STRING")
