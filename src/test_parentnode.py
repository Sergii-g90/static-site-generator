import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print(f"Parent to html: {parent_node.to_html()}")
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tags(self):
        node1 = ParentNode('', children="test", props={"test": "prop1", "test2": "prop2"})
        with self.assertRaises(ValueError) as context:
            node1.to_html()
        self.assertEqual(str(context.exception), "Parent node must have a tag")

    def test_multiple_leaf_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_node_with_params(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "Some text", {"href": "https://mobile.google.com", "target": "_blank", "style": "test"})
            ],
            props={
                "href": "https://google.com",
                "test1": "property1",
                "test2": "property2"
            }
        )
        self.assertEqual(node.to_html(),'<p href="https://google.com" test1="property1" test2="property2"><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://mobile.google.com" target="_blank" style="test">Some text</a></p>')