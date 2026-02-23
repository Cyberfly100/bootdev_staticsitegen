import unittest
from textnode import TextNode, TextType
from converter import text_node_to_html_node, markdown_to_html_node

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
        self.assertEqual(html_node.to_html(), '<img src="https://example.com/image.png" alt="This is the alt text."></img>')

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
## This is a heading with a **bold** word and a [link](https://example.com)

This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><h2>This is a heading with a <b>bold</b> word and a <a href="https://example.com">link</a></h2><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>',
        )

    def test_blockquote(self):
        md = """
> This is a blockquote with **bold** text and a [link](https://example.com)
> And this is still part of the blockquote with _italic_ text and `code`
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>This is a blockquote with <b>bold</b> text and a <a href="https://example.com">link</a>\nAnd this is still part of the blockquote with <i>italic</i> text and <code>code</code></blockquote></div>',
        )

    def test_lists(self):
        md = """
- Item 1
- Item 2
- ![Image text](https://imgurl.com/image.png)

34. Item 1
35. Item 2
36. Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li>Item 1</li><li>Item 2</li><li><img src="https://imgurl.com/image.png" alt="Image text"></img></li></ul><ol start="34"><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>',
        )

if __name__ == "__main__":
    unittest.main()
