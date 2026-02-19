from htmlnode import HTMLNode

node1 = HTMLNode("a", "This is link text.", None, {"href": "https://www.google.com", "target": "_blank"})
node2 = HTMLNode("p", "This is a paragraph", None, None)
node3 = HTMLNode("div", None, [node1, node2])
node4 = HTMLNode("div", None, [node3])

print(node1)
print(node2)
print(node3)
print(node4)
