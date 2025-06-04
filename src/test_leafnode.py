import unittest

from leafnode import LeafNode

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