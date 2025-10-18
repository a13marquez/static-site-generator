

def markdown_to_blocks(markdown_text):
    # Dummy implementation for illustration purposes
    new_lines = markdown_text.split('\n\n')
    blocks = []
    for line in new_lines:
        if len(line.strip()) > 0:
          blocks.append(line.strip())
  
  
   
    return blocks