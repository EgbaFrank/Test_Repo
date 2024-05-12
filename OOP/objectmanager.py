#!/usr/bin/env python3
# Command line object manager
import cmd
from item import Item


class Object_manager(cmd.Cmd):
    """Command line interpreter for managing item objects"""
    intro = "Welcome to the Item object manager shell (type help for a list of commands)"
    prompt = "(items) "

    def __init__(self):
        super().__init__()
        self.items = []

    def do_create(self, arg):
        """Creates a new item instance"""
        args = arg.split()

        if len(args) != 3:
            print("Usage: create <name> <price> <quantity>")
            return

        name, price, quantity = args

        try:
            price = int(price)
            quantity = int(quantity)

        except ValueError:
            print("price and quantity must be integers")
            return

        new_item = Item(name, price, quantity)
        self.items.append(new_item)
        print(f"Created new item\n\n{new_item}")

    def do_list(self, arg):
        """Lists all items"""
        for item in self.items:
            print(item)

    def do_exit(self, arg):
        """Exits the interpreter"""
        print("Thanks for dropping in")
        return True

if __name__ == "__main__":
    Object_manager().cmdloop()
