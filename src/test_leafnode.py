import unittest

from htmlnode import LeafNode, HTMLNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Raw text", '{"href": "https://google.com"}')
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Some text", {"href": "https://google.com", "target": "_blank", "style": "test"})
        self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank" style="test">Some text</a>')