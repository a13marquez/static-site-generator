import unittest

from extract_title import extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Title\nContent"), "Title")
        self.assertEqual(extract_title("# Another Title\nMore content"), "Another Title")
        with self.assertRaises(Exception):
            extract_title("No title here")

if __name__ == "__main__":
    unittest.main()