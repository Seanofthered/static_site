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
