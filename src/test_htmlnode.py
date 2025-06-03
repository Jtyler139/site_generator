import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()