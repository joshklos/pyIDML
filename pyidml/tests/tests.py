import unittest
from .dummy_icml import contents as icml_contents
from pyidml import pyIDML


class TestPyIDML(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_idml_extension(self):
        test_idml = pyIDML("Orthodoxy.idml")
        self.assertEqual(test_idml._inputType, "IDML")

    def test_icml_extension(self):
        test_idml = pyIDML("Chapter 1.icMl")
        self.assertEqual(test_idml._inputType, "ICML")

    def test_string_pass(self):
        test_idml = pyIDML(icml_contents)
        self.assertEqual(test_idml._inputType, "STRING")
        
