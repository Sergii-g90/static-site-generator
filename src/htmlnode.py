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

