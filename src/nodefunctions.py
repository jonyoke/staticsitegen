import re

from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode

def text_node_to_html_node(text_node):
    #Returns: LeafNode
    #Not part of the TextNode class
    #Expects a TextNode that is one of the types of TextType
    if not text_node:
        raise ValueError("trying to convert TextNode to LeafNode but text_node is empty")
    if text_node.text_type == None:
        raise ValueError("trying to convert TextNode to LeafNode but text_node.text_type is None")
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value="", props={"src":text_node.url,"alt":text_node.text})
        case _:
            raise ValueError("trying to convert TextNode to LeafNode but text_node.text_type is not a valid TextType")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #No nested nodes!
    new_nodes = []
    for node in old_nodes:
        #print(node)
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
        else:
            num_delimeters = node.text.count(delimiter)
            if num_delimeters % 2 != 0:
                raise Exception("Odd number of delimiters - invalid Markdown syntax")
            split_texts = node.text.split(delimiter)

            for i in range(len(split_texts)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(split_texts[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(split_texts[i], text_type))
    
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
            
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    #No nested nodes!
    new_nodes = []
    for node in old_nodes:
        #print(f"Printing node in loop {node}")
        if not node.text_type == TextType.TEXT:  #If it's not an IMAGE, just add it bc NO NESTED
            new_nodes.append(node)
        else:
            matches = extract_markdown_images(node.text)
            #print(f"Printing matches {matches}")
            if len(matches) > 0:
                sections = node.text.split(f"![{matches[0][0]}]({matches[0][1]})", 1)
                #print(f"Printing sections {sections}")
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(matches[0][0], TextType.IMAGE, matches[0][1]))
                new_nodes.extend(split_nodes_image([TextNode(sections[1], TextType.TEXT)]))
            else:
                if len(node.text) > 0:
                    new_nodes.append(node)
    return new_nodes     

def split_nodes_link(old_nodes):
    #No nested nodes!
    new_nodes = []
    for node in old_nodes:
        #print(f"Printing node in loop {node}")
        if not node.text_type == TextType.TEXT:  #If it's not an IMAGE, just add it bc NO NESTED
            new_nodes.append(node)
        else:
            matches = extract_markdown_links(node.text)
            #print(f"Printing matches {matches}")
            if len(matches) > 0:
                sections = node.text.split(f"[{matches[0][0]}]({matches[0][1]})", 1)
                #print(f"Printing sections {sections}")
                if len(sections[0]) > 0:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(matches[0][0], TextType.LINK, matches[0][1]))
                new_nodes.extend(split_nodes_link([TextNode(sections[1], TextType.TEXT)]))
            else:
                if len(node.text) > 0:
                    new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)

    return new_nodes


    