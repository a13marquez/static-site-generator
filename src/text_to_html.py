from htmlnode import LeafNode, HTMLNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node:TextNode):
    if text_node.text_type is None:
        raise Exception("text_type is None")
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode("", text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return HTMLNode("a", text_node.text, href=text_node.url)
        case TextType.IMAGE:
            return HTMLNode("img", None, src=text_node.url, alt=text_node.Text)
        case _:
            raise Exception(f"Unknown TextType: {text_node.TextType}")