from textnode import TextNode, TextType
import re

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

def extract_markdown_images(text):
    alt_text_pattern = r"(?<=\!\[)[\w\s]+(?=\])"
    image_pattern = r"(?<=\()[^\s]+(?=\))"
    alt_texts = re.findall(alt_text_pattern, text)
    images = re.findall(image_pattern, text)
    return list(zip(alt_texts, images))

def extract_markdown_links(text):
    url_pattern = r"(?<=\()[^\s]+(?=\))"
    anchor_text_pattern = r"(?<=\[)[\w\s]+(?=\])"
    anchors = re.findall(anchor_text_pattern, text)
    urls = re.findall(url_pattern, text)
    return list(zip(anchors, urls))
 
