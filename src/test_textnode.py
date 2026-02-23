import unittest

from textnode import TextNode, TextType


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
        node = TextNode("Node text", TextType.LINKS, "https://google.com")
        node2 = TextNode("Node text", TextType.LINKS, "https://google.com")
        self.assertEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Node text", TextType.LINKS, "https://google.com")
        node2 = TextNode("Node text", TextType.PLAIN, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_link_not_eq(self):
        node = TextNode("Node text", TextType.LINKS, "https://google.com")
        node2 = TextNode("Node text", TextType.LINKS, "https://mobile.google.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()