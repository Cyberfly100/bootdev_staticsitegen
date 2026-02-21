def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    stripped_blocks = [block.strip() for block in blocks if block]
    return stripped_blocks
   
