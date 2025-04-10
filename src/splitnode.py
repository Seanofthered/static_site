from textnode import TextNode, TextType



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
