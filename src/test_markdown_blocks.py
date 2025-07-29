import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToHTTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )    


    def test_single_block(self):
        md = """
This is a single line markdown with **bolded** and _italic_ text
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["This is a single line markdown with **bolded** and _italic_ text"],
        )

    def test_multiple_new_line(self):
        md = """
This is the first paragraph

This is the second


This paragraph has an extra new_line
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is the first paragraph",
                "This is the second",
                "This paragraph has an extra new_line",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "### This is a heading"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "``` \nThis is some code Text\n ```"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> Dorothy followed her through many of the beautiful rooms in her castle.\n>\n> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood."

        new_block =block_to_block_type(block)
        self.assertEqual(new_block, BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- First item\n- Second item\n- Third item\n- Fourth item"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "I really like using Markdown.\n\nI think I'll use it to format all of my documents from now on."
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.PARAGRAPH)


    def test_block_to_block_type_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item\n4. Fourth item"
        new_block = block_to_block_type(block)
        self.assertEqual(new_block, BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()