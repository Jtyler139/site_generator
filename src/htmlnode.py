from enum import Enum





class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        dict_string = ""
        for key, value in self.props.items():
            dict_string = dict_string + f' {key}="{value}"'
        return dict_string
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children  and self.props == other.props
    
    def __repr__(self):
        return f"HTMLNode:{self.tag}, Value:{self.value}, Children:{self.children}, Props:{self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode:{self.tag}, Value:{self.value}, Props:{self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: missing tag")
        if self.children == []:
            raise ValueError("invalid HTML: missing children")
        return f"<{self.tag}{self.props_to_html()}>{"".join([child.to_html() for child in self.children])}</{self.tag}>"