#!/usr/bin/python3
"""
command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    console
    """
    prompt = "(hbnb)"

    def emptyline(self):
        """
        do nothing and pass the line
        """
        pass

    def do_quit(self, arg):
        """
        exit the programm
        """
        raise SystemExit

    def do_EOF(self, arg):
        """
        exit the programm
        """
        raise SystemExit

    def help_quit(self):
        """
        show quit description
        """
        print("Quit command used to exit the program")
        print()

    def help_EOF(self):
        """
        show EOF description
        """
        print("EOF command used to exit the program")
        print()

    def do_create(self, args):
        """
        create a new instance
        """
        className = args.split()
        if self.check_for_class(className):
            new_instance = eval("{}()".format(className[0]))
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        print an specific instance
        """
        class_id = arg.split()
        if self.check_for_class(class_id) and self.check_for_id(class_id):
            dict = storage.all()
            print("{}".format(dict[class_id[0] + "." + class_id[1]]))

    def do_destroy(self, args):
        """
        delete an specific instance
        """
        class_id = args.split()
        if self.check_for_class(class_id) and self.check_for_id(class_id):
            dict = storage.all()
            del dict[class_id[0] + "." + class_id[1]]
            storage.save()

    def do_all(self, args):
        """
        print an specific class or all classes
        """
        newlist = []
        args_sp = args.split()
        for key, value in storage.all().items():
            className = key.split(".")
            if len(args) == 0:
                newlist.append(value.__str__())
            elif className[0] == args_sp[0]:
                newlist.append(value.__str__())
        if bool(newlist) is False:
            print("** class doesn't exist **")
        else:
            print(newlist)

    def do_update(self, args):
        """
        create or update an attribute value in
        a specific instance
        """
        args_sp = args.split()
        if (self.check_for_class(args_sp) and self.check_for_id(args_sp) and
                self.check_for_attribute(args_sp)):
            for i in range(len(args_sp)):
                args_sp[i] = args_sp[i].strip('"')
            class_id = args_sp[0] + "." + args_sp[1]
            attribute = args_sp[2]
            upd_instance = storage.all().get(class_id)
            try:
                upd_attr = getattr(upd_instance, attribute)
            finally:        # change exept
                upd_attr = ""
            type_attr = type(upd_attr)
            setattr(upd_instance, attribute, type_attr(args_sp[3]))
            upd_instance.save()

    def check_for_class(self, args):
        """
        check if the input is good and if the class exists
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        else:
            try:
                check = eval("{}()".format(args[0]))
                dict = storage.all()
                del dict[args[0] + "." + check.id]
                return True
            finally:        # change exept
                print("** class doesn't exist **")
                return False

    def check_for_id(self, args):
        """
        check if the input is good and if the instance id
        is present
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        key = args[0] + "." + args[1]
        if key in storage.all():
            return True
        else:
            print("** no instance found **")
            return False

    def check_for_attribute(self, args):
        """
        check if the input is good and if attribute
        name and value are present
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        elif len(args) < 4:
            print("** value missing **")
            return False
        elif args[3] in ['id', 'updated_at', 'created_at']:
            return False
        else:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
