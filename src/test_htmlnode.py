import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHMTLNode(unittest.TestCase):
    """
    def test_hmtlnode1(self):
        node = LeafNode("p", "Hello, world!")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_hmtlnode2(self):
        node = LeafNode("a", "google.com", props={"href": "https://www.google.com"})
        print(node.to_html())
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">google.com</a>")

    def test_hmtlnode3(self):
        node = LeafNode("i", "italics")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<i>italics</i>")

    def test_hmtlnode4(self):
        node = LeafNode("b", "bold")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<b>bold</b>")

    def test_hmtlnode5(self):
        node = LeafNode("code", "This is code")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<code>This is code</code>")

    def test_hmtlnode6(self):
        node = LeafNode("h5", "Heading 5")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<h5>Heading 5</h5>")

    def test_hmtlnode7(self):
        img_props = {"src" : "url/of/image.jpg", "alt" : "Description of image"}
        node = LeafNode("img", value="random nonsense", props=img_props)
        print(node.to_html())
        self.assertEqual(node.to_html(), "<img src=\"url/of/image.jpg\" alt=\"Description of image\">random nonsense</img>")

    def test_hmtlnode8(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    """



if __name__ == "__main__":
    unittest.main()