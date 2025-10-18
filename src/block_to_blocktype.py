

from enum import Enum 
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_blocktype(block):
    header_pattern = re.compile(r'^#{1,6} ')
    if header_pattern.match(block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    else:
       lines = block.split('\n')
       if all(line.strip().startswith('- ') for line in lines):
           return BlockType.UNORDERED_LIST
       elif all(re.match(r'^\d+\. ', line.strip()) for line in lines):
           return BlockType.ORDERED_LIST
       elif block.startswith('> '):
           return BlockType.QUOTE
       else:
           return BlockType.PARAGRAPH
      