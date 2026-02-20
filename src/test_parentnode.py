import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_children(self):
        grandchild = LeafNode("a", "Link text.", {"href": "https://www.google.com"})
        child1 = ParentNode("div", [grandchild])
        child2 = LeafNode("p", "Paragraph of text. Lorem ipsum dolor.", {"class": "centered"})
        parent = ParentNode("div", [child1, child2])
        self.assertEqual(
            parent.to_html(),
            '<div><div><a href="https://www.google.com">Link text.</a></div><p class="centered">Paragraph of text. Lorem ipsum dolor.</p></div>'
        )

    def test_to_html_no_children(self):
        parent = ParentNode("div", [])
        self.assertRaises(ValueError, parent.to_html)

    def test_to_html_no_tag(self):
        child = LeafNode("p", "Paragraph text.", {"class": "centered"})
        parent = ParentNode(None, [child])
        self.assertRaises(ValueError, parent.to_html)
        

if __name__ == "__main__":
    unittest.main()
