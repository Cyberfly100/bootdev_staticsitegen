from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        segments = node.text.split(delimiter)
        if len(segments) % 2 == 0:
            raise Exception(f"Invalid markdown syntax detected. No match for delimiter {delimiter}.")
        for i, segment in enumerate(segments):
            if not segment:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(segment, TextType.TEXT))
            else:
                if text_type not in TextType:
                    raise Exception(f"Unknown text type: {text_type}.")
                new_nodes.append(TextNode(segment, text_type))
    return new_nodes
