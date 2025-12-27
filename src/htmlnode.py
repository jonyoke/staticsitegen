

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              #A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value          #A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children    #A list of HTMLNode objects representing the children of this node      
        self.props = props          #A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}


    def to_html(self):
        raise NotImplementedError("to_html in HTMLNode should be overwritten")
    
    def props_to_html(self):
        if not self.props:
            return None
        str = ""
        for key, val in self.props.items():
            str += f' {key}="{val}"'
        return str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        #print(f"declaring props as {self.props}")

    def to_html(self):
        if self.value == None:
            raise ValueError("trying to convert LeafNode to html, but value is None")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        #EXPECTS children to be a
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("trying to convert ParentNode to html, but tag is None")
        if self.children == None or self.children == []:
            raise ValueError(f"trying to convert ParentNode to html, but children is {self.children}")
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html