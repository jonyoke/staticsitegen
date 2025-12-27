import unittest

from textnode import *
from htmlnode import *
from nodefunctions import *
from markdownfunctions import *

class TestMarkdownFunctions(unittest.TestCase):

    """
    def test_block_to_block_type_heading(self):
        heading_md = "# Blah"
        print(heading_md)
        self.assertEqual(block_to_blocktype(heading_md), BlockType.HEADING)
        heading_md = "## Blah"
        print(heading_md)
        self.assertEqual(block_to_blocktype(heading_md), BlockType.HEADING)
        heading_md = "### Blah"
        print(heading_md)
        self.assertEqual(block_to_blocktype(heading_md), BlockType.HEADING)
        heading_md = "#### Blah"
        print(heading_md)
        self.assertEqual(block_to_blocktype(heading_md), BlockType.HEADING)
        heading_md = "##### Blah"
        print(heading_md)
        self.assertEqual(block_to_blocktype(heading_md), BlockType.HEADING)
        heading_md = "###### Blah"
        print(heading_md)
        self.assertEqual(block_to_blocktype(heading_md), BlockType.HEADING)

        
    def test_block_to_block_type_code(self):
        md = "```here is some code\nmore code\nmore code   ```"
        print(md)
        blocktype = block_to_blocktype(md)
        print(blocktype)
        self.assertEqual(blocktype, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        md = ">here is a quote\n>more quote\n>more quote   ```"
        print(md)
        blocktype = block_to_blocktype(md)
        print(blocktype)
        self.assertEqual(blocktype, BlockType.QUOTE)

    def test_block_to_block_type_ulist(self):
        md = "- here is a ulist\n- >more ulist\n- more ulist   ####"
        print(md)
        blocktype = block_to_blocktype(md)
        print(blocktype)
        self.assertEqual(blocktype, BlockType.ULIST)

    def test_block_to_block_type_olist(self):
        md = "1. here is an olist\n2. -more olist\n3. - more olist"
        print(md)
        blocktype = block_to_blocktype(md)
        print(blocktype)
        self.assertEqual(blocktype, BlockType.OLIST)

    def test_block_to_block_type_paragraph(self):
        md = "1. here is a paragraph\n2. -more paragraph\n4. - more paragraph"
        print(md)
        blocktype = block_to_blocktype(md)
        print(blocktype)
        self.assertEqual(blocktype, BlockType.PARAGRAPH)
    """

    def test_headings(self):
        md = "### This is a [link](www.google.com) inside of a heading\n\n#### This is a heading with nothing in it"
        print(md)
        node = markdown_to_html_node(md)
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><h3>This is a <a href=\"www.google.com\">link</a> inside of a heading</h3><h4>This is a heading with nothing in it</h4></div>",
        )

    # def test_unordered_list(self):
    #     md = "- This is **bold** blah\n- This is _italics_\n- This is plain.\n"
    #     print(md)
    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     print(html)
    #     self.assertEqual(
    #         html,
    #         "<div><ul><li>This is <b>bold</b> blah</li><li>This is <i>italics</i></li><li>This is plain.</li></ul></div>",
    #     )
    
    # def test_ordered_list(self):
    #     md = "1. This is **bold** blah\n2. This is _italics_\n3. This is plain.\n"
    #     print(md)
    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     print(html)
    #     self.assertEqual(
    #         html,
    #         "<div><ol><li>This is <b>bold</b> blah</li><li>This is <i>italics</i></li><li>This is plain.</li></ol></div>",
    #     )

    # def test_blockquote(self):
    #     md = ">This is **bold** blah\n>This is _italics_\n>This is plain.\n"
    #     print(md)
    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     print(html)
    #     self.assertEqual(
    #         html,
    #         "<div><blockquote>This is <b>bold</b> blah\nThis is <i>italics</i>\nThis is plain.\n</blockquote></div>",
    #     )

    # def test_paragraphs(self):
    #     md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_ text and `code` here\n"
    #     print(md)
    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     print(html)
    #     self.assertEqual(
    #         html,
    #         "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    #     )

    # def test_codeblock(self):
    #     md = "\n```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```\n"
    #     print(md)
    #     node = markdown_to_html_node(md)
    #     #print(node)
    #     html = node.to_html()
    #     print(html)
    #     self.assertEqual(
    #         html,
    #         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
    #     )

if __name__ == "__main__":
    unittest.main()