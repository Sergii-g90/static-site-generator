from textnode import TextType
from textnode import TextNode

def main():
    new_node = TextNode("Some text", TextType.LINKS, "https://google.com")
    print(new_node)

main()