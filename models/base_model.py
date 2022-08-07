#!usr/bin/python3
"""
BaseModel class that defines all common attributes and methods for other classes

"""


import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel class that defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of Basemodel class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            date = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], date)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the instance
        """
        class_name = "[" + self.__class__.__name__ + "]"
        new_dict = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + "(" + self.id + ") " + str(new_dict)

    def save(self):
        """
        Save the instance to the storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of the instance
        """
        dict_new = {}

        for key, values in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dict_new[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    dict_new[key] = values
        dict_new['__class__'] = self.__class__.__name__
        return dict_new
