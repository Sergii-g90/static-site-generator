from textnode import TextType, TextNode


def main():
    new_node = TextNode("Some text", TextType.LINKS, "https://google.com")
    print(new_node)

main()