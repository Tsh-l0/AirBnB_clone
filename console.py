#!/usr/bin/python3
"""
Entry point for the cmd interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class, command interpreter
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        When there is no entry in the command line
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
