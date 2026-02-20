import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        node1 = HTMLNode("a", "This is a link text.", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_props2(self):
        node2 = HTMLNode("p", "This is a paragraph.", None, None)
        self.assertEqual(node2.props_to_html(), "")

    def test_props3(self):
        node1 = HTMLNode("a", "This is a link text.", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a paragraph.", None, None)
        node3 = HTMLNode("div", None, [node1, node2])
        self.assertEqual(node3.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
           
