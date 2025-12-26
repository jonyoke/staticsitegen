from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "CODE"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_blocktype(markdown):

    if markdown.startswith("# ") or markdown.startswith("## ") or  markdown.startswith("### ") or  markdown.startswith("#### ") or  markdown.startswith("##### ") or markdown.startswith("###### "):
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    is_quote, is_ulist, is_olist, olist_cntr = True, True, True, 0
    for line in markdown.split("\n"):
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