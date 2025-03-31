from htmlnode import HTMLNode


def test_props_to_html_empty():
    # Test with empty props
    node = HTMLNode(props=None)
    assert node.props_to_html() == ""

    node = HTMLNode(props={})
    assert node.props_to_html() == ""

def test_props_to_html_one_prop():
    # Test with one property
    node = HTMLNode(props={"href": "https://www.google.com"})
    assert node.props_to_html() == ' href="https://www.google.com"'

def test_props_to_html_multiple_props():
    # Test with multiple properties
    node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
    # The order of properties in a dictionary might vary, so we need to check if both are present
    result = node.props_to_html()
    assert ' href="https://www.google.com"' in result
    assert ' target="_blank"' in result
    # Make sure the length is correct (no extra characters)
    assert len(result) == len(' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    # Run tests
    test_props_to_html_empty()
    test_props_to_html_one_prop()
    test_props_to_html_multiple_props()
    print("All tests passed!")
