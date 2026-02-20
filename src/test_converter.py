import unittest
from textnode import TextNode, TextType
from converter import text_node_to_html_node

class TestConverter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_link(self):
        node = TextNode("This is the link text", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is the link text")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_img(self):
        node = TextNode("This is the alt text.", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "This is the alt text."})

if __name__ == "__main__":
    unittest.main()
