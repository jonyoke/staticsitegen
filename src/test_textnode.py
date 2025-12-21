import unittest

from textnode import TextNode, TextType
from nodefunctions import *

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
        print(new_nodes) """


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
      

if __name__ == "__main__":
    unittest.main()