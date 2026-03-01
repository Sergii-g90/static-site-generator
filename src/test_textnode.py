import unittest

from textnode import TextNode, TextType,text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is first text node", TextType.BOLD, "https://google.com")
        node2 = TextNode("This is second text node", TextType.BOLD, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_eq_all_fields(self):
        node = TextNode("Node text", TextType.LINK, "https://google.com")
        node2 = TextNode("Node text", TextType.LINK, "https://google.com")
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Node text", TextType.LINK, "https://google.com")
        node2 = TextNode("Node text", TextType.TEXT, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_link_not_eq(self):
        node = TextNode("Node text", TextType.LINK, "https://google.com")
        node2 = TextNode("Node text", TextType.LINK, "https://mobile.google.com")
        self.assertNotEqual(node, node2)

    def test_to_html_text_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_to_html_link_type(self):
        node = TextNode("Node text", TextType.LINK, "https://google.com")
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.to_html(),'<a href="https://google.com">Node text</a>')

    def test_to_html_bold_type(self):
        node = TextNode("Bold text", TextType.BOLD)
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.to_html(),'<b>Bold text</b>')

    def test_to_html_italic_type(self):
        node = TextNode("Italic text", TextType.ITALIC)
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.to_html(), '<i>Italic text</i>')

    def test_to_html_code(self):
        node = TextNode("Code text", TextType.CODE)
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.to_html(), '<code>Code text</code>')

    def test_to_html_image(self):
        node = TextNode("Image alt text", TextType.IMAGE, "https://google.com/image.png")
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.to_html(), '<img src="https://google.com/image.png" alt="Image alt text">')

    def test_to_html_wrong_type(self):
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(TextNode("Code text", "Test"))
        self.assertEqual(str(context.exception), "Text type is not correct")



if __name__ == "__main__":
    unittest.main()