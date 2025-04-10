import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    alt_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_images

def extract_markdown_links(text):
    alt_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return alt_links

def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        extracted = extract_markdown_images(text)

        while extracted:
            alt_text, url = extracted
            found_markdown = f"![{alt_text}]({url})"
            sections = text.split(found_markdown, 1)
            before_text = sections[0]
            after_text = sections[1] if len(sections) > 1 else ""

            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            text = after_text
            extracted = extract_markdown_images(text)

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        extracted = extract_markdown_links(text)

        while extracted:
            alt_text, url = extracted
            found_markdown = f"[{alt_text}]({url})"
            sections = text.split(found_markdown, 1)
            before_text = sections[0]
            after_text = sections[1] if len(sections) > 1 else ""

            if before_text:
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.LINK, url))

            text = after_text
            extracted = extract_markdown_links(text)

    return new_nodes
