import unittest

from block_to_blocktype import BlockType, block_to_blocktype
  
class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
       

        self.assertEqual(block_to_blocktype("This is a paragraph."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype("**Bold Text**"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_blocktype("- List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_blocktype("> Blockquote"), BlockType.QUOTE)
        self.assertEqual(block_to_blocktype("```code block```"), BlockType.CODE)

if __name__ == "__main__":
    unittest.main()