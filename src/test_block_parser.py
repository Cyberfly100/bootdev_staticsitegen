import unittest
from block_parser import markdown_to_blocks, BlockType, block_to_block_type

class TestBlockParser(unittest.TestCase):
    def test_markdown_to_blocks1(self):
        markdown  = '''
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
'''
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ],
            blocks
        )

    def test_markdown_to_blocks2(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks3(self):
        md = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            ],
        )

    def test_block_to_block_type1(self):
        blocks = [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ]
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertListEqual(
            [
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.UNORDERED_LIST
            ],
            block_types
        )
 
    def test_block_to_block_type2(self):
        blocks = [
            "```\nThis is a code block.\nIt can have many lines,\n and {[]}: symbols.\n```",
            "## Heading2",
            "# Heading1",
            "### Heading3",
            "###### Heading6",
            "> Before you criticize someone,\n>walk a mile in their shoes.\n> That way, you'll be a mile from them,\n> and you'll have their shoes.",
            "9993. This is a list\n9994. with items\n9995. It is ordered.",
        ]
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertListEqual(
            [
                BlockType.CODE,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.QUOTE,
                BlockType.ORDERED_LIST
            ],
            block_types
        )
        
    def test_block_to_block_type3(self):
        blocks = [
            "``\nThis is a NOT code block.\nIt can have many lines,\n and {[]}: symbols.\n```",
            "##NOT a Heading",
            "####### NOT a Heading",
            "### Heading3",
            "> Before you criticize someone,\nwalk a mile in their shoes.\n> That way, you'll be a mile from them,\n> and you'll have their shoes.",
            "9993. This is a list\n9999. with items\n9995. It is ordered.",
            "- This is NOT a list\n-with items\n- It is ordered.",
        ]
        block_types = [block_to_block_type(block) for block in blocks]
        self.assertListEqual(
            [
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.HEADING,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
            block_types
        )
 

if __name__ == "__main__":
    unittest.main()
