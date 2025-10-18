
from text_to_html import text_node_to_html_node
from textnode import TextNode, TextType


def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

    node = TextNode("This is a bold text", TextType.BOLD)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "b")
    self.assertEqual(html_node.value, "This is a bold text")

    node = TextNode("This is an italic text", TextType.ITALIC)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "i")
    self.assertEqual(html_node.value, "This is an italic text")

    node = TextNode("This is a code text", TextType.CODE)
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "code")
    self.assertEqual(html_node.value, "This is a code text")    

    node = TextNode("This is a link", TextType.LINK, url="http://example.com")
    html_node = text_node_to_html_node(node)
    self.assertEqual(html_node.tag, "a")
    self.assertEqual(html_node.value, "This is a link")