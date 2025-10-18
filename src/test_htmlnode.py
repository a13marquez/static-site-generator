import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        props = node.props_to_html()
        self.assertEqual(props, " class=\"container\"")
        node2 = HTMLNode("p", "This is a paragraph", [], {"id": "para1"})
        props2 = node2.props_to_html()
        self.assertEqual(props2, " id=\"para1\"")
        self.assertNotEqual(props, props2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode(None, "Just text")
        self.assertEqual(node2.to_html(), "Just text")
        node3 = LeafNode("span", "")
        with self.assertRaises(ValueError):
          node3.to_html()
        node4 = LeafNode("div", "this is a div")
        self.assertEqual(node4.to_html(), "<div>this is a div</div>")

    def test_parent_to_html_p(self):
      node = ParentNode(
        "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
        ],
      )
      result = node.to_html()
      self.assertEqual(result, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()