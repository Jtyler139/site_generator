from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
import os

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    new_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block != '':
            new_blocks.append(block)
    return new_blocks

def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith(('#', "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith('```') and lines[-1].endswith('```'):
        return BlockType.CODE
    
    if block.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE   
    
    if block.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    if block.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type is BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type is BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type is BlockType.CODE:
        return code_to_html_node(block)
    if block_type is BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)
    if block_type is BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type is BlockType.QUOTE:
        return quote_to_html_node(block)
    raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def extract_title(markdown):
    markdown_lines = markdown.split('\n')
    for line in markdown_lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("Missing Title")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as file:
        from_path_content = file.read()
    with open(template_path, "r") as file:
        template_path_content = file.read()
    html_node = markdown_to_html_node(from_path_content)
    html_string = html_node.to_html()
    title = extract_title(from_path_content)
    template_path_content = template_path_content.replace("{{ Title }}", title)
    template_path_content = template_path_content.replace("{{ Content }}", html_string)
    template_path_content = template_path_content.replace('href="/', f'href="{basepath}')
    template_path_content = template_path_content.replace('src="/', f'src="{basepath}')

    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    with open(dest_path, "w") as file:
        file.write(template_path_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    list_dir = os.listdir(dir_path_content)
    for item in list_dir:
        item_path = os.path.join(dir_path_content, item)
        dest_item_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            if item_path.endswith('.md'):
                dest_item_path = dest_item_path.replace('.md', '.html')
            generate_page(item_path, template_path, dest_item_path, basepath)
        else:
            generate_pages_recursive(item_path, template_path, dest_item_path, basepath)