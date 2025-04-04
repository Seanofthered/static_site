class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        convert = ""
        if not self.props:
            return ""
        else:
            for key,value in self.props.items():
                convert += f' {key}="{value}"'
        return convert

    def __repr__(self):
        return f"HTMLNode('{self.tag!r}', '{self.value!r}', {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, props)
        self.value = value


    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")

        if not self.tag:
            return self.value

        html = f"<{self.tag}"

        if self.props:
            for key, value in self.props.items():
                html += f' {key}="{value}"'

        html += f">{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError ("Invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
