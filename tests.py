import unittest
from htmlfile import AIRoFile, AIRoHTMLFile

import os


class UnitTests(unittest.TestCase):
    def test_greek_html_no_error(self):
        try:
            html_file = AIRoHTMLFile(os.path.join("", "cylaw_greek", "1995", "rep", "1995_1_0001.htm"))
            parsed = html_file.parse_to_text()
            # print(parsed)
            self.assertEqual("δικαιοδοτικών" in parsed, True)
        except:
            self.assertEqual(0,1)

    def test_latin_html_no_error(self):
        html_file = AIRoHTMLFile(os.path.join("", "CODICES-dataset-Hackathton_2024_11_15/ROM/rom-2006-3-003.htm"))
        parsed = (html_file.parse_to_text())
        self.assertEqual("Justiţie" in parsed, True)

if __name__ == "__main__":
    unittest.main()