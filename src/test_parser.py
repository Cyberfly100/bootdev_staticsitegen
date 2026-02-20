import unittest
from textnode import TextNode, TextType
from parser import split_nodes_delimiter

class TestConverter(unittest.TestCase):
    def test_bold(self):
        old_node = TextNode("This is text with a **bold section**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                         [TextNode("This is text with a ", TextType.TEXT),
                          TextNode("bold section", TextType.BOLD)])

    def test_italic(self):
        old_node = TextNode("This is _italicised_ text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], '_', TextType.ITALIC)
        self.assertEqual(new_nodes,
                         [TextNode("This is ", TextType.TEXT),
                          TextNode("italicised", TextType.ITALIC),
                          TextNode(" text.", TextType.TEXT)])

    def test_code(self):
        old_node = TextNode("This is text with a `code block` word.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
                         [TextNode("This is text with a ", TextType.TEXT),
                          TextNode("code block", TextType.CODE),
                          TextNode(" word.", TextType.TEXT)])

    def test_multi(self):
        old_node = TextNode("This is some text with **bold** and _italic_ and ´code´ sections.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "´", TextType.CODE)
        self.assertEqual(new_nodes,
                         [TextNode("This is some text with ", TextType.TEXT),
                          TextNode("bold", TextType.BOLD),
                          TextNode(" and ", TextType.TEXT),
                          TextNode("italic", TextType.ITALIC),
                          TextNode(" and ", TextType.TEXT),
                          TextNode("code", TextType.CODE),
                          TextNode(" sections.", TextType.TEXT)])

if __name__ == "__main__":
    unittest.main()
