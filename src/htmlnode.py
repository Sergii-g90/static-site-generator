class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ''
        properties = ""
        for prop in self.props:
            properties += f' {prop}="{self.props[prop]}"'
        return properties

    def __repr__(self):
        return f"HTMLNode:\n    tag: {self.tag}\n    value: {self.value}\n    children: {self.children}\n    props: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('All leaf nodes must have a value')
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{super().props_to_html()}>"
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode:\n    tag: {self.tag}\n    value: {self.value}\n    props: {self.props}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == '':
            raise ValueError('Parent node must have a tag')
        if self.children is None or self.children == '':
            raise ValueError('Parent node must have a children')
        converted = ""
        for item in self.children:
            converted += item.to_html()

        return f"<{self.tag}{self.props_to_html()}>{converted}</{self.tag}>"
