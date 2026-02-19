from enum import Enum
from typing import Optional

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMG = "image"

class TextNode():
    def __init__(self, text: String, text_type: TextType, url: Optional[String] = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: TextNode):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == self.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

