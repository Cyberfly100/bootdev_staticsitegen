class HTMLNode():
    def __init__(self, tag:str = None, value:str = None, children:list[HTMLNode | LeafNode | ParentNode] = None, props:dict[str:str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes should implement this method.")

    def props_to_html(self):
        if self.props == None:
            return ""
        props_strings = []
        for key, value in self.props.items():
            props_strings.append(f'{key}="{value}"')
        return " " + " ".join(props_strings)

    def __repr__(self):
        output = []
        if self.tag != None:
            output.append(f"  - tag: {self.tag}")
        if self.value != None:
            output.append(f"  - value: {self.value}")
        if self.children:
            children = []
            for child in self.children:
                new_child = []
                for i, line in enumerate(str(child).split("\n")):
                    if i == 0:
                        new_child.append(line)
                    else:
                        new_child.append(f"    {line}")
                children.append(f"    - {"\n".join(new_child)}")
            output.append(f"  - children:\n{"\n".join(children)}")
        if self.props:
            props = []
            for key, value in self.props.items():
                props.append(f"    - {key}: {value}")
            output.append(f"  - props:\n{"\n".join(props)}")
        return f'{type(self).__name__}:\n{"\n".join(output)}'

class LeafNode(HTMLNode):
    def __init__(self, tag:str, value:str, props:dict[str:str] = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode | LeafNode | ParentNode], props: dict[str:str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required for parent nodes.")
        if not self.children:
            raise ValueError("Children are required for parent node.")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>'
