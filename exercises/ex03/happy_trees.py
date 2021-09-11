"""Drawing forests in a loop."""

__author__ = "730481343"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
counter: int = 0

tree_image: str = ""

if depth > 0: 
    while counter < depth: 
        if counter != depth:
            tree_image = tree_image + TREE + " "
            counter = counter + 1
            print(tree_image)
        else: 
            beat_string = tree_image + TREE
            counter = counter + 1
            print(tree_image)