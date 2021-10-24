from GenericLinkedList import GenericLinkedList
__header__ = "GenericMainMenu"
#  The Generic Main Menu program is just a interface for a user to test all the functions
# within the Generic Linked List class.
__author__ = "Andy"
__since__ = "10/23/2021"
__purpose__ = "Future Reference and Practice"
def main():
    header = """
            \t\t+---------------------+
            \t\t| Generic Linked List |
            \t\t+---------------------+ 
            """
    options = """
          Commands:
          print:                   shows contents of the linked list
          size:                    prints the number of nodes in the list
          clear:                   removes all the nodes in the list
          quit:                    exits the program
          add <item> <index>:      adds an item to the linked list
          remove <index>:          removes an item or location of an item in the list
          find <item> <index>:     prints Found if the item is in the list, Not Found otherwise
          reverse:                 reverses the linked list
          sort:                    sorts the current linked list
          save <file>:             saves the list to a file
          load <file>:             loads the list from a file
          """
    print(header)
    print(options)
    lst = GenericLinkedList()
    while True:
        print("GLL#> ", end="")
        # Command prompt for the user to manipulate the given linked
        # list.
        cmd = input().split(" ")
        # Three user input options
        option = None; arg1 = None; arg2 = None
        if len(cmd) == 0 or len(cmd) > 3:
            print("Invalid Option")
        elif len(cmd) >= 1:
            option = cmd[0]
            if len(cmd) >= 2:
                arg1 = cmd[1]
                if len(cmd) == 3:
                    arg2 = cmd[2]
        if option is not None:
            if option == "print":
                print(lst.print())
            elif option == "size":
                print(lst.get_size())
            elif option == "clear":
                lst.reset_head()
            elif option == "quit":
                break
            elif option == "add" and arg1 is not None:
                if arg2 is not None:
                    try:
                        lst.add_node(arg1, int(arg2))
                    except ValueError:
                        lst.add_node(arg1)
                else:
                    lst.add_node(arg1)
            elif option == "remove" and arg1 is not None:
                try:
                    lst.remove_node(int(arg1))
                except ValueError:
                    print("Incorrect Index")
            elif option == "reverse":
                lst.reverse()
            elif option == "find" and arg1 is not None:
                result = False
                if arg2 is not None:
                    try:
                        result = lst.find_node(arg1, int(arg2))
                    except ValueError:
                        result = lst.find_node(arg1)
                else:
                    result = lst.find_node(arg1)
                print(("Not Found", "Found")[result])
            elif option == "sort":
                lst.merge_sort()
            elif option == "save" and arg1 is not None:
                lst.save_to_file(arg1)
            elif option == "load" and arg1 is not None:
                lst.load_from_file(arg1)
            else:
                print("Invalid Option")

if __name__ == "__main__":
    main()