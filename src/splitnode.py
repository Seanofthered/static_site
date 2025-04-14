from textnode import TextNode, TextType
from extract_links import split_nodes_images, split_nodes_links


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue

        text = old_node.text

        start_index = text.find(delimiter)

        if start_index > 0:
            new_nodes.append(TextNode(text[:start_index], TextType.TEXT))

        end_index = text.find(delimiter, start_index + len(delimiter))
        if end_index == -1:
            raise Exception(f"No closing delimiter found for {delimiter}")

        content_between = text[start_index + len(delimiter):end_index]
        new_nodes.append(TextNode(content_between, text_type))

        remaining_text = text[end_index + len(delimiter):]
        if remaining_text:
            remaining_node = TextNode(remaining_text, TextType.TEXT)
            result_of_recursive_call = split_nodes_delimiter([remaining_node], delimiter, text_type)
            new_nodes.extend(result_of_recursive_call)

    return new_nodes


def text_to_textnodes(text):
    """
    Converts a raw string of markdown-flavored text into a list of TextNode objects.
    """
    # Start with a single text node
    nodes = [TextNode(text, TextType.TEXT)]

    # Apply splitting functions in sequence
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)

    return nodes

def markdown_to_blocks(markdown):
    block_split = markdown.split("\n\n")
    blocks = []
    for string in block_split:
        stripped = string.strip()
        if stripped != "":
            blocks.append(stripped)
    return blocks
