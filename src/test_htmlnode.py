import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        node = HTMLNode("p", "some text", "children")
        self.assertEqual(node.props_to_html(),'')

    def test_one_prop(self):
        node = HTMLNode("a", "some text", "children", {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(),' href="https://www.google.com"')

    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank", "style": "test"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank" style="test"')

    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)