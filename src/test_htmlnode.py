import unittest

from htmlnode import HTMLNode, LeafNode



class TestHTMLNode(unittest.TestCase):
    def test_equal(self):
        node = HTMLNode("p", "This is the value text", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is the value text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_unequal(self):
        node = HTMLNode("p", "This is the value text", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "This is the value text", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_single_attr(self):
        node = HTMLNode(props={"href": "https://boot.dev"})
        expected = ' href="https://boot.dev"'
        assert node.props_to_html() == expected

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_value_None(self):
        node = LeafNode("a", None, {"href": "https://www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()            
    def test_tag_None(self):
        node = LeafNode(None, "This is a paragraph of text.", {"testy": "McTestFace"})
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

if __name__ == "__main__":
    unittest.main()