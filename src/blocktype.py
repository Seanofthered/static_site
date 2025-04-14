from enum import Enum

BlockType = Enum('BlockType', ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list'])


def block_to_block_type(block):
    # Check for heading (1-6 # followed by space)
    if block.startswith("#"):
        hash_part = block.split(" ", 1)[0]
        if 1 <= len(hash_part) <= 6 and len(block) > len(hash_part) and block[len(hash_part)] == " ":
            return BlockType.heading

    # Check for code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code

    # Check for quote block
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return BlockType.quote

    # Check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.unordered_list

    # Check for ordered list
    ordered_list = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i+1}. "
        if not line.startswith(expected_prefix):
            ordered_list = False
            break
    if ordered_list:
        return BlockType.ordered_list

    # Default to paragraph
    return BlockType.paragraph
