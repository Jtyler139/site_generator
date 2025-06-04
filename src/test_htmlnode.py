import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode



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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")
    
    def test_None_props(self):
        child_node = LeafNode("span", "widdle baby")
        node = ParentNode("p", [child_node], None)
        self.assertEqual(node.to_html(), "<p><span>widdle baby</span></p>")

    def test_None_tag(self):
        child_node = LeafNode("b", "text go here", {"dic": "tionary"})
        node = ParentNode(None, [child_node], {"href": "www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_None_children(self):
        node = ParentNode("p", children=None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()