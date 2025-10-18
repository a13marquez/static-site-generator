
import unittest

from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


class TestSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.PLAIN),
            ],
            new_nodes,
        )
        
        
if __name__ == "__main__":
    unittest.main()