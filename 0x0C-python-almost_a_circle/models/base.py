#!/usr/bin/python3
"""module ´´base´´ with base class"""
import json
import csv


class Base:
    """Base class
    Attributes:
        __nb_objects: private class attribure
        id (int): instance public attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id (int): instance public attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w') as f:
            new_list = []
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                for each_obj in list_objs:
                    obj_dict = each_obj.to_dictionary()
                    new_list.append(obj_dict)
                string_json = cls.to_json_string(new_list)
                f.write(string_json)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that serializes in CSV"""
        file_name = "{}.csv".format(cls.__name__)
        with open(file_name, 'w', newline='') as f:
            outer_list = []
            writer = csv.writer(f)
            if list_objs is None:
                writer.writerows(outer_list)
            else:
                if cls.__name__ == "Rectangle":
                    for each_obj in list_objs:
                        new_list = []
                        new_list.append(each_obj.id)
                        new_list.append(each_obj.width)
                        new_list.append(each_obj.height)
                        new_list.append(each_obj.x)
                        new_list.append(each_obj.y)
                        outer_list.append(new_list)
                    writer.writerows(outer_list)
                if cls.__name__ == "Square":
                    for each_obj in list_objs:
                        new_list = []
                        new_list.append(each_obj.id)
                        new_list.append(each_obj.size)
                        new_list.append(each_obj.x)
                        new_list.append(each_obj.y)
                        outer_list.append(new_list)
                    writer.writerows(outer_list)

    @staticmethod
    def from_json_string(json_string):
        """Static method that returns the list of the JSON string
        representation json_string
        """
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes already
        set
        """
        dummy_ins = cls(1, 1)
        dummy_ins.update(**dictionary)
        return dummy_ins

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name) as f:
                list_of_instances = []
                objs_json_str = f.read()
                insta_dicts = cls.from_json_string(objs_json_str)
                for obj in insta_dicts:
                    obj_inst = cls.create(**obj)
                    list_of_instances.append(obj_inst)

            return list_of_instances

        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """class method that deserializes in CSV"""
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, newline='') as f:
                list_of_instances = []
                if cls.__name__ == "Rectangle":
                    attr_name = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Square":
                    attr_name = ['id', 'size', 'x', 'y']
                reader = csv.reader(f)
                for row in reader:
                    obj = {}
                    i = 0
                    for vals in row:
                        obj[attr_name[i]] = int(vals)
                        i += 1
                    obj_inst = cls.create(**obj)
                    list_of_instances.append(obj_inst)

            return list_of_instances

        except IOError:
            return []
