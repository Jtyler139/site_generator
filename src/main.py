from textnode import TextNode
from textnode import TextType

def main():
    my_text_node = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    print(my_text_node)

if __name__ == "__main__":
    main()