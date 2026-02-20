import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Link text", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Link text</a>')

    def test_leaf_to_html_missing_value(self):
        node = LeafNode("p", None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_leaf_to_html_plain(self):
        node = LeafNode(None, "Plain text")
        self.assertEqual(node.to_html(), "Plain text")


if __name__ == "__main__":
    unittest.main()
