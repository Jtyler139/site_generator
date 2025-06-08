import unittest

from splitnodes import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_expected_val(self):
        node = TextNode("Testing **bold** text", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(node_list, [TextNode("Testing ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" text", TextType.TEXT)])

    def test_end_delim(self):
        node = TextNode("Testing ending of string _here_", TextType.TEXT)
        node_list = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(node_list, [TextNode("Testing ending of string ", TextType.TEXT), TextNode("here", TextType.ITALIC)])
    
    def test_multi_node(self):
        node = TextNode("This is test **node** number one", TextType.TEXT)
        node2 = TextNode("This **here** is text node numbah two", TextType.TEXT)
        node_list = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(node_list, [TextNode("This is test ", TextType.TEXT), TextNode("node", TextType.BOLD), TextNode(" number one", TextType.TEXT), TextNode("This ", TextType.TEXT), TextNode("here", TextType.BOLD), TextNode(" is text node numbah two", TextType.TEXT)])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text that contains a [link](https://www.google.com)")
        self.assertListEqual([("link", "https://www.google.com")], matches)

if __name__ == "__main__":
    unittest.main()