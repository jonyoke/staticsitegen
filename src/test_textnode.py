import unittest

from textnode import TextNode, TextType
from nodefunctions import *
from markdownfunctions import *

class TestTextNode(unittest.TestCase):
    """     
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)  

    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text ode", TextType.BOLD)
        self.assertNotEqual(node, node2)    

    def test_noteq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, url="http://www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_conversion_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())

    def test_conversion_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())

    def test_conversion_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())

    def test_conversion_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())

    def test_conversion_link(self):
        node = TextNode("This is a link node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href" : "www.google.com"})
        print(html_node.to_html())

    def test_conversion_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "www.myimageurl.com/img")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"www.myimageurl.com/img", "alt":"This is an image node"})
        print(html_node.to_html())

    def test_conversion_empty1(self):
        node = None
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())

    def test_conversion_empty2(self):
        node = TextNode(None, TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())

    def test_conversion_empty3(self):
        node = TextNode("This is a text node", "booty")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.props, None)
        print(html_node.to_html())
    

    def test_split1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result_to_test_against = [
                                    TextNode("This is text with a ", TextType.TEXT),
                                    TextNode("code block", TextType.CODE),
                                    TextNode(" word", TextType.TEXT),
                                ]
        self.assertEqual(new_nodes, result_to_test_against)
        print(new_nodes)


    def test_split2(self):
        node = TextNode("_italics_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        result_to_test_against = [
                                    TextNode("", TextType.TEXT),
                                    TextNode("italics", TextType.ITALIC),
                                    TextNode(" word", TextType.TEXT),
                                ]
        self.assertEqual(new_nodes, result_to_test_against)
        print(new_nodes)

    def test_split3(self):
        node = TextNode("This is text with two **bolded** in **the** middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result_to_test_against = [
                                    TextNode("This is text with two ", TextType.TEXT),
                                    TextNode("bolded", TextType.BOLD),
                                    TextNode(" in ", TextType.TEXT),
                                    TextNode("the", TextType.BOLD),
                                    TextNode(" middle", TextType.TEXT),
                                ]
        self.assertEqual(new_nodes, result_to_test_against)
        print(new_nodes)

    def test_split4(self):
        print("Test 4********")
        node1 = TextNode("This is text with two **bolded** in **the** middle", TextType.TEXT)
        node2 = TextNode("Already _bolded_ text", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        print(new_nodes)
        result_to_test_against = [
                                    TextNode("This is text with two ", TextType.TEXT),
                                    TextNode("bolded", TextType.BOLD),
                                    TextNode(" in ", TextType.TEXT),
                                    TextNode("the", TextType.BOLD),
                                    TextNode(" middle", TextType.TEXT),
                                    TextNode("Already _bolded_ text", TextType.BOLD)
                                ]
        self.assertEqual(new_nodes, result_to_test_against)
        

    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        print(matches)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        print(matches)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images1(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images2(self):
        node = TextNode(
            "![tester image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual(
            [TextNode("tester image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")],
            new_nodes,
        )

    def test_split_images3(self):
        node = TextNode(
            "![tester image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual([node], new_nodes)

    def test_split_images4(self):
        node = TextNode(
            "![tester image]https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual([node], new_nodes)
    
    def test_split_links1(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links2(self):
        node = TextNode(
            "[tester link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual(
            [TextNode("tester link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png")],
            new_nodes,
        )

    def test_split_links3(self):
        node = TextNode(
            "[tester link](https://i.imgur.com/zjjcJKZ.png)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual([node], new_nodes)

    def test_split_links4(self):
        node = TextNode(
            "[tester link]https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual([node], new_nodes)


    def test_split_all1(self):
        text = "This is **text** with an _italic_ word and a `code block` " \
        "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) " \
        "and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual(
            new_nodes, 
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        ) 

    def test_split_all2(self):
        text = " [link](https://boot.dev) **some bold text** [link](https://boot.dev) [link](https://boot.dev) [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        print(f"Printing new_nodes {new_nodes}")
        self.assertListEqual(
            new_nodes, 
            [
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" ", TextType.TEXT),
                TextNode("some bold text", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )

    def test_markdown_to_blocks2(self):
        md = "# This is a heading\n\n" \
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n\n" \
                "- This is the first list item in a list block\n" \
                "- This is a list item     \n" \
                "- This is another list item    \n\n\n\n\n"
        print(md)
        blocks = markdown_to_blocks(md)
        print(blocks)
        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item     \n- This is another list item"
            ],
        ) """
    
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

if __name__ == "__main__":
    unittest.main()