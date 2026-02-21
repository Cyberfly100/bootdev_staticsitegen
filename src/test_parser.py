import unittest
from textnode import TextNode, TextType
from parser import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

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

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_nodes_image1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
           ],
            new_nodes,
        )

    def test_split_nodes_image2(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [Click me!](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a link [Click me!](https://www.google.com)", TextType.TEXT)
           ],
            new_nodes,
        )

    def test_split_nodes_link1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [Click me!](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link ", TextType.TEXT),
                TextNode("Click me!", TextType.LINK, "https://www.google.com")  
           ],
            new_nodes,
        )

    def test_split_nodes_image3(self):
        node = TextNode(
            "This is text with no images or links.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images or links.", TextType.TEXT)
            ],
            new_nodes
        )

    def test_split_nodes_link3(self):
        node = TextNode(
            "This is text with no images or links.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images or links.", TextType.TEXT)
            ],
            new_nodes
        )
 
    def test_text_to_textnodes1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
 
    def test_text_to_textnodes2(self):
        text = "This is text with no special features."
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            [TextNode("This is text with no special features.", TextType.TEXT)],
            nodes
        )
  

       
if __name__ == "__main__":
    unittest.main()
