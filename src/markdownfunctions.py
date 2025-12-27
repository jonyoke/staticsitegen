from enum import Enum

from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from nodefunctions import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    H1 = "h1"
    H2 = "h2"
    H3 = "h3"
    H4 = "h4"
    H5 = "h5"
    H6 = "h6"
    CODE = "CODE"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_blocktype(markdown):

    if markdown.startswith("# "):
        return BlockType.H1
    if markdown.startswith("## "):
        return BlockType.H2
    if markdown.startswith("### "):
        return BlockType.H3
    if markdown.startswith("#### "):
        return BlockType.H4
    if markdown.startswith("##### "):
        return BlockType.H5
    if markdown.startswith("###### "):
        return BlockType.H6       
    
    lines = markdown.split("\n")
    if lines[0].strip() == "```" and lines[-1].strip() == "```":
        return BlockType.CODE

    is_quote, is_ulist, is_olist, olist_cntr = True, True, True, 0
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("- "):
            is_ulist = False
        olist_cntr += 1
        if not line.startswith(f"{olist_cntr}. "):
            is_olist = False
    if is_quote:
        return BlockType.QUOTE
    if is_ulist:
        return BlockType.ULIST
    if is_olist:
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    return list(filter(None,map(str.strip, markdown.split("\n\n"))))

def markdown_to_html_node(markdown):
    # Converts a full markdown document into a single parent HTMLNode
    # The Big Function that does The Thing
    blocks = markdown_to_blocks(markdown)
    #print(f"blocks are: {blocks}")

    div_child_nodes = []
    for block in blocks:
        blocktype = block_to_blocktype(block)
        #print(f"{block} ... is {blocktype}")
        if blocktype == BlockType.CODE:
            #SPECIAL HANDLING FOR CODE
            lines = block.split("\n")
            inner_lines = lines[1:-1]
            code_text = "\n".join(inner_lines) + "\n"
            div_child_nodes.append(ParentNode("pre",[text_node_to_html_node(TextNode(code_text,TextType.CODE))]))
        else:
            match blocktype:
                case BlockType.H1:
                    tag = "h1"
                    child_nodes = text_to_textnodes(block[len("# "):])
                case BlockType.H2:
                    tag = "h2"
                    child_nodes = text_to_textnodes(block[len("## "):])
                case BlockType.H3:
                    tag = "h3"
                    child_nodes = text_to_textnodes(block[len("### "):])
                case BlockType.H4:
                    tag = "h4"
                    child_nodes = text_to_textnodes(block[len("#### "):])
                case BlockType.H5:
                    tag = "h5"
                    child_nodes = text_to_textnodes(block[len("##### "):])
                case BlockType.H6:
                    tag = "h6"
                    child_nodes = text_to_textnodes(block[len("###### "):])
                case BlockType.QUOTE:
                    tag = "blockquote"
                    lines = block.split("\n")
                    inner_lines = list(map(lambda x: x.lstrip(">"), lines))
                    stripped_text = "\n".join(inner_lines) + "\n"
                    child_nodes = text_to_textnodes(stripped_text)
                case BlockType.ULIST:
                    tag = "ul"
                    lines = block.split("\n")
                    inner_lines = list(map(lambda x: x.lstrip("- "), lines))
                    children = []
                    for inner_line in inner_lines:
                        child_nodes = text_to_textnodes(inner_line)
                        li_children = list(map(text_node_to_html_node, child_nodes))
                        children.append(ParentNode("li", li_children))
                case BlockType.OLIST:
                    tag = "ol"
                    lines = block.split("\n")
                    children = []
                    for i in range(len(lines)):
                        inner_line = lines[i].lstrip(f"{i+1}. ")
                        child_nodes = text_to_textnodes(inner_line)
                        li_children = list(map(text_node_to_html_node, child_nodes))
                        children.append(ParentNode("li", li_children))
                case BlockType.PARAGRAPH:
                    tag = "p"
                    lines = block.split("\n")
                    stripped_text = " ".join(line.strip() for line in lines)
                    child_nodes = text_to_textnodes(stripped_text)
                case _:
                    raise ValueError(f"Expected a valid BlockType in markdown_to_html_node, got {blocktype} instead")
            
            if blocktype != BlockType.ULIST and blocktype != BlockType.OLIST:
                children = list(map(text_node_to_html_node, child_nodes))
            #print(f"Printing children: {children}")
            div_child_nodes.append(ParentNode(tag,children))

    return ParentNode(tag="div", children=div_child_nodes)