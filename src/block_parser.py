from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    stripped_blocks = [block.strip() for block in blocks if block]
    return stripped_blocks

def block_to_block_type(md_block) -> BlockType:
    block_type = BlockType.PARAGRAPH
    if md_block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        block_type = BlockType.HEADING
    elif md_block.startswith("```\n") and md_block.endswith("```"):
        block_type = BlockType.CODE
    elif all([line.startswith(">") for line in md_block.split("\n")]):
        block_type = BlockType.QUOTE
    elif all([line.startswith("- ") for line in md_block.split("\n")]):
        block_type = BlockType.UNORDERED_LIST 
    elif md_block[0].isdigit():
        lines = md_block.split("\n")
        initial_number = int("".join([ch for ch in lines[0] if ch.isdigit()]))
        if all([line.startswith(f"{initial_number + i}. ") for i, line in enumerate(lines)]):
            block_type = BlockType.ORDERED_LIST
    return block_type