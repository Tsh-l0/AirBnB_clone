#!/usr/bin/python3
"""
Entry point for the cmd interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class, command interpreter
    """
    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place
            "Review": Review
            }

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves the JSON file and
        prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on class
        name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name
        """
        args = arg.split()
        objs = storage.all()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        to_print = [str(obj) for obj in objs.values() if not args or
                    obj.__class__.__name__ == args[0]]
        print(to_print)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')

        if attr_name in instance.__class__.__dict__:
            attr_type = type(instance.__class__.__dict__[attr_name])
            instance.__dict__[attr_name] = attr_type(attr_value)
        else:
            instance.__dict__[attr_name] = attr_value
        instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
