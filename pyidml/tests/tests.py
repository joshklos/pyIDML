import unittest
from .dummy_icml import contents as icml_contents
from pyidml import pyIDML
from pyidml.Text.BaseText import CommonText


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


class TestCommonText(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_boolean_setting(self):
        test_text = CommonText()
        test_text.hyphenation = True
        self.assertEqual(test_text.hyphenation, True)

    def test_boolean_not_boolean(self):
        with self.assertRaises(TypeError):
            test_text = CommonText()
            test_text.hyphenation = ["One", "Two"]

    def test_unset_boolean_is_none(self):
        test_text = CommonText()
        self.assertEqual(test_text.hyphenation, None)

    def test_setting_values(self):
        test_text = CommonText()
        test_text.properties_from_tag("yo")
