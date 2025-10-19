import re


def extract_title(markdown):
    title = re.match(r'# (.+)\n', markdown)
    if not title:
        raise Exception("No title found in the markdown content.")
    return title.group(1)