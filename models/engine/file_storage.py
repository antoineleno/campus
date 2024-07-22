#!/usr/bin/python3
"""file_storage module"""
import json
import copy
import os
from models.base_model import BaseModel


class FileStorage:
    """Class to store object to json file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all: method to return all object of in objects dictionary
        """
        return self.__objects

    def new(self, obj):
        """Method that generate key for each object then store
        in object dictionary
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save: method to save all objects to a json file
        """
        all_objects = copy.deepcopy(self.__objects)
        for obj_id in all_objects.keys():
            all_objects[obj_id] = all_objects[obj_id].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(all_objects, file)

    def reload(self):
        """reload: Method to reload all objects from json file"""
        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, "r") as file:
                    content = json.load(file)
                    for key, value in content.items():
                        class_name, object_id = key.split('.')
                        cls = eval(class_name)
                        class_instance = cls(**value)
                        self.__objects[key] = class_instance
            except Exception:
                pass

    def delete(self, obj=None):
        """delete: delete an object from __objects

        Args:
            obj (class instance): oject to be delected if exits.
            Defaults to None.
        """
        if obj:
            key_to_delete = obj.__class__.__name__ + '.' + obj.id
            if key_to_delete in self.__objects.keys():
                del self.__objects[key_to_delete]
        else:
            return
