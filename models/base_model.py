#!/usr/bin/python3
"""
BaseModel class
"""


from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    defines base model attributes and methods
    created_at: The datetime at creation
    updated_at: The datetime of last update
    """

    def __init__(self, *args, **kwargs):
        """
        create à new instance and save the info (Initializes the BaseModel)
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            storage.new(self)

    def __str__(self):
        """
        return output to a specific format
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update updated_at with the current datetime and save it
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the BaseModel
        """
        dictionary = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dictionary[key] = value
        return dictionary
