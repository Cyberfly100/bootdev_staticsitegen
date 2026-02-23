from textnode import TextNode, TextType
from htmlnode import LeafNode, ParentNode
from inline_parser import text_to_textnodes
from block_parser import BlockType, markdown_to_blocks, block_to_block_type, detect_heading

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
            result = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            types = [e.value for e in TextType]
            raise Exception(f"Unexpected TextType. Valid options: {','.join(types)}")
    return result

def strip_markdown_from_block(markdown_block: str) -> tuple[str, BlockType]:
    type = block_to_block_type(markdown_block)
    match type:
        case BlockType.PARAGRAPH:
            return markdown_block.replace("\n", " "), type
        case BlockType.HEADING:
            return markdown_block.strip("# "), type
        case BlockType.CODE:
            return markdown_block.lstrip("```\n").rstrip("```"), type
        case BlockType.QUOTE:
            return "\n".join([line.lstrip("> ") for line in markdown_block.split("\n")]), type
        case BlockType.UNORDERED_LIST:
            return "\n".join([line.lstrip("- ") for line in markdown_block.split("\n")]), type
        case BlockType.ORDERED_LIST:
            lines = markdown_block.split("\n")
            initial_number = int("".join([ch for ch in lines[0].split(".", 1)[0] if ch.isdigit()]))
            return " \n".join([line.lstrip(f"{initial_number + i}. ") for i, line in enumerate(lines)]), type
        case _:
            types = [e.value for e in BlockType]
            raise Exception(f"Unexpected BlockType. Valid options: {','.join(types)}")

def text_to_child_nodes(text: str) -> list[LeafNode]:
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        text_block, type= strip_markdown_from_block(block)
        match type:
            case BlockType.PARAGRAPH:
                child_nodes = text_to_child_nodes(text_block)
                nodes.append(ParentNode("p", child_nodes))
            case BlockType.HEADING:
                child_nodes = text_to_child_nodes(text_block)
                nodes.append(ParentNode(f"h{detect_heading(block)}", child_nodes))
            case BlockType.CODE:
                nodes.append(ParentNode("pre", [text_node_to_html_node(TextNode(text_block, TextType.CODE))]))
            case BlockType.QUOTE:
                child_nodes = text_to_child_nodes(text_block)
                nodes.append(ParentNode("blockquote", child_nodes))
            case BlockType.UNORDERED_LIST:
                child_nodes = [ParentNode("li", text_to_child_nodes(item.strip())) for item in text_block.split("\n")]
                nodes.append(ParentNode("ul", child_nodes))
            case BlockType.ORDERED_LIST:
                initial_number = int("".join([ch for ch in block.split(".", 1)[0] if ch.isdigit()]))
                child_nodes = [LeafNode("li", item.strip()) for item in text_block.split("\n")]
                nodes.append(ParentNode("ol", child_nodes, {"start": str(initial_number)}))
            case _:
                types = [e.value for e in BlockType]
                raise Exception(f"Unexpected BlockType. Valid options: {','.join(types)}")
    return ParentNode("div", nodes)