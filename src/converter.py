from textnode import TextNode, TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    result = None
    match text_node.text_type:
        case TextType.TEXT:
            result = LeafNode(None, text_node.text)
        case TextType.BOLD:
            result = LeafNode("b", text_node.text)
        case TextType.ITALIC:
            result = LeafNode("i", text_node.text)
        case TextType.CODE:
            result = LeafNode("code", text_node.text)
        case TextType.LINK:
            result = LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            result = LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        case _:
            types = [e.value for e in TextType]
            raise Exception(f"Unexpected TextType. Valid options: {','.join(types)}")
    return result
