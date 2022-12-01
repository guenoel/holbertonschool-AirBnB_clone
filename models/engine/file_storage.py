import json

class FileStorage:
    __file_path = "file.json"
    __objects = {} #dict of instances
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        json_objects = {} #empty list created
        for key in self.__objects: #loop to treat each key that correspond to an instance (type BaseModel)
            json_object = self.__objects[key].to_dict() #take each key (instance) and convert to a dict
            json_objects[key] = json_object # empty the previous dict to an new dict of dict
        with open(self.__file_path, "w") as f: # open file as a stream
            json.dump(json_objects, f, indent=4) # convert dict of dict to a json...
            # ...string stored to a file (indented for smart display)
    
    def reload(self):
        try:
            from models.base_model import BaseModel #import here (not at the top of the file) to avoid circular import

            with open(self.__file_path, "r") as f:
                dict_of_dict = json.load(f) # lit le fichier, recupere la string et convertit en dict
            for key, value in dict_of_dict.items(): # items method returns a view object that ...
                # ...displays a list of dictionary's (key, value) tuple pairs: dict_items([(key, value), (key, value), ...])
                obj = BaseModel(**value) #the value is in fact a dictionary with all arguments (kwargs list): __init__ create...
                # an object of class BaseModel
                self.new(obj) # we can give this object to the "new" method that put this object in the dict __objects (a dict of objects)
        except Exception:
            pass
