
class HTMLNode:
    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        props_str = ''
        for item in self.props.items():
            props_str += f' {item[0]}="{item[1]}"'
        return props_str
    
    def __repr__(self):
        print(f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})")

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag=tag, value=value, children=[])
 
    def to_html(self):
        if not self.value:
            raise ValueError("A leaf node must have a value.")
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
  
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("A Parent node must have a tag.")
        if not self.children:
            raise ValueError("A Parent node must have children.")
        html_str = f"<{self.tag}>"
        for child in self.children:
            html_str += child.to_html()
        html_str += f"</{self.tag}>"
        return html_str