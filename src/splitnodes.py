from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        new_list = []
        split_node = old_node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise ValueError("missing closing delimeter character")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 == 0:
                new_list.append(TextNode(split_node[i], TextType.TEXT))
            else:
                new_list.append(TextNode(split_node[i], text_type))
        new_nodes.extend(new_list)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

print(extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"))